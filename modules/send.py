# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import logging

# URL https://api.twilio.com/2010-04-01/Accounts/AC6b00ea51558d95aa922c17ad4d966fd1/Messages.json

# Account info
account_sid = "AC6b00ea51558d95aa922c17ad4d966fd1"
auth_token = "0052aff4f3c52903d4f5ed6b811dc7c5"
client = Client(account_sid, auth_token)

def send_sms(phone_num, text_body):

    if isinstance(text_body, tuple):
        if text_body[1] is not None:
            client.messages.create(to=str(phone_num),
                                   from_="+16179413912",
                                   body=str(text_body[0]),
                                   media_url= 'static/images' + text_body[1])
        else: # no URL available
            client.messages.create(to=str(phone_num),
                                   from_="+16179413912",
                                   body=str(text_body[0]))
    else: # when the input message is not a tuple
        client.messages.create(to=str(phone_num),
                               from_="+16179413912",
                               body=str(text_body[0]))
    # log messages sent
    logging.info({'sent_to': phone_num, 'message': text_body[0]})
