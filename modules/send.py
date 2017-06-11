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
    client.messages.create(to=str(phone_num),
                                             from_="+16179413912",
                                             body=text_body)
    logging.info({'sent_to': phone_num, 'message': text_body})

# def send_mms(phone_num, media):
# 	message = client.api.account.messages.create(to="+12316851234",
#                                              from_="+15555555555",
#                                              body="Hello there!",
#                                              media_url=[
#                                                    'https://demo.twilio.com/owl.png',
#                                                    'https://demo.twilio.com/logo.png'])

# send_sms('+16177101266', 'Parker you bastard!')