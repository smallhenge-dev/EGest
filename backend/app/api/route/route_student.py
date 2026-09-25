from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.database import session
from backend.app.schemas.student import StudentCreate, StudentRead, StudentUpdate
from backend.app.services import service_student

route = APIRouter(prefix="/api/v1", tags=["students"])
Session = session()


@route.get("/students/info", response_model=list[StudentRead], status_code=status.HTTP_200_OK)
async def affiche_student(db: AsyncSession = Depends(Session.get_db)):
    students = await service_student.read_list(db)
    return [StudentRead.model_validate(student) for student in students]


@route.get("/students/info/{student_id}", response_model=StudentRead, status_code=status.HTTP_200_OK)
async def affiche_student_by_id(student_id: int, db: AsyncSession = Depends(Session.get_db)):
    result = await service_student.read_by_id(db, student_id)
    if result is None:
        raise HTTPException(status_code=404, detail="cet etudiant n'existe pas")
    return StudentRead.model_validate(result)


@route.post("/students/info", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
async def create_student(student_data: StudentCreate, db: AsyncSession = Depends(Session.get_db)):
    try:
        new_student = await service_student.create_student(db, student_data)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return StudentRead.model_validate(new_student)


@route.put("/students/info/{student_id}", response_model=StudentRead, status_code=status.HTTP_200_OK)
async def update_student(student_id: int, student_data: StudentUpdate, db: AsyncSession = Depends(Session.get_db)):
    try:
        updated_student = await service_student.update_student(db, student_id, student_data)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    if updated_student is None:
        raise HTTPException(status_code=404, detail="cet etudiant n'existe pas")
    return StudentRead.model_validate(updated_student)


@route.delete("/students/info/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int, db: AsyncSession = Depends(Session.get_db)):
    deleted_student = await service_student.delete_student(db, student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail="cet etudiant n'existe pas")
    return {"message": "etudiant supprimé avec succès"}