from importlib import import_module
from typing import Any, Type

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.database import session as SessionFactory
from backend.app.schemas.academic_level import AcademicLevelCreate, AcademicLevelRead, AcademicLevelUpdate
from backend.app.schemas.attendance import AttendanceCreate, AttendanceRead, AttendanceUpdate
from backend.app.schemas.attendance_session import AttendanceSessionCreate, AttendanceSessionRead, AttendanceSessionUpdate
from backend.app.schemas.class_sub import ClasseSubjectCreate, ClasseSubjectRead, ClasseSubjectUpdate
from backend.app.schemas.classe import ClasseCreate, ClasseRead, ClasseUpdate
from backend.app.schemas.document import DocumentCreate, DocumentRead, DocumentUpdate
from backend.app.schemas.enrollment import EnrollmentCreate, EnrollmentRead, EnrollmentUpdate
from backend.app.schemas.fee import FeeCreate, FeeRead, FeeUpdate
from backend.app.schemas.grade import GradeCreate, GradeRead, GradeUpdate
from backend.app.schemas.invoice import InvoiceCreate, InvoiceRead, InvoiceUpdate
from backend.app.schemas.invoice_item import InvoiceItemCreate, InvoiceItemRead, InvoiceItemUpdate
from backend.app.schemas.message import MessageCreate, MessageRead, MessageUpdate
from backend.app.schemas.notification import NotificationCreate, NotificationRead, NotificationUpdate
from backend.app.schemas.parent import ParentCreate, ParentRead, ParentUpdate
from backend.app.schemas.parent_student import ParentStudentCreate, ParentStudentRead, ParentStudentUpdate
from backend.app.schemas.payment import PaymentCreate, PaymentRead, PaymentUpdate
from backend.app.schemas.report import ReportCreate, ReportRead, ReportUpdate
from backend.app.schemas.schedule import ScheduleCreate, ScheduleRead, ScheduleUpdate
from backend.app.schemas.school_year import SchoolYearCreate, SchoolYearRead, SchoolYearUpdate
from backend.app.schemas.student import StudentCreate, StudentRead, StudentUpdate
from backend.app.schemas.subject import SubjectCreate, SubjectRead, SubjectUpdate
from backend.app.schemas.teacher import TeacherCreate, TeacherRead, TeacherUpdate
from backend.app.schemas.teacher_sub import TeacherSubjectCreate, TeacherSubjectRead, TeacherSubjectUpdate
from backend.app.schemas.term import TermCreate, TermRead, TermUpdate
from backend.app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/api/v1", tags=["models"])
db_factory = SessionFactory()

