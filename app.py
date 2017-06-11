from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
import datetime
from peewee import *
from playhouse.flask_utils import FlaskDB

import modules

# db_wrapper = FlaskDB(app)
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
def route():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    message = "You sent: " + body + " from " + from_number
    resp.message(message)
    return str(resp)

if __name__ == "__main__":
    app.run()
