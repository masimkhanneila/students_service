from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
students = {
    1 : { "id": 1,"first_name": "Ayazhan" , "last_name": "Kyzyr", "age":19,"courses":["chemistry","biology"]},
    2 : { "id": 2,"first_name": "Indira" , "last_name": "Myrzagali", "age":18,"courses":["chemistry","biology"]},
    3 : { "id": 3,"first_name": "Kalamkas" , "last_name": "Iglikova", "age":19,"courses":["management","sociology"]},
    4 : { "id": 4,"first_name": "Alina" , "last_name": "Maimysheva", "age":17,"courses":["algorithms","mathematics"]},
}

class Student_courses_create(BaseModel):
    first_name : str
    last_name : str
    age : int
    courses: list[str]

@app.post("/students")
def create_student(student: Student_courses_create):
    student_id = len(students) + 1
    students[student_id] = {"id" : student_id, "first_name":student.first_name,"last_name":student.last_name,"age":student.age,"courses":student.courses}
    return students[student_id]

def find_student(id : int):
    student = students.get(id)
    if student is None:
        raise HTTPException(status_code = 404,detail = "Student is not found")
    return student

@app.delete("/students/{id}", status_code=204)
def delete_student(id : int):
    find_student(id)
    del students[id]

@app.get("/students/{id}")
def get_student(id: int):
    return find_student(id)

@app.get("/students")
def get_all_students():
    return list(students.values())

class Student_courses(BaseModel):
    first_name : str | None
    last_name : str | None
    age : int | None
    courses: list[str] | None

@app.patch("/students/{id}")
def update_student(id: int, body: Student_courses):
    student = find_student(id)
    if body.first_name is not None:
        student["first_name"] = body.first_name
    if body.last_name is not None:
        student["last_name"] = body.last_name
    if body.age is not None:
        student["age"] = body.age
    if body.courses is not None:
        student["courses"] = body.courses
    return student



