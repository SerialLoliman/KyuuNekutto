# Quick Start Guide

## 1 Minute Setup

### Start the Application

```bash
# Open Command Prompt or PowerShell
cd c:\Users\taleo\Documents\KyuuNekutto

# Install dependencies (first time only)
pip install -r requirements.txt

# Run the application
cd Backend
python app.py
```

You should see:
```
WARNING in app.run?????: This is a development server. Do not use it in production.
In a full production deployment, you should use a production WSGI server.
* Running on http://127.0.0.1:5000
```

### Access the Application

Open your browser and go to: **http://localhost:5000**

## Main Features Overview

### 1. Dashboard
- View quick statistics
- See total counts for Faculty, Students, and Scholarships
- Check Research Personnel count

### 2. Faculty Management
- Add new faculty members
- Manage faculty information (name, ID, email, department, position)
- Edit existing records
- Delete records
- Search faculty by name or ID

### 3. Student Management
- Add students to the system
- Track academic program, year level, and status
- Edit and delete student records
- Quick search functionality

### 4. Research Personnel
- Manage research and extension personnel
- Track specializations and positions
- Edit and manage records

### 5. Scholarships
- Assign scholarships to students
- Track scholarship amounts and academic years
- Manage scholarship types

### 6. Reports
Five types of reports available:

#### Faculty Report
- Lists all faculty members
- Includes department and position information
- Export as PDF or Excel

#### Student Report
- Shows all student information
- Includes enrollment status
- Available in PDF or Excel format

#### Enrollment Report
- Student academic load details
- Units enrolled, GPA, course count
- Format: PDF or Excel

#### Scholarships Report
- All scholarship awards
- Student information and scholarship amounts
- Formats: PDF or Excel

#### Research & Extension Report
- Research personnel details
- Publications and research outputs
- Multiple sheets in Excel
- PDF with formatted tables

## Data Entry Tips

### Adding Faculty
1. Click "Faculty" → "Add Faculty"
2. **Name**: Full name of faculty member
3. **Faculty ID**: Unique identifier (e.g., FAC001)
4. **Email**: Valid email address
5. **Department**: Department name
6. **Position**: Title/rank
7. Click "Save"

### Adding Students
1. Click "Students" → "Add Student"
2. **Name**: Full student name
3. **Student ID**: Unique ID (e.g., STU001)
4. **Email**: Valid email
5. **Program**: Degree program (e.g., BS Computer Science)
6. **Year Level**: 1st Year, 2nd Year, etc.
7. **Status**: Active, Inactive, or Graduated
8. Click "Save"

### Adding Scholarships
1. Click "Scholarships" → "Add Scholarship"
2. **Student**: Select from dropdown
3. **Scholarship Name**: Name of scholarship
4. **Type**: Scholarship category
5. **Amount**: Dollar amount
6. **Academic Year**: Year awarded (e.g., 2023-2024)
7. **Semester**: 1st Semester or 2nd Semester
8. Click "Save"

## Searching

### Quick Search
- Click on any section (Faculty, Students, Research Personnel)
- Use the search box at the top
- Type a name or ID
- Results update automatically

## Generating Reports

### Step-by-Step
1. Click "Reports" in navigation
2. Choose a report type (Faculty, Student, etc.)
3. Click "PDF" for PDF format or "Excel" for spreadsheet
4. Report downloads automatically to your Downloads folder

### Report Formats

**PDF Reports**
- Professional formatting
- Print-friendly
- Tables with headers
- Perfect for external distribution

**Excel Reports**
- Editable spreadsheet
- Multiple sheets (if applicable)
- Color-coded headers
- Easy data manipulation

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Add Faculty | Click "Faculty" → Click "Add Faculty" |
| Add Student | Click "Students" → Click "Add Student" |
| Delete Record | Click "Delete" button (confirm when prompted) |
| Edit Record | Click "Edit" button on the row |
| Close Form | Click X button in top-right of form |

## Common Tasks

### Change Student Status from Active to Graduated
1. Click "Students"
2. Find the student
3. Click "Edit"
4. Change Status dropdown to "Graduated"
5. Click "Save"

### Update Faculty Information
1. Click "Faculty"
2. Locate the faculty member
3. Click "Edit"
4. Modify fields as needed
5. Click "Save"

### Remove a Scholarship Record
1. Click "Scholarships"
2. Find the scholarship row
3. Click "Delete"
4. Confirm deletion

### Export All Faculty to Excel
1. Click "Reports"
2. Click "Faculty Report" card
3. Click "Excel" button
4. File downloads automatically

## Troubleshooting

### Application Won't Start
**Problem**: "Address already in use"
**Solution**: 
- Another program is using port 5000
- Edit `Backend/app.py` and change port to 5001
- Or restart your computer

### Can't Add Data
**Problem**: "Error saving [item]"
**Solution**:
- Check that email is not duplicate
- Check that ID is not duplicate
- Check that all required fields have data
- Try refreshing the page (F5)

### Reports Not Downloading
**Problem**: Report button did nothing
**Solution**:
- Check browser console for errors (F12)
- Ensure backend is running
- Check firewall settings
- Try a different browser

### Search Not Working
**Problem**: Search returns no results
**Solution**:
- Check spelling
- Search is case-insensitive
- Try searching by ID instead of name

## Data Privacy

The system stores:
- Personal information (names, emails)
- Academic information
- Scholarship details
- Research publications

### Recommendations
- Keep credentials secure
- Don't share access to the application
- For production use, implement user authentication
- Back up data regularly
- Use the system only for intended educational purposes

## Performance Tips

### For Best Performance
1. Keep browser cache cleaned
2. Use Chrome or Firefox
3. Don't open too many browser tabs
4. Close the application properly (Ctrl+C in terminal)
5. Restart the application if it becomes slow

### Data Organization
- Archive old data periodically
- Remove test records before production use
- Keep IDs consistent (e.g., FAC001, STU001)
- Use proper program names for consistency

## Next Steps

After setup:
1. ✅ Start adding faculty members
2. ✅ Add students to the system
3. ✅ Create scholarship records
4. ✅ Generate first report
5. ✅ Explore remaining features

## Need Help?

Check:
1. **README.md** - Comprehensive documentation
2. **Backend/models.py** - Database structure
3. **Frontend/static/js/app.js** - Application code
4. **Browser Console** - Errors (F12 key)

## Keyboard Browser Actions

- **F5**: Refresh page
- **F12**: Open developer tools
- **Ctrl+Shift+Delete**: Clear cache
- **Ctrl+P**: Print/Generate PDF

---

**Ready?** Start the application and begin entering your data!

Questions or issues? Check the README.md for detailed documentation.
