// API Base URL
const API_BASE = 'http://localhost:5000/api';

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Set up navigation
    setupNavigation();
    
    // Load initial data
    loadDashboard();
    loadFacultyTable();
    loadStudentTable();
    loadResearchTable();
    loadScholarshipTable();
    loadStudentSelectOptions();
    
    // Set up search functionality
    document.getElementById('faculty-search').addEventListener('input', function() {
        loadFacultyTable(this.value);
    });
    
    document.getElementById('student-search').addEventListener('input', function() {
        loadStudentTable(this.value);
    });
    
    document.getElementById('research-search').addEventListener('input', function() {
        loadResearchTable(this.value);
    });
});

// Navigation Setup
function setupNavigation() {
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const section = this.getAttribute('data-section');
            showSection(section);
        });
    });
}

// Show/Hide Sections
function showSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.classList.remove('active');
    });
    
    // Show selected section
    const selectedSection = document.getElementById(sectionId);
    if (selectedSection) {
        selectedSection.classList.add('active');
    }
}

// ==================== DASHBOARD ====================
async function loadDashboard() {
    try {
        const facultyRes = await fetch(`${API_BASE}/faculty`);
        const studentRes = await fetch(`${API_BASE}/student`);
        const scholarshipRes = await fetch(`${API_BASE}/scholarship`);
        const researchRes = await fetch(`${API_BASE}/research-personnel`);
        
        const facultyData = await facultyRes.json();
        const studentData = await studentRes.json();
        const scholarshipData = await scholarshipRes.json();
        const researchData = await researchRes.json();
        
        document.getElementById('faculty-count').textContent = facultyData.total || 0;
        document.getElementById('student-count').textContent = studentData.total || 0;
        document.getElementById('scholarship-count').textContent = scholarshipData.total || 0;
        document.getElementById('research-count').textContent = researchData.total || 0;
    } catch (error) {
        console.error('Error loading dashboard:', error);
    }
}

// ==================== FACULTY FUNCTIONS ====================
async function loadFacultyTable(search = '') {
    try {
        const url = search 
            ? `${API_BASE}/faculty?search=${encodeURIComponent(search)}`
            : `${API_BASE}/faculty`;
        
        const response = await fetch(url);
        const data = await response.json();
        const tableBody = document.getElementById('faculty-table');
        tableBody.innerHTML = '';
        
        if (data.data && data.data.length > 0) {
            data.data.forEach(faculty => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${faculty.id}</td>
                    <td>${faculty.name}</td>
                    <td>${faculty.faculty_id}</td>
                    <td>${faculty.email}</td>
                    <td>${faculty.department || '-'}</td>
                    <td>${faculty.position || '-'}</td>
                    <td>
                        <div class="actions">
                            <button class="btn btn-edit" onclick="editFaculty(${faculty.id})">Edit</button>
                            <button class="btn btn-danger" onclick="deleteFaculty(${faculty.id})">Delete</button>
                        </div>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        } else {
            tableBody.innerHTML = '<tr><td colspan="7" style="text-align: center; padding: 20px;">No faculty found</td></tr>';
        }
    } catch (error) {
        console.error('Error loading faculty table:', error);
        showAlert('Error loading faculty data', 'error');
    }
}

function showFacultyForm() {
    document.getElementById('faculty-form').reset();
    document.getElementById('faculty-id').value = '';
    document.getElementById('faculty-modal').classList.add('show');
}

function closeFacultyForm() {
    document.getElementById('faculty-modal').classList.remove('show');
}

async function saveFaculty(event) {
    event.preventDefault();
    
    const id = document.getElementById('faculty-id').value;
    const data = {
        name: document.getElementById('faculty-name').value,
        faculty_id: document.getElementById('faculty-faculty_id').value,
        email: document.getElementById('faculty-email').value,
        department: document.getElementById('faculty-department').value,
        position: document.getElementById('faculty-position').value,
        phone: document.getElementById('faculty-phone').value
    };
    
    try {
        const method = id ? 'PUT' : 'POST';
        const url = id ? `${API_BASE}/faculty/${id}` : `${API_BASE}/faculty`;
        
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            showAlert('Faculty saved successfully', 'success');
            closeFacultyForm();
            loadFacultyTable();
            loadDashboard();
        } else {
            showAlert('Error saving faculty', 'error');
        }
    } catch (error) {
        console.error('Error saving faculty:', error);
        showAlert('Error saving faculty', 'error');
    }
    
    return false;
}

