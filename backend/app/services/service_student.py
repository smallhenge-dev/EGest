from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.models.enrollment import Enrollment
from backend.app.models.student import Student
from backend.app.schemas.student import StudentCreate, StudentUpdate


async def _find_duplicate(db: AsyncSession, field_name: str, value: str, exclude_student_id: int | None = None):
    stmt = select(Student).where(getattr(Student, field_name) == value)
    if exclude_student_id is not None:
        stmt = stmt.where(Student.id != exclude_student_id)
    result = await db.execute(stmt)
    return result.scalars().first()


async def read_list(db: AsyncSession):
    result = await db.execute(select(Student))
    return list(result.scalars().all())


async def read_by_id(db: AsyncSession, student_id: int):
    result = await db.execute(select(Student).where(Student.id == student_id))
    return result.scalars().first()


async def create_student(db: AsyncSession, student_data: StudentCreate):
    if student_data.email and await _find_duplicate(db, "email", student_data.email):
        raise ValueError("Un étudiant avec cet email existe déjà.")
    if student_data.matricule and await _find_duplicate(db, "matricule", student_data.matricule):
        raise ValueError("Un étudiant avec cette matricule existe déjà.")

    new_student = Student(**student_data.model_dump())
    db.add(new_student)
    try:
        await db.commit()
    except IntegrityError as exc:
        await db.rollback()
        raise ValueError("Un étudiant avec cet email ou cette matricule existe déjà.") from exc
    await db.refresh(new_student)
    return new_student


async def update_student(db: AsyncSession, student_id: int, student_data: StudentUpdate):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalars().first()
    if student is None:
        return None

    update_data = student_data.model_dump(exclude_unset=True)

    if "email" in update_data and update_data["email"] is not None:
        existing_email = await _find_duplicate(db, "email", update_data["email"], student_id)
        if existing_email is not None:
            raise ValueError("Un étudiant avec cet email existe déjà.")

    if "matricule" in update_data and update_data["matricule"] is not None:
        existing_matricule = await _find_duplicate(db, "matricule", update_data["matricule"], student_id)
        if existing_matricule is not None:
            raise ValueError("Un étudiant avec cette matricule existe déjà.")

    for key, value in update_data.items():
        setattr(student, key, value)

    try:
        await db.commit()
    except IntegrityError as exc:
        await db.rollback()
        raise ValueError("Un étudiant avec cet email ou cette matricule existe déjà.") from exc
    await db.refresh(student)
    return student


async def delete_student(db: AsyncSession, student_id: int):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalars().first()
    if student is None:
        return None

    enrollments_result = await db.execute(select(Enrollment).where(Enrollment.student_id == student_id))
    for enrollment in enrollments_result.scalars().all():
        await db.delete(enrollment)

    await db.delete(student)
    await db.commit()
    return student