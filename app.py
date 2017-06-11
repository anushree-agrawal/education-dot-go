from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from modules.status_response import transition

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/", methods=['GET', 'POST'])
def route():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    message = "You sent: " + body + " from " + from_number
    # resp.message(message)
    # send.send_sms(from_number, body)
	transition(from_number, body)
    # return str(resp)
    return 200
    # resp = MessagingResponse()
    # message = "You sent: " + body + " from " + from_number
    # resp.message(message)
    # return str(resp)

if __name__ == "__main__":
    app.run()