async function editFaculty(id) {
    try {
        const response = await fetch(`${API_BASE}/faculty/${id}`);
        const faculty = await response.json();
        
        document.getElementById('faculty-id').value = faculty.id;
        document.getElementById('faculty-name').value = faculty.name;
        document.getElementById('faculty-faculty_id').value = faculty.faculty_id;
        document.getElementById('faculty-email').value = faculty.email;
        document.getElementById('faculty-department').value = faculty.department || '';
        document.getElementById('faculty-position').value = faculty.position || '';
        document.getElementById('faculty-phone').value = faculty.phone || '';
        
        document.getElementById('faculty-modal').classList.add('show');
    } catch (error) {
        console.error('Error loading faculty:', error);
        showAlert('Error loading faculty', 'error');
    }
}

async function deleteFaculty(id) {
    if (!confirm('Are you sure you want to delete this faculty?')) return;
    
    try {
        const response = await fetch(`${API_BASE}/faculty/${id}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showAlert('Faculty deleted successfully', 'success');
            loadFacultyTable();
            loadDashboard();
        } else {
            showAlert('Error deleting faculty', 'error');
        }
    } catch (error) {
        console.error('Error deleting faculty:', error);
        showAlert('Error deleting faculty', 'error');
    }
}

// ==================== STUDENT FUNCTIONS ====================
async function loadStudentTable(search = '') {
    try {
        const url = search 
            ? `${API_BASE}/student?search=${encodeURIComponent(search)}`
            : `${API_BASE}/student`;
        
        const response = await fetch(url);
        const data = await response.json();
        const tableBody = document.getElementById('student-table');
        tableBody.innerHTML = '';
        
        if (data.data && data.data.length > 0) {
            data.data.forEach(student => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${student.id}</td>
                    <td>${student.name}</td>
                    <td>${student.student_id}</td>
                    <td>${student.email}</td>
                    <td>${student.program || '-'}</td>
                    <td>${student.year_level || '-'}</td>
                    <td>${student.status}</td>
                    <td>
                        <div class="actions">
                            <button class="btn btn-edit" onclick="editStudent(${student.id})">Edit</button>
                            <button class="btn btn-danger" onclick="deleteStudent(${student.id})">Delete</button>
                        </div>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        } else {
            tableBody.innerHTML = '<tr><td colspan="8" style="text-align: center; padding: 20px;">No students found</td></tr>';
        }
    } catch (error) {
        console.error('Error loading student table:', error);
        showAlert('Error loading student data', 'error');
    }
}

function showStudentForm() {
    document.getElementById('student-form').reset();
    document.getElementById('student-id').value = '';
    document.getElementById('student-modal').classList.add('show');
}

function closeStudentForm() {
    document.getElementById('student-modal').classList.remove('show');
}

async function saveStudent(event) {
    event.preventDefault();
    
    const id = document.getElementById('student-id').value;
    const data = {
        name: document.getElementById('student-name').value,
        student_id: document.getElementById('student-student_id').value,
        email: document.getElementById('student-email').value,
        program: document.getElementById('student-program').value,
        year_level: document.getElementById('student-year_level').value,
        phone: document.getElementById('student-phone').value,
        status: document.getElementById('student-status').value
    };
    
    try {
        const method = id ? 'PUT' : 'POST';
        const url = id ? `${API_BASE}/student/${id}` : `${API_BASE}/student`;
        
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            showAlert('Student saved successfully', 'success');
            closeStudentForm();
            loadStudentTable();
            loadStudentSelectOptions();
            loadDashboard();
        } else {
            showAlert('Error saving student', 'error');
        }
    } catch (error) {
        console.error('Error saving student:', error);
        showAlert('Error saving student', 'error');
    }
    
    return false;
}

async function editStudent(id) {
    try {
        const response = await fetch(`${API_BASE}/student/${id}`);
        const student = await response.json();
        
        document.getElementById('student-id').value = student.id;
        document.getElementById('student-name').value = student.name;
        document.getElementById('student-student_id').value = student.student_id;
        document.getElementById('student-email').value = student.email;
        document.getElementById('student-program').value = student.program || '';
        document.getElementById('student-year_level').value = student.year_level || '';
        document.getElementById('student-phone').value = student.phone || '';
        document.getElementById('student-status').value = student.status;
        
        document.getElementById('student-modal').classList.add('show');
    } catch (error) {
        console.error('Error loading student:', error);
        showAlert('Error loading student', 'error');
    }
}

async function deleteStudent(id) {
    if (!confirm('Are you sure you want to delete this student?')) return;
    
    try {
        const response = await fetch(`${API_BASE}/student/${id}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showAlert('Student deleted successfully', 'success');
            loadStudentTable();
            loadStudentSelectOptions();
            loadDashboard();
        } else {
            showAlert('Error deleting student', 'error');
        }
    } catch (error) {
        console.error('Error deleting student:', error);
        showAlert('Error deleting student', 'error');
    }
}

