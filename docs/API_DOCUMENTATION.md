# API Documentation

## Base URL
```
http://localhost:5000/api
```

## Content-Type
All requests should include:
```
Content-Type: application/json
```

---

## Faculty Endpoints

### List All Faculty
```
GET /faculty
```

**Query Parameters:**
- `page` (optional): Page number for pagination (default: 1)
- `search` (optional): Search term to filter by name or faculty_id

**Response:**
```json
{
  "data": [
    {
      "id": 1,
      "name": "Dr. John Smith",
      "faculty_id": "FAC001",
      "email": "john.smith@university.edu",
      "department": "Computer Science",
      "position": "Assistant Professor",
      "phone": "555-0123",
      "created_at": "2024-01-15T10:30:00",
      "updated_at": "2024-01-15T10:30:00"
    }
  ],
  "total": 1,
  "pages": 1
}
```

### Get Faculty by ID
```
GET /faculty/{id}
```

**Path Parameters:**
- `id`: Faculty ID

**Response:**
```json
{
  "id": 1,
  "name": "Dr. John Smith",
  "faculty_id": "FAC001",
  "email": "john.smith@university.edu",
  "department": "Computer Science",
  "position": "Assistant Professor",
  "phone": "555-0123",
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00"
}
```

### Create New Faculty
```
POST /faculty
```

**Request Body:**
```json
{
  "name": "Dr. Jane Doe",
  "faculty_id": "FAC002",
  "email": "jane.doe@university.edu",
  "department": "Mathematics",
  "position": "Associate Professor",
  "phone": "555-0456"
}
```

**Response:** Created faculty object (201 Created)

### Update Faculty
```
PUT /faculty/{id}
```

**Request Body:** (all fields optional)
```json
{
  "name": "Dr. Jane Doe",
  "email": "jane.doe.updated@university.edu",
  "department": "Applied Mathematics",
  "position": "Full Professor"
}
```

**Response:** Updated faculty object (200 OK)

### Delete Faculty
```
DELETE /faculty/{id}
```

**Response:**
```json
{
  "message": "Faculty deleted successfully"
}
```

---

## Student Endpoints

### List All Students
```
GET /student
```

**Query Parameters:**
- `page` (optional): Page number
- `search` (optional): Search by name or student_id

**Response:**
```json
{
  "data": [
    {
      "id": 1,
      "name": "Maria Garcia",
      "student_id": "STU001",
      "email": "maria.garcia@student.university.edu",
      "program": "BS Computer Science",
      "year_level": "3rd Year",
      "phone": "555-1234",
      "status": "Active",
      "created_at": "2024-01-20T14:00:00",
      "updated_at": "2024-01-20T14:00:00"
    }
  ],
  "total": 1,
  "pages": 1
}
```

### Get Student by ID
```
GET /student/{id}
```

### Create New Student
```
POST /student
```

**Request Body:**
```json
{
  "name": "Carlos Santos",
  "student_id": "STU002",
  "email": "carlos.santos@student.university.edu",
  "program": "BS Engineering",
  "year_level": "2nd Year",
  "phone": "555-2345",
  "status": "Active"
}
```

**Valid Status Values:** Active, Inactive, Graduated

### Update Student
```
PUT /student/{id}
```

### Delete Student
```
DELETE /student/{id}
```

---

## Research Personnel Endpoints

### List All Research Personnel
```
GET /research-personnel
```

**Query Parameters:**
- `search` (optional): Search by name or personnel_id

### Get Research Personnel by ID
```
GET /research-personnel/{id}
```

### Create Research Personnel
```
POST /research-personnel
```

**Request Body:**
```json
{
  "name": "Dr. Robert Chen",
  "personnel_id": "RES001",
  "email": "robert.chen@university.edu",
  "specialization": "Artificial Intelligence",
  "position": "Senior Researcher",
  "phone": "555-3456"
}
```

### Update Research Personnel
```
PUT /research-personnel/{id}
```

### Delete Research Personnel
```
DELETE /research-personnel/{id}
```

---

## Scholarship Endpoints

### List All Scholarships
```
GET /scholarship
```

**Query Parameters:**
- `student_id` (optional): Filter by student

### Get Scholarship by ID
```
GET /scholarship/{id}
```

### Create Scholarship
```
POST /scholarship
```

**Request Body:**
```json
{
  "student_id": 1,
  "scholarship_name": "Merit Excellence Award",
  "scholarship_type": "Academic Excellence",
  "amount": 5000.00,
  "academic_year": "2023-2024",
  "semester": "1st",
  "start_date": "2023-08-01T00:00:00",
  "end_date": "2023-12-31T00:00:00"
}
```

### Update Scholarship
```
PUT /scholarship/{id}
```

### Delete Scholarship
```
DELETE /scholarship/{id}
```

---

## Student Load Endpoints

### List Student Loads
```
GET /student-load
```

**Query Parameters:**
- `student_id` (optional): Filter by student

### Create Student Load
```
POST /student-load
```

**Request Body:**
```json
{
  "student_id": 1,
  "academic_year": "2023-2024",
  "semester": "1st",
  "total_units": 18,
  "courses_enrolled": 6,
  "gpa": 3.75,
  "status": "Good Standing"
}
```

