#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Send e-mail with module smtplib
# v0.10
# Simone Dellabora

import smtplib

def sendMail():

  local_hostname = 'localhost'

  smtpObject = smtplib.SMTP(local_hostname)

  sender = 'root@vostramail.it'
  receivers = 'destination@destination.it'
  message = """From: CHECK-MACHINE <root>
  To: Name Surname <name.surname@destination.it>
  Subject: ALLERT PING DEVICE

  This is a test e-mail message DEVICE DOWN !.
  """

  try:
    smtpObject
    smtpObject.sendmail(sender, receivers, message)
  except SMTPException:
    print ('Error: Unsable to send email')