// ==================== RESEARCH PERSONNEL FUNCTIONS ====================
async function loadResearchTable(search = '') {
    try {
        const url = search 
            ? `${API_BASE}/research-personnel?search=${encodeURIComponent(search)}`
            : `${API_BASE}/research-personnel`;
        
        const response = await fetch(url);
        const data = await response.json();
        const tableBody = document.getElementById('research-table');
        tableBody.innerHTML = '';
        
        if (data.data && data.data.length > 0) {
            data.data.forEach(person => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${person.id}</td>
                    <td>${person.name}</td>
                    <td>${person.personnel_id}</td>
                    <td>${person.email}</td>
                    <td>${person.position || '-'}</td>
                    <td>${person.specialization || '-'}</td>
                    <td>
                        <div class="actions">
                            <button class="btn btn-edit" onclick="editResearch(${person.id})">Edit</button>
                            <button class="btn btn-danger" onclick="deleteResearch(${person.id})">Delete</button>
                        </div>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        } else {
            tableBody.innerHTML = '<tr><td colspan="7" style="text-align: center; padding: 20px;">No research personnel found</td></tr>';
        }
    } catch (error) {
        console.error('Error loading research table:', error);
        showAlert('Error loading research data', 'error');
    }
}

function showResearchForm() {
    document.getElementById('research-form').reset();
    document.getElementById('research-id').value = '';
    document.getElementById('research-modal').classList.add('show');
}

function closeResearchForm() {
    document.getElementById('research-modal').classList.remove('show');
}

async function saveResearch(event) {
    event.preventDefault();
    
    const id = document.getElementById('research-id').value;
    const data = {
        name: document.getElementById('research-name').value,
        personnel_id: document.getElementById('research-personnel_id').value,
        email: document.getElementById('research-email').value,
        position: document.getElementById('research-position').value,
        specialization: document.getElementById('research-specialization').value,
        phone: document.getElementById('research-phone').value
    };
    
    try {
        const method = id ? 'PUT' : 'POST';
        const url = id ? `${API_BASE}/research-personnel/${id}` : `${API_BASE}/research-personnel`;
        
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            showAlert('Research personnel saved successfully', 'success');
            closeResearchForm();
            loadResearchTable();
            loadDashboard();
        } else {
            showAlert('Error saving research personnel', 'error');
        }
    } catch (error) {
        console.error('Error saving research personnel:', error);
        showAlert('Error saving research personnel', 'error');
    }
    
    return false;
}

async function editResearch(id) {
    try {
        const response = await fetch(`${API_BASE}/research-personnel/${id}`);
        const person = await response.json();
        
        document.getElementById('research-id').value = person.id;
        document.getElementById('research-name').value = person.name;
        document.getElementById('research-personnel_id').value = person.personnel_id;
        document.getElementById('research-email').value = person.email;
        document.getElementById('research-position').value = person.position || '';
        document.getElementById('research-specialization').value = person.specialization || '';
        document.getElementById('research-phone').value = person.phone || '';
        
        document.getElementById('research-modal').classList.add('show');
    } catch (error) {
        console.error('Error loading research personnel:', error);
        showAlert('Error loading research personnel', 'error');
    }
}

