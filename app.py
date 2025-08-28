from chalice import Chalice

app = Chalice(app_name='pycode-api')

@app.route('/')
def index():
    return {'message': 'Hi! This is a sample Python API using Chalice, deployed in AWS Lambda'}

@app.route('/users')
def users():
    return {
        'users': [
            {'id': 1, 'name': 'Alice Johnson', 'age': 29, 'email': 'alice.johnson@example.com', 'position': 'Backend Developer'},
            {'id': 2, 'name': 'Bob Smith', 'age': 32, 'email': 'bob.smith@example.com', 'position': 'Frontend Developer'},
            {'id': 3, 'name': 'Charlie Lee', 'age': 27, 'email': 'charlie.lee@example.com', 'position': 'DevOps Engineer'},
            {'id': 4, 'name': 'Diana Cruz', 'age': 30, 'email': 'diana.cruz@example.com', 'position': 'QA Analyst'},
            {'id': 5, 'name': 'Ethan Brown', 'age': 35, 'email': 'ethan.brown@example.com', 'position': 'Full Stack Developer'},
            {'id': 6, 'name': 'Fiona Green', 'age': 26, 'email': 'fiona.green@example.com', 'position': 'Data Scientist'},
            {'id': 7, 'name': 'George White', 'age': 31, 'email': 'george.white@example.com', 'position': 'Product Manager'},
            {'id': 8, 'name': 'Hannah Black', 'age': 28, 'email': 'hannah.black@example.com', 'position': 'UX Designer'},
            {'id': 9, 'name': 'Ian Clark', 'age': 33, 'email': 'ian.clark@example.com', 'position': 'Mobile Developer'},
            {'id': 10, 'name': 'Julia Adams', 'age': 25, 'email': 'julia.adams@example.com', 'position': 'Cloud Engineer'},
            {'id': 11, 'name': 'Kevin Turner', 'age': 36, 'email': 'kevin.turner@example.com', 'position': 'Tech Lead'},
            {'id': 12, 'name': 'Laura Scott', 'age': 29, 'email': 'laura.scott@example.com', 'position': 'Scrum Master'},
            {'id': 13, 'name': 'Michael Young', 'age': 34, 'email': 'michael.young@example.com', 'position': 'Security Analyst'},
            {'id': 14, 'name': 'Natalie King', 'age': 27, 'email': 'natalie.king@example.com', 'position': 'Business Analyst'},
            {'id': 15, 'name': 'Oscar Reed', 'age': 30, 'email': 'oscar.reed@example.com', 'position': 'Machine Learning Engineer'},
        ]
    }


@app.route('/companies')
def companies():
    return {
        'companies': [
            {'id': 1, 'name': 'Tech Innovators Inc.', 'industry': 'Technology', 'location': 'San Francisco, CA', 'employees': 500},
            {'id': 2, 'name': 'Health Solutions LLC', 'industry': 'Healthcare', 'location': 'New York, NY', 'employees': 300},
            {'id': 3, 'name': 'EcoFriendly Co.', 'industry': 'Environmental Services', 'location': 'Seattle, WA', 'employees': 150},
            {'id': 4, 'name': 'Finance Gurus Ltd.', 'industry': 'Financial Services', 'location': 'Chicago, IL', 'employees': 400},
            {'id': 5, 'name': 'EduTech Partners', 'industry': 'Education Technology', 'location': 'Boston, MA', 'employees': 250},
            {'id': 6, 'name': 'Retail Giants Corp.', 'industry': 'Retail', 'location': 'Los Angeles, CA', 'employees': 600},
            {'id': 7, 'name': 'AutoMakers Inc.', 'industry': 'Automotive', 'location': 'Detroit, MI', 'employees': 350},
            {'id': 8, 'name': 'Foodies United', 'industry': 'Food & Beverage', 'location': 'Austin, TX', 'employees': 200},
            {'id': 9, 'name': 'Travel Experts Ltd.', 'industry': 'Travel & Tourism', 'location': 'Miami, FL', 'employees': 180},
            {'id': 10, 'name': 'MediaWorks LLC', 'industry': 'Media & Entertainment', 'location': 'Atlanta, GA', 'employees': 220},
            {'id': 11, 'name': 'Real Estate Pros', 'industry': 'Real Estate', 'location': 'Denver, CO', 'employees': 130},
            {'id': 12, 'name': 'Logistics Masters Inc.', 'industry': 'Logistics & Supply Chain', 'location': 'Memphis, TN', 'employees': 270},
            {'id': 13, 'name': 'Energy Solutions Co.', 'industry': 'Energy', 'location': 'Houston, TX', 'employees': 320},
            {'id': 14, 'name': 'Consulting Experts Ltd.', 'industry': 'Consulting', 'location': 'Philadelphia, PA', 'employees': 210},
            {'id': 15, 'name': 'NonProfit Heroes', 'industry': "Non-Profit", "location": "Washington, D.C.", "employees": 90},
        ]
    }