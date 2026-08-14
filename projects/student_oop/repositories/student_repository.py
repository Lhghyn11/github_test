class StudentRepository:

    def __init__(self, db):
        self.db = db


    def get_all_students(self):

        return self.db.get_students()


    def add_student(self, student):

        return self.db.add_student(student)


    def delete_student(self, student_id):

        return self.db.delete_student(student_id)


    def update_student(self, student_id, score):

        return self.db.update_student(student_id, score)

    