async function deleteResearch(id) {
    if (!confirm('Are you sure you want to delete this research personnel?')) return;
    
    try {
        const response = await fetch(`${API_BASE}/research-personnel/${id}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showAlert('Research personnel deleted successfully', 'success');
            loadResearchTable();
            loadDashboard();
        } else {
            showAlert('Error deleting research personnel', 'error');
        }
    } catch (error) {
        console.error('Error deleting research personnel:', error);
        showAlert('Error deleting research personnel', 'error');
    }
}

// ==================== SCHOLARSHIP FUNCTIONS ====================
async function loadScholarshipTable() {
    try {
        const response = await fetch(`${API_BASE}/scholarship`);
        const data = await response.json();
        const tableBody = document.getElementById('scholarship-table');
        tableBody.innerHTML = '';
        
        if (data.data && data.data.length > 0) {
            data.data.forEach(scholarship => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${scholarship.id}</td>
                    <td>${scholarship.student_id}</td>
                    <td>${scholarship.scholarship_name}</td>
                    <td>${scholarship.scholarship_type || '-'}</td>
                    <td>${scholarship.amount ? '$' + scholarship.amount.toFixed(2) : '-'}</td>
                    <td>${scholarship.academic_year || '-'}</td>
                    <td>
                        <div class="actions">
                            <button class="btn btn-edit" onclick="editScholarship(${scholarship.id})">Edit</button>
                            <button class="btn btn-danger" onclick="deleteScholarship(${scholarship.id})">Delete</button>
                        </div>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        } else {
            tableBody.innerHTML = '<tr><td colspan="7" style="text-align: center; padding: 20px;">No scholarships found</td></tr>';
        }
    } catch (error) {
        console.error('Error loading scholarship table:', error);
        showAlert('Error loading scholarship data', 'error');
    }
}

async function loadStudentSelectOptions() {
    try {
        const response = await fetch(`${API_BASE}/student?page=1`);
        const data = await response.json();
        const select = document.getElementById('scholarship-student_id');
        select.innerHTML = '<option value="">Select Student</option>';
        
        if (data.data && data.data.length > 0) {
            data.data.forEach(student => {
                const option = document.createElement('option');
                option.value = student.id;
                option.textContent = `${student.name} (${student.student_id})`;
                select.appendChild(option);
            });
        }
    } catch (error) {
        console.error('Error loading student options:', error);
    }
}

function showScholarshipForm() {
    document.getElementById('scholarship-form').reset();
    document.getElementById('scholarship-id').value = '';
    document.getElementById('scholarship-modal').classList.add('show');
}

function closeScholarshipForm() {
    document.getElementById('scholarship-modal').classList.remove('show');
}

async function saveScholarship(event) {
    event.preventDefault();
    
    const id = document.getElementById('scholarship-id').value;
    const data = {
        student_id: parseInt(document.getElementById('scholarship-student_id').value),
        scholarship_name: document.getElementById('scholarship-scholarship_name').value,
        scholarship_type: document.getElementById('scholarship-scholarship_type').value,
        amount: parseFloat(document.getElementById('scholarship-amount').value) || null,
        academic_year: document.getElementById('scholarship-academic_year').value,
        semester: document.getElementById('scholarship-semester').value
    };
    
    try {
        const method = id ? 'PUT' : 'POST';
        const url = id ? `${API_BASE}/scholarship/${id}` : `${API_BASE}/scholarship`;
        
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            showAlert('Scholarship saved successfully', 'success');
            closeScholarshipForm();
            loadScholarshipTable();
            loadDashboard();
        } else {
            showAlert('Error saving scholarship', 'error');
        }
    } catch (error) {
        console.error('Error saving scholarship:', error);
        showAlert('Error saving scholarship', 'error');
    }
    
    return false;
}

async function editScholarship(id) {
    try {
        const response = await fetch(`${API_BASE}/scholarship/${id}`);
        const scholarship = await response.json();
        
        document.getElementById('scholarship-id').value = scholarship.id;
        document.getElementById('scholarship-student_id').value = scholarship.student_id;
        document.getElementById('scholarship-scholarship_name').value = scholarship.scholarship_name;
        document.getElementById('scholarship-scholarship_type').value = scholarship.scholarship_type || '';
        document.getElementById('scholarship-amount').value = scholarship.amount || '';
        document.getElementById('scholarship-academic_year').value = scholarship.academic_year || '';
        document.getElementById('scholarship-semester').value = scholarship.semester || '';
        
        document.getElementById('scholarship-modal').classList.add('show');
    } catch (error) {
        console.error('Error loading scholarship:', error);
        showAlert('Error loading scholarship', 'error');
    }
}

async function deleteScholarship(id) {
    if (!confirm('Are you sure you want to delete this scholarship?')) return;
    
    try {
        const response = await fetch(`${API_BASE}/scholarship/${id}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            showAlert('Scholarship deleted successfully', 'success');
            loadScholarshipTable();
            loadDashboard();
        } else {
            showAlert('Error deleting scholarship', 'error');
        }
    } catch (error) {
        console.error('Error deleting scholarship:', error);
        showAlert('Error deleting scholarship', 'error');
    }
}

// ==================== REPORTS ====================
async function generateReport(reportType, format) {
    try {
        const url = `${API_BASE}/reports/${reportType}?format=${format}`;
        const response = await fetch(url);
        
        if (response.ok) {
            const blob = await response.blob();
            const downloadUrl = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = downloadUrl;
            link.download = `${reportType}_report.${format === 'pdf' ? 'pdf' : 'xlsx'}`;
            document.body.appendChild(link);
            link.click();
            link.remove();
            showAlert('Report generated successfully', 'success');
        } else {
            showAlert('Error generating report', 'error');
        }
    } catch (error) {
        console.error('Error generating report:', error);
        showAlert('Error generating report', 'error');
    }
}

// ==================== UTILITY FUNCTIONS ====================
function showAlert(message, type = 'info') {
    // Create alert element
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    
    // Insert at top of main content
    const mainContent = document.querySelector('.main-content');
    mainContent.insertBefore(alert, mainContent.firstChild);
    
    // Remove after 5 seconds
    setTimeout(() => {
        alert.remove();
    }, 5000);
}
