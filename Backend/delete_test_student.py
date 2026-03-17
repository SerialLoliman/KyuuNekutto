from app import app
from db import db
from models import Student

if __name__ == '__main__':
    with app.app_context():
        student = Student.query.first()
        if student:
            db.session.delete(student)
            db.session.commit()
            print('Student deleted.')
        else:
            print('No student found.')
