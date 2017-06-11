from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

import datetime
from peewee import *
from playhouse.flask_utils import FlaskDB

DATABASE = ''


app = Flask(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)


# add schemas below
class User(db_wrapper.Model):
    # username = CharField(unique=True)

class Tweet(db_wrapper.Model):
    # user = ForeignKeyField(User, related_name='tweets')
    # content = TextField()
    # timestamp = DateTimeField(default=datetime.datetime.now)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    resp = MessagingResponse().message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)