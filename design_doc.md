# students_service
# system design
Спроектировать сервис студентов 

# Technologies
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Docker
# Problem 
Kinda digital gradebook for students to check their grades

## 1) Что должен делать продукт?

Учет студентов в школе:
    - список всех студентов 
    - их оценки по всем предметам

## 2) Сущности:
    - Студент
    - Oценка
    - Предмет

## 3) Свойства сущностей:
    - Студент: имя,оценки,класс
    - Оценка: предмет,значение,студент
    - Предмет: название,класс

## 4) Поведение сервиса
    1.Создавать студентов
    2.Получение оценки
    3.Создавать оценки 
    4.Создавать предметы
    5.Получать список всех студентов

## 5) API ручки
    1.POST/student
    2.GET/grades/{student_id}/{subject_name}
    3.POST/grades/{student_id}/{subject_name}
    4.POST/subject
    5.GET/students

## 6) Databases
table : Student
|   id  |    name    |   level  |
|:-----:|:----------:|:--------:|
|   1   | Zhangir    |     9    |
|   2   | Neila      |    10    |
|   3   | Batyrzhan  |    11    |
|   4   | Alimzhan   |     9    |

table : Subject
|   id  |    name    |   level  |
|:-----:|:----------:|:--------:|
|   1   |   Math     |     9    |
|   2   |   Math     |    10    |
|   3   |   Math     |    11    |

Table : Grade
|   id  | student_id | subject_id |     date    | value |
|:-----:|:----------:|:----------:|:-----------:|:-----:|
|   1   |      1     |     1      | 2026-09-29  |   5   |
|   2   |      2     |     2      | 2026-09-29  |   5   |
|   3   |      4     |     1      | 2026-09-29  |   5   |

## 7) Architecture

Client → FastAPI → SQLAlchemy → Database

[Link for System Design](https://miro.com/app/board/uXjVHLv8O5A=/?share_link_id=399988145303)