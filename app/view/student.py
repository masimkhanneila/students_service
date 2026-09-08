from pydantic import BaseModel, Field


class Student(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    courses: list[str] = Field(default_factory=list)