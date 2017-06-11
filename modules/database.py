from flask import Flask, request, redirect

from peewee import *
from playhouse.flask_utils import FlaskDB

DATABASE = SqliteDatabase('my_app3.db')

app = Flask(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)

class User(db_wrapper.Model):
    first_name = TextField()
    last_name = TextField()

class Course(db_wrapper.Model):
    title = TextField()
    description = TextField()

class UserCourse(db_wrapper.Model):
    user_id = ForeignKeyField(User, related_name='in-class')
    course_id = ForeignKeyField(Course, related_name='enrolled')
    status = TextField();
    takingQuiz = BooleanField(default = False)
    hasTaken = BooleanField(default = False)

    class Meta:
        primary_key = CompositeKey('user_id', 'course_id')

def setup_database():
    DATABASE.create_tables([User, Course, UserCourse])

    user = User.create(first_name='Robert', last_name='Olsthoorn')
    course = Course.create(title='Testing', description='All fields')
    UserCourse.create(user_id=user.id, course_id=course.id, status=0.0)

query = (User
         .select()
         .join(UserCourse)
         .join(Course)
         .where(Course.title == 'Testing'))

for student in query:
    print student.first_name
