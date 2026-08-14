from database.db import Database
from repositories.student_repository import StudentRepository


db = Database()

repo = StudentRepository(db)

students = repo.get_all_students()

for student in students:
    print(student.show_info())