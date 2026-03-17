from datetime import datetime
from cryptography.fernet import Fernet
import os
from db import db

# Faculty Model
class Faculty(db.Model):
    __tablename__ = 'faculty'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    faculty_id = db.Column(db.String(50), unique=True, nullable=False)
    _email = db.Column('email', db.LargeBinary, unique=True, nullable=False)

    # Encryption key (should be stored securely in production)
    _fernet_key = os.environ.get('FERNET_KEY') or Fernet.generate_key()
    _fernet = Fernet(_fernet_key)

    @property
    def email(self):
        if self._email:
            return Faculty._fernet.decrypt(self._email).decode()
        return None

    @email.setter
    def email(self, value):
        if value:
            self._email = Faculty._fernet.encrypt(value.encode())
        else:
            self._email = None
    department = db.Column(db.String(255))
    position = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    faculty_loads = db.relationship('FacultyLoad', backref='faculty', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'faculty_id': self.faculty_id,
            'email': self.email,
            'department': self.department,
            'position': self.position,
            'phone': self.phone,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Student Model
class Student(db.Model):
    __tablename__ = 'student'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    student_id = db.Column(db.String(50), unique=True, nullable=False)
    _email = db.Column('email', db.LargeBinary, unique=True, nullable=False)

    @property
    def email(self):
        if self._email:
            return Faculty._fernet.decrypt(self._email).decode()
        return None

    @email.setter
    def email(self, value):
        if value:
            self._email = Faculty._fernet.encrypt(value.encode())
        else:
            self._email = None
    program = db.Column(db.String(255))
    year_level = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    status = db.Column(db.String(50), default='Active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    student_loads = db.relationship('StudentLoad', backref='student', lazy=True, cascade='all, delete-orphan')
    scholarships = db.relationship('Scholarship', backref='student', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'student_id': self.student_id,
            'email': self.email,
            'program': self.program,
            'year_level': self.year_level,
            'phone': self.phone,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Research and Extension Personnel Model
class ResearchPersonnel(db.Model):
    __tablename__ = 'research_personnel'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    personnel_id = db.Column(db.String(50), unique=True, nullable=False)
    _email = db.Column('email', db.LargeBinary, unique=True, nullable=False)

    @property
    def email(self):
        if self._email:
            return Faculty._fernet.decrypt(self._email).decode()
        return None

    @email.setter
    def email(self, value):
        if value:
            self._email = Faculty._fernet.encrypt(value.encode())
        else:
            self._email = None
    specialization = db.Column(db.String(255))
    position = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    publications = db.relationship('Publication', backref='personnel', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'personnel_id': self.personnel_id,
            'email': self.email,
            'specialization': self.specialization,
            'position': self.position,
            'phone': self.phone,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Scholarship Model
class Scholarship(db.Model):
    __tablename__ = 'scholarship'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    scholarship_name = db.Column(db.String(255), nullable=False)
    scholarship_type = db.Column(db.String(100))
    amount = db.Column(db.Float)
    academic_year = db.Column(db.String(50))
    semester = db.Column(db.String(20))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'scholarship_name': self.scholarship_name,
            'scholarship_type': self.scholarship_type,
            'amount': self.amount,
            'academic_year': self.academic_year,
            'semester': self.semester,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Student Academic Load Model
class StudentLoad(db.Model):
    __tablename__ = 'student_load'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    academic_year = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    total_units = db.Column(db.Float)
    courses_enrolled = db.Column(db.Integer)
    gpa = db.Column(db.Float)
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'academic_year': self.academic_year,
            'semester': self.semester,
            'total_units': self.total_units,
            'courses_enrolled': self.courses_enrolled,
            'gpa': self.gpa,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Faculty Academic Load Model
class FacultyLoad(db.Model):
    __tablename__ = 'faculty_load'
    
    id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    academic_year = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(20), nullable=False)
    courses_taught = db.Column(db.Integer)
    total_units = db.Column(db.Float)
    students_taught = db.Column(db.Integer)
    research_hours = db.Column(db.Float)
    extension_hours = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'faculty_id': self.faculty_id,
            'academic_year': self.academic_year,
            'semester': self.semester,
            'courses_taught': self.courses_taught,
            'total_units': self.total_units,
            'students_taught': self.students_taught,
            'research_hours': self.research_hours,
            'extension_hours': self.extension_hours,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Publication Model for Research/Extension
class Publication(db.Model):
    __tablename__ = 'publication'
    
    id = db.Column(db.Integer, primary_key=True)
    personnel_id = db.Column(db.Integer, db.ForeignKey('research_personnel.id'), nullable=False)
    title = db.Column(db.String(500), nullable=False)
    publication_type = db.Column(db.String(100))
    publication_date = db.Column(db.DateTime)
    journal_name = db.Column(db.String(255))
    volume = db.Column(db.String(50))
    pages = db.Column(db.String(50))
    url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'personnel_id': self.personnel_id,
            'title': self.title,
            'publication_type': self.publication_type,
            'publication_date': self.publication_date.isoformat() if self.publication_date else None,
            'journal_name': self.journal_name,
            'volume': self.volume,
            'pages': self.pages,
            'url': self.url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
