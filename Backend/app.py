from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
from datetime import datetime
import os
import json
from db import db

# Initialize Flask app
app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kyuu_nekutto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

# Import models and routes after db is initialized with app
from models import Faculty, Student, ResearchPersonnel, Scholarship, StudentLoad, FacultyLoad, Publication
from routes import register_routes
from reports import register_report_routes

# Register blueprints
register_routes(app, db)
register_report_routes(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)
