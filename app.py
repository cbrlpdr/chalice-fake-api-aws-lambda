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