def register_crud_routes(endpoint: str, module_path: str, class_name: str, create_schema: Type[BaseModel], update_schema: Type[BaseModel], read_schema: Type[BaseModel], item_name: str):
    model_module = import_module(module_path)
    model = getattr(model_module, class_name)

    @router.get(f"/{endpoint}", response_model=list[read_schema])
    async def list_items(db: AsyncSession = Depends(db_factory.get_db)):
        result = await db.execute(select(model))
        return result.scalars().all()

    @router.post(f"/{endpoint}", response_model=read_schema, status_code=status.HTTP_201_CREATED)
    async def create_item(payload: create_schema, db: AsyncSession = Depends(db_factory.get_db)):
        obj = model(**payload.model_dump())
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    @router.get(f"/{endpoint}/{{id}}", response_model=read_schema)
    async def read_item(id: int, db: AsyncSession = Depends(db_factory.get_db)):
        result = await db.execute(select(model).where(model.id == id))
        obj = result.scalars().first()
        if obj is None:
            raise HTTPException(status_code=404, detail=f"{item_name} not found")
        return obj

    @router.put(f"/{endpoint}/{{id}}", response_model=read_schema)
    async def update_item(id: int, payload: update_schema, db: AsyncSession = Depends(db_factory.get_db)):
        result = await db.execute(select(model).where(model.id == id))
        obj = result.scalars().first()
        if obj is None:
            raise HTTPException(status_code=404, detail=f"{item_name} not found")
        for name, value in payload.model_dump(exclude_unset=True).items():
            setattr(obj, name, value)
        await db.commit()
        await db.refresh(obj)
        return obj

    @router.delete(f"/{endpoint}/{{id}}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_item(id: int, db: AsyncSession = Depends(db_factory.get_db)):
        result = await db.execute(select(model).where(model.id == id))
        obj = result.scalars().first()
        if obj is None:
            raise HTTPException(status_code=404, detail=f"{item_name} not found")
        await db.delete(obj)
        await db.commit()


register_crud_routes("academic-levels", "backend.app.models.academic_level", "AcademicLevel", AcademicLevelCreate, AcademicLevelUpdate, AcademicLevelRead, "AcademicLevel")
register_crud_routes("attendances", "backend.app.models.attendance", "Attendance", AttendanceCreate, AttendanceUpdate, AttendanceRead, "Attendance")
register_crud_routes("attendance-sessions", "backend.app.models.attendance_session", "AttendanceSession", AttendanceSessionCreate, AttendanceSessionUpdate, AttendanceSessionRead, "AttendanceSession")
register_crud_routes("class-subjects", "backend.app.models.class_sub", "ClasseSubject", ClasseSubjectCreate, ClasseSubjectUpdate, ClasseSubjectRead, "ClasseSubject")
register_crud_routes("classes", "backend.app.models.classe", "Classe", ClasseCreate, ClasseUpdate, ClasseRead, "Classe")
register_crud_routes("documents", "backend.app.models.document", "Document", DocumentCreate, DocumentUpdate, DocumentRead, "Document")
register_crud_routes("enrollments", "backend.app.models.enrollment", "Enrollment", EnrollmentCreate, EnrollmentUpdate, EnrollmentRead, "Enrollment")
register_crud_routes("fees", "backend.app.models.fee", "Fee", FeeCreate, FeeUpdate, FeeRead, "Fee")
register_crud_routes("grades", "backend.app.models.grade", "Grade", GradeCreate, GradeUpdate, GradeRead, "Grade")
register_crud_routes("invoices", "backend.app.models.invoice", "Invoice", InvoiceCreate, InvoiceUpdate, InvoiceRead, "Invoice")
register_crud_routes("invoice-items", "backend.app.models.invoice_item", "InvoiceItem", InvoiceItemCreate, InvoiceItemUpdate, InvoiceItemRead, "InvoiceItem")
register_crud_routes("messages", "backend.app.models.message", "Message", MessageCreate, MessageUpdate, MessageRead, "Message")
register_crud_routes("notifications", "backend.app.models.notification", "Notification", NotificationCreate, NotificationUpdate, NotificationRead, "Notification")
register_crud_routes("parents", "backend.app.models.parent", "Parent", ParentCreate, ParentUpdate, ParentRead, "Parent")
register_crud_routes("parent-students", "backend.app.models.parent_student", "ParentStudent", ParentStudentCreate, ParentStudentUpdate, ParentStudentRead, "ParentStudent")
register_crud_routes("payments", "backend.app.models.payment", "Payment", PaymentCreate, PaymentUpdate, PaymentRead, "Payment")
register_crud_routes("reports", "backend.app.models.report", "Report", ReportCreate, ReportUpdate, ReportRead, "Report")
register_crud_routes("schedules", "backend.app.models.schedule", "Schedule", ScheduleCreate, ScheduleUpdate, ScheduleRead, "Schedule")
register_crud_routes("school-years", "backend.app.models.school_year", "SchoolYear", SchoolYearCreate, SchoolYearUpdate, SchoolYearRead, "SchoolYear")
register_crud_routes("students", "backend.app.models.student", "Student", StudentCreate, StudentUpdate, StudentRead, "Student")
register_crud_routes("subjects", "backend.app.models.subject", "Subject", SubjectCreate, SubjectUpdate, SubjectRead, "Subject")
register_crud_routes("teachers", "backend.app.models.teacher", "Teacher", TeacherCreate, TeacherUpdate, TeacherRead, "Teacher")
register_crud_routes("teacher-subjects", "backend.app.models.teacher_sub", "TeacherSubject", TeacherSubjectCreate, TeacherSubjectUpdate, TeacherSubjectRead, "TeacherSubject")
register_crud_routes("terms", "backend.app.models.term", "Term", TermCreate, TermUpdate, TermRead, "Term")
register_crud_routes("users", "backend.app.models.user", "User", UserCreate, UserUpdate, UserRead, "User")
