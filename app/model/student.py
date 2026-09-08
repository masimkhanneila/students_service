students = {
    1 : { "id": 1,"first_name": "Ayazhan" , "last_name": "Kyzyr", "age":19,"courses":["chemistry","biology"]},
    2 : { "id": 2,"first_name": "Indira" , "last_name": "Myrzagali", "age":18,"courses":["chemistry","biology"]},
    3 : { "id": 3,"first_name": "Kalamkas" , "last_name": "Iglikova", "age":19,"courses":["management","sociology"]},
    4 : { "id": 4,"first_name": "Alina" , "last_name": "Maimysheva", "age":17,"courses":["algorithms","mathematics"]},
}

def create_student(student):
    student_id = max(students.keys(), default=0) + 1
    students[student_id] = {
        "id": student_id,
        "first_name": student.first_name,
        "last_name": student.last_name,
        "age": student.age,
        "courses": student.courses
    }
    return students[student_id]
    
def find_student(id: int):
    return students.get(id)

def delete_student(id: int):
    del students[id]

def get_all_students():
    return list(students.values())

def update_student(id: int,first_name: str = None,last_name: str = None,age: int = None,courses: list[str] = None):
    student = find_student(id)
    if student is None:
        return None
    if first_name is not None:
        student["first_name"] = first_name
    if last_name is not None:
        student["last_name"] = last_name
    if age is not None:
        student["age"] = age
    if courses is not None:
        student["courses"] = courses

    return student