### Update Student Load
```
PUT /student-load/{id}
```

### Delete Student Load
```
DELETE /student-load/{id}
```

---

## Faculty Load Endpoints

### List Faculty Loads
```
GET /faculty-load
```

**Query Parameters:**
- `faculty_id` (optional): Filter by faculty

### Create Faculty Load
```
POST /faculty-load
```

**Request Body:**
```json
{
  "faculty_id": 1,
  "academic_year": "2023-2024",
  "semester": "1st",
  "courses_taught": 4,
  "total_units": 12,
  "students_taught": 120,
  "research_hours": 10,
  "extension_hours": 5
}
```

### Update Faculty Load
```
PUT /faculty-load/{id}
```

### Delete Faculty Load
```
DELETE /faculty-load/{id}
```

---

## Publication Endpoints

### List Publications
```
GET /publication
```

**Query Parameters:**
- `personnel_id` (optional): Filter by research personnel

### Create Publication
```
POST /publication
```

**Request Body:**
```json
{
  "personnel_id": 1,
  "title": "Advanced Machine Learning Techniques",
  "publication_type": "Journal Article",
  "publication_date": "2024-01-15T00:00:00",
  "journal_name": "International Journal of AI Research",
  "volume": "45",
  "pages": "123-145",
  "url": "https://example.com/article"
}
```

### Update Publication
```
PUT /publication/{id}
```

### Delete Publication
```
DELETE /publication/{id}
```

---

## Reports Endpoints

### Generate Faculty Report
```
GET /reports/faculty
```

**Query Parameters:**
- `format`: pdf or excel (required)

**Example:**
```
GET /reports/faculty?format=pdf
GET /reports/faculty?format=excel
```

### Generate Student Report
```
GET /reports/student?format=pdf|excel
```

### Generate Enrollment Report
```
GET /reports/enrollment?format=pdf|excel
```

### Generate Scholarships Report
```
GET /reports/scholarships?format=pdf|excel
```

### Generate Research & Extension Report
```
GET /reports/research-extension?format=pdf|excel
```

**Response:** Binary file (PDF or Excel) for download

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Description of what went wrong"
}
```

### 404 Not Found
```json
{
  "error": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error message"
}
```

---

## Health Check

### System Health
```
GET /api/health
```

**Response:**
```json
{
  "status": "healthy"
}
```

---

## Data Validation Rules

### Faculty
- **name**: Required, string
- **faculty_id**: Required, unique string
- **email**: Required, unique email format
- **department**: Optional, string
- **position**: Optional, string
- **phone**: Optional, string

### Student
- **name**: Required, string
- **student_id**: Required, unique string
- **email**: Required, unique email format
- **program**: Optional, string
- **year_level**: Optional, string
- **status**: Optional, must be (Active, Inactive, Graduated)
- **phone**: Optional, string

### Scholarship
- **student_id**: Required, must reference existing student
- **scholarship_name**: Required, string
- **scholarship_type**: Optional, string
- **amount**: Optional, decimal (max 2 decimal places)
- **academic_year**: Optional, string (format: YYYY-YYYY)
- **semester**: Optional, string

### Research Personnel
- **name**: Required, string
- **personnel_id**: Required, unique string
- **email**: Required, unique email format
- **specialization**: Optional, string
- **position**: Optional, string
- **phone**: Optional, string

---

## Usage Examples

### Using cURL

**Create Faculty:**
```bash
curl -X POST http://localhost:5000/api/faculty \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dr. John Smith",
    "faculty_id": "FAC001",
    "email": "john@university.edu",
    "department": "CS",
    "position": "Professor"
  }'
```

**Get All Faculty:**
```bash
curl http://localhost:5000/api/faculty
```

**Search Faculty:**
```bash
curl http://localhost:5000/api/faculty?search=Smith
```

**Update Faculty:**
```bash
curl -X PUT http://localhost:5000/api/faculty/1 \
  -H "Content-Type: application/json" \
  -d '{
    "position": "Associate Professor"
  }'
```

**Delete Faculty:**
```bash
curl -X DELETE http://localhost:5000/api/faculty/1
```

**Generate Report:**
```bash
curl http://localhost:5000/api/reports/faculty?format=pdf \
  --output faculty_report.pdf
```

### Using JavaScript Fetch API

**Create Student:**
```javascript
fetch('http://localhost:5000/api/student', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'Maria Garcia',
    student_id: 'STU001',
    email: 'maria@student.edu',
    program: 'BS Computer Science',
    status: 'Active'
  })
})
.then(response => response.json())
.then(data => console.log('Success:', data))
.catch(error => console.error('Error:', error));
```

**Get Faculty:**
```javascript
fetch('http://localhost:5000/api/faculty')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## Pagination

All list endpoints support pagination:

```
GET /faculty?page=2
```

**Response includes:**
- `data`: Array of records
- `total`: Total number of records
- `pages`: Total number of pages

---

## Rate Limiting

Currently not implemented. For production, implement rate limiting to prevent abuse.

---

## Version

**Current API Version:** 1.0

---

## Support

For API issues or questions, refer to the main README.md or check the Flask application logs.
