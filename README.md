# students_service
# system design
Спроектировать сервис студентов 

## 1) Что должен делать продукт?

-Учет студентов в школе:
    *список всех студентов 
    *их оценки по всем предметам

## 2) Сущности:
    *Студент
    *Оценка
    *Предмет

## 3) Свойства сущностей:
    -Студент: имя,оценки,класс
    -Оценка: предмет,значение,студент
    -Предмет: название,класс

## 4) Поведение сервиса
    1.Создавать студентов
    2.Получение оценки
    3.Создавать оценки 
    4.Создавать предметы

## 5) API ручки
    1.POST/students
    2.GET/grades/{students_id}
    3.POST/grades/{students_id}/{subject_name}
    4.POST/subject

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

[Link for System Design](https://miro.com/app/board/uXjVHLv8O5A=/?share_link_id=399988145303)