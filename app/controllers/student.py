from fastapi import HTTPException,APIRouter
from pydantic import BaseModel
from app.view.student import Student
from app.model import student as student_model

router = APIRouter(prefix="/students")

class Student_py(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    courses: list[str] | None = None

def find_student_contrl(student_id: int):
    student = student_model.find_student(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.patch("/{id}", response_model=Student, response_model_exclude_unset=True)
def update_student_contrl(id: int, body: Student_py):
    student = find_student_contrl(id)
    if body.first_name is not None:
        student["first_name"] = body.first_name
    if body.last_name is not None:
        student["last_name"] = body.last_name
    if body.age is not None:
        student["age"] = body.age
    if body.courses is not None:
        student["courses"] = body.courses
    return student

@router.post("", response_model=Student)
def create_student_contrl(student: Student_py):
    return student_model.create_student(student)

@router.get("/{id}", response_model=Student)
def get_student_contrl(id: int):
    return find_student_contrl(id)

@router.get("", response_model=list[Student])
def get_all_students_contrl():
    return student_model.get_all_students()

@router.delete("/{id}", status_code=204)
def delete_student_contrl(id: int):
    find_student_contrl(id)
    student_model.delete_student(id)
