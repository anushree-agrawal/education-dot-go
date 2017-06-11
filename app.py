from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

import datetime
from peewee import *
from playhouse.flask_utils import FlaskDB

DATABASE = 'test.db'


app = Flask(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)


# add schemas below
class User(db_wrapper.Model):
    first_name = TextField()
    last_name = TextField()

class Course(db_wrapper.Model):
    title = TextField()
    description = TextField()

class UserCourse(db_wrapper.Model):
    user_id = ForeignKeyField(User, related_name='in-class')
    course_id = ForeignKeyField(Course, related_name='enrolled')
    hasTaken = booleanField(default = false)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    resp = MessagingResponse().message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
