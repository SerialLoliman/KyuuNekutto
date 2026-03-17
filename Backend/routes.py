from flask import request, jsonify, Blueprint
from models import Faculty, Student, ResearchPersonnel, Scholarship, StudentLoad, FacultyLoad, Publication
from datetime import datetime

def register_routes(app, db):
    
    # ==================== FACULTY ROUTES ====================
    @app.route('/api/faculty', methods=['GET'])
    def get_faculty():
        page = request.args.get('page', 1, type=int)
        search = request.args.get('search', '')
        
        query = Faculty.query
        if search:
            query = query.filter(Faculty.name.ilike(f'%{search}%') | Faculty.faculty_id.ilike(f'%{search}%'))
        
        faculty_list = query.paginate(page=page, per_page=10)
        return jsonify({
            'data': [f.to_dict() for f in faculty_list.items],
            'total': faculty_list.total,
            'pages': faculty_list.pages
        }), 200
    
    @app.route('/api/faculty/<int:faculty_id>', methods=['GET'])
    def get_faculty_by_id(faculty_id):
        faculty = Faculty.query.get_or_404(faculty_id)
        return jsonify(faculty.to_dict()), 200
    
    @app.route('/api/faculty', methods=['POST'])
    def create_faculty():
        try:
            data = request.json
            faculty = Faculty(
                name=data['name'],
                faculty_id=data['faculty_id'],
                department=data.get('department'),
                position=data.get('position'),
                phone=data.get('phone')
            )
            faculty.email = data['email']
            db.session.add(faculty)
            db.session.commit()
            return jsonify(faculty.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/faculty/<int:faculty_id>', methods=['PUT'])
    def update_faculty(faculty_id):
        try:
            faculty = Faculty.query.get_or_404(faculty_id)
            data = request.json
            
            faculty.name = data.get('name', faculty.name)
            if 'email' in data:
                faculty.email = data['email']
            faculty.department = data.get('department', faculty.department)
            faculty.position = data.get('position', faculty.position)
            faculty.phone = data.get('phone', faculty.phone)
            
            db.session.commit()
            return jsonify(faculty.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/faculty/<int:faculty_id>', methods=['DELETE'])
    def delete_faculty(faculty_id):
        try:
            faculty = Faculty.query.get_or_404(faculty_id)
            db.session.delete(faculty)
            db.session.commit()
            return jsonify({'message': 'Faculty deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    # ==================== STUDENT ROUTES ====================
    @app.route('/api/student', methods=['GET'])
    def get_students():
        page = request.args.get('page', 1, type=int)
        search = request.args.get('search', '')
        
        query = Student.query
        if search:
            query = query.filter(Student.name.ilike(f'%{search}%') | Student.student_id.ilike(f'%{search}%'))
        
        students = query.paginate(page=page, per_page=10)
        return jsonify({
            'data': [s.to_dict() for s in students.items],
            'total': students.total,
            'pages': students.pages
        }), 200
    
    @app.route('/api/student/<int:student_id>', methods=['GET'])
    def get_student_by_id(student_id):
        student = Student.query.get_or_404(student_id)
        return jsonify(student.to_dict()), 200
    
    @app.route('/api/student', methods=['POST'])
    def create_student():
        try:
            data = request.json
            student = Student(
                name=data['name'],
                student_id=data['student_id'],
                program=data.get('program'),
                year_level=data.get('year_level'),
                phone=data.get('phone'),
                status=data.get('status', 'Active')
            )
            student.email = data['email']
            db.session.add(student)
            db.session.commit()
            return jsonify(student.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/student/<int:student_id>', methods=['PUT'])
    def update_student(student_id):
        try:
            student = Student.query.get_or_404(student_id)
            data = request.json
            
            student.name = data.get('name', student.name)
            if 'email' in data:
                student.email = data['email']
            student.program = data.get('program', student.program)
            student.year_level = data.get('year_level', student.year_level)
            student.phone = data.get('phone', student.phone)
            student.status = data.get('status', student.status)
            
            db.session.commit()
            return jsonify(student.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/student/<int:student_id>', methods=['DELETE'])
    def delete_student(student_id):
        try:
            student = Student.query.get_or_404(student_id)
            db.session.delete(student)
            db.session.commit()
            return jsonify({'message': 'Student deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    # ==================== RESEARCH PERSONNEL ROUTES ====================
    @app.route('/api/research-personnel', methods=['GET'])
    def get_research_personnel():
        page = request.args.get('page', 1, type=int)
        search = request.args.get('search', '')
        
        query = ResearchPersonnel.query
        if search:
            query = query.filter(ResearchPersonnel.name.ilike(f'%{search}%') | ResearchPersonnel.personnel_id.ilike(f'%{search}%'))
        
        personnel = query.paginate(page=page, per_page=10)
        return jsonify({
            'data': [p.to_dict() for p in personnel.items],
            'total': personnel.total,
            'pages': personnel.pages
        }), 200
    
    @app.route('/api/research-personnel/<int:personnel_id>', methods=['GET'])
    def get_research_personnel_by_id(personnel_id):
        personnel = ResearchPersonnel.query.get_or_404(personnel_id)
        return jsonify(personnel.to_dict()), 200
    
    @app.route('/api/research-personnel', methods=['POST'])
    def create_research_personnel():
        try:
            data = request.json
            personnel = ResearchPersonnel(
                name=data['name'],
                personnel_id=data['personnel_id'],
                specialization=data.get('specialization'),
                position=data.get('position'),
                phone=data.get('phone')
            )
            personnel.email = data['email']
            db.session.add(personnel)
            db.session.commit()
            return jsonify(personnel.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/research-personnel/<int:personnel_id>', methods=['PUT'])
    def update_research_personnel(personnel_id):
        try:
            personnel = ResearchPersonnel.query.get_or_404(personnel_id)
            data = request.json
            
            personnel.name = data.get('name', personnel.name)
            if 'email' in data:
                personnel.email = data['email']
            personnel.specialization = data.get('specialization', personnel.specialization)
            personnel.position = data.get('position', personnel.position)
            personnel.phone = data.get('phone', personnel.phone)
            
            db.session.commit()
            return jsonify(personnel.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/research-personnel/<int:personnel_id>', methods=['DELETE'])
    def delete_research_personnel(personnel_id):
        try:
            personnel = ResearchPersonnel.query.get_or_404(personnel_id)
            db.session.delete(personnel)
            db.session.commit()
            return jsonify({'message': 'Research personnel deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    # ==================== SCHOLARSHIP ROUTES ====================
    @app.route('/api/scholarship', methods=['GET'])
    def get_scholarships():
        page = request.args.get('page', 1, type=int)
        student_id = request.args.get('student_id', type=int)
        
        query = Scholarship.query
        if student_id:
            query = query.filter_by(student_id=student_id)
        
        scholarships = query.paginate(page=page, per_page=10)
        return jsonify({
            'data': [s.to_dict() for s in scholarships.items],
            'total': scholarships.total,
            'pages': scholarships.pages
        }), 200
    
    @app.route('/api/scholarship/<int:scholarship_id>', methods=['GET'])
    def get_scholarship_by_id(scholarship_id):
        scholarship = Scholarship.query.get_or_404(scholarship_id)
        return jsonify(scholarship.to_dict()), 200
    
    @app.route('/api/scholarship', methods=['POST'])
    def create_scholarship():
        try:
            data = request.json
            scholarship = Scholarship(
                student_id=data['student_id'],
                scholarship_name=data['scholarship_name'],
                scholarship_type=data.get('scholarship_type'),
                amount=data.get('amount'),
                academic_year=data.get('academic_year'),
                semester=data.get('semester'),
                start_date=datetime.fromisoformat(data['start_date']) if data.get('start_date') else None,
                end_date=datetime.fromisoformat(data['end_date']) if data.get('end_date') else None
            )
            db.session.add(scholarship)
            db.session.commit()
            return jsonify(scholarship.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/scholarship/<int:scholarship_id>', methods=['PUT'])
    def update_scholarship(scholarship_id):
        try:
            scholarship = Scholarship.query.get_or_404(scholarship_id)
            data = request.json
            
            scholarship.scholarship_name = data.get('scholarship_name', scholarship.scholarship_name)
            scholarship.scholarship_type = data.get('scholarship_type', scholarship.scholarship_type)
            scholarship.amount = data.get('amount', scholarship.amount)
            scholarship.academic_year = data.get('academic_year', scholarship.academic_year)
            scholarship.semester = data.get('semester', scholarship.semester)
            
            db.session.commit()
            return jsonify(scholarship.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/scholarship/<int:scholarship_id>', methods=['DELETE'])
    def delete_scholarship(scholarship_id):
        try:
            scholarship = Scholarship.query.get_or_404(scholarship_id)
            db.session.delete(scholarship)
            db.session.commit()
            return jsonify({'message': 'Scholarship deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    # ==================== STUDENT LOAD ROUTES ====================
    @app.route('/api/student-load', methods=['GET'])
    def get_student_loads():
        student_id = request.args.get('student_id', type=int)
        
        query = StudentLoad.query
        if student_id:
            query = query.filter_by(student_id=student_id)
        
        loads = query.all()
        return jsonify([l.to_dict() for l in loads]), 200
    
    @app.route('/api/student-load', methods=['POST'])
    def create_student_load():
        try:
            data = request.json
            load = StudentLoad(
                student_id=data['student_id'],
                academic_year=data['academic_year'],
                semester=data['semester'],
                total_units=data.get('total_units'),
                courses_enrolled=data.get('courses_enrolled'),
                gpa=data.get('gpa'),
                status=data.get('status')
            )
            db.session.add(load)
            db.session.commit()
            return jsonify(load.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/student-load/<int:load_id>', methods=['PUT'])
    def update_student_load(load_id):
        try:
            load = StudentLoad.query.get_or_404(load_id)
            data = request.json
            
            load.total_units = data.get('total_units', load.total_units)
            load.courses_enrolled = data.get('courses_enrolled', load.courses_enrolled)
            load.gpa = data.get('gpa', load.gpa)
            load.status = data.get('status', load.status)
            
            db.session.commit()
            return jsonify(load.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/student-load/<int:load_id>', methods=['DELETE'])
    def delete_student_load(load_id):
        try:
            load = StudentLoad.query.get_or_404(load_id)
            db.session.delete(load)
            db.session.commit()
            return jsonify({'message': 'Student load deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    # ==================== FACULTY LOAD ROUTES ====================
    @app.route('/api/faculty-load', methods=['GET'])
    def get_faculty_loads():
        faculty_id = request.args.get('faculty_id', type=int)
        
        query = FacultyLoad.query
        if faculty_id:
            query = query.filter_by(faculty_id=faculty_id)
        
        loads = query.all()
        return jsonify([l.to_dict() for l in loads]), 200
    
    @app.route('/api/faculty-load', methods=['POST'])
    def create_faculty_load():
        try:
            data = request.json
            load = FacultyLoad(
                faculty_id=data['faculty_id'],
                academic_year=data['academic_year'],
                semester=data['semester'],
                courses_taught=data.get('courses_taught'),
                total_units=data.get('total_units'),
                students_taught=data.get('students_taught'),
                research_hours=data.get('research_hours'),
                extension_hours=data.get('extension_hours')
            )
            db.session.add(load)
            db.session.commit()
            return jsonify(load.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/faculty-load/<int:load_id>', methods=['PUT'])
    def update_faculty_load(load_id):
        try:
            load = FacultyLoad.query.get_or_404(load_id)
            data = request.json
            
            load.courses_taught = data.get('courses_taught', load.courses_taught)
            load.total_units = data.get('total_units', load.total_units)
            load.students_taught = data.get('students_taught', load.students_taught)
            load.research_hours = data.get('research_hours', load.research_hours)
            load.extension_hours = data.get('extension_hours', load.extension_hours)
            
            db.session.commit()
            return jsonify(load.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/faculty-load/<int:load_id>', methods=['DELETE'])
    def delete_faculty_load(load_id):
        try:
            load = FacultyLoad.query.get_or_404(load_id)
            db.session.delete(load)
            db.session.commit()
            return jsonify({'message': 'Faculty load deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    # ==================== PUBLICATION ROUTES ====================
    @app.route('/api/publication', methods=['GET'])
    def get_publications():
        personnel_id = request.args.get('personnel_id', type=int)
        
        query = Publication.query
        if personnel_id:
            query = query.filter_by(personnel_id=personnel_id)
        
        publications = query.all()
        return jsonify([p.to_dict() for p in publications]), 200
    
    @app.route('/api/publication', methods=['POST'])
    def create_publication():
        try:
            data = request.json
            publication = Publication(
                personnel_id=data['personnel_id'],
                title=data['title'],
                publication_type=data.get('publication_type'),
                publication_date=datetime.fromisoformat(data['publication_date']) if data.get('publication_date') else None,
                journal_name=data.get('journal_name'),
                volume=data.get('volume'),
                pages=data.get('pages'),
                url=data.get('url')
            )
            db.session.add(publication)
            db.session.commit()
            return jsonify(publication.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/publication/<int:publication_id>', methods=['PUT'])
    def update_publication(publication_id):
        try:
            publication = Publication.query.get_or_404(publication_id)
            data = request.json
            
            publication.title = data.get('title', publication.title)
            publication.publication_type = data.get('publication_type', publication.publication_type)
            publication.journal_name = data.get('journal_name', publication.journal_name)
            publication.volume = data.get('volume', publication.volume)
            publication.pages = data.get('pages', publication.pages)
            publication.url = data.get('url', publication.url)
            
            db.session.commit()
            return jsonify(publication.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    @app.route('/api/publication/<int:publication_id>', methods=['DELETE'])
    def delete_publication(publication_id):
        try:
            publication = Publication.query.get_or_404(publication_id)
            db.session.delete(publication)
            db.session.commit()
            return jsonify({'message': 'Publication deleted successfully'}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
