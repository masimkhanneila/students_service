from pathlib import Path
from sqlalchemy import(JSON,Column,Integer,MetaData,String,Table,create_engine,select,inspect)

db_path = Path(__file__).resolve().parents[2]/"students.db"
engine = create_engine(f"sqlite:///{db_path}")
metadata = MetaData()
students = Table("students",metadata,
                 Column("id",Integer,primary_key=True),
                 Column("first_name",String,nullable=False),
                 Column("last_name",String,nullable=False),
                 Column("age",Integer,nullable=False),
                 Column("courses",JSON,nullable=True)
                 )
def initialize_db():
    with engine.begin() as connection:
        if inspect(connection).has_table("students"):
            return
        metadata.create_all(connection)
        sample_students = [
            { "id": 1,"first_name": "Ayazhan" , "last_name": "Kyzyr", "age":19,"courses":["chemistry","biology"]},
            { "id": 2,"first_name": "Indira" , "last_name": "Myrzagali", "age":18,"courses":["chemistry","biology"]},
            { "id": 3,"first_name": "Kalamkas" , "last_name": "Iglikova", "age":19,"courses":["management","sociology"]},
            { "id": 4,"first_name": "Alina" , "last_name": "Maimysheva", "age":17,"courses":["algorithms","mathematics"]}
        ]
        connection.execute(students.insert(),sample_students)


def create_student(student):
    query = students.insert().values(
        first_name = student.first_name,
        last_name=student.last_name,
        age=student.age,
        courses=student.courses
        )
    with engine.begin() as connection:
        result = connection.execute(query)
        student_id = result.inserted_primary_key[0]
        return {"id": student_id, "first_name": student.first_name, "last_name": student.last_name,"age" : student.age,"courses":student.courses}
    
def find_student(id: int):
    query = select(students).where(students.c.id == id)
    with engine.connect() as connection:
        # mappings() makes rows accessible by column name; first() may be None.
        row = connection.execute(query).mappings().first()
        if row is None:
            return None
        return dict(row)

def delete_student(id: int):
    query = students.delete().where(students.c.id == id)
    with engine.begin() as connection:
        connection.execute(query)

def get_all_students():
    query = select(students).order_by(students.c.id)
    with engine.connect() as connection:
        rows = connection.execute(query).mappings()
        return [dict(row) for row in rows]

def update_student(id: int,first_name: str = None,last_name: str = None,age: int = None,courses: list[str] = None):
    values = {}
    if first_name is not None:
        values["first_name"] = first_name
    if last_name is not None:
        values["last_name"] = last_name
    if age:
        values["age"] = age
    if courses is not None:
        values["courses"] = courses
    if not values:
        return find_student(id)

    query = (
        students
        .update()
        .where(students.c.id == id)
        .values(**values)
    )

    with engine.begin() as connection:
        connection.execute(query)

    return find_student(id)