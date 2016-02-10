#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# Execute ping and when fail advertise with error and send e-mail
# version 0.10
#
# Author: Simone Dellabora
#
# file: pingcheck.py
# Software save configuration cisco.
#
# Python version 3
#

# import module
import sys
import time
import os
import sendmail # my file in directory for send e-mail

# Check Argument
def checkarg():
  if len(sys.argv) != 2:
    print('execute ./pingcheck IP_address')
    sys.exit(1)


# Function banner start program
def banner():
  print ("\n")
  print ("***********************************************")
  print ("*       Execute check ping  -   v0.10         *")
  print ("***********************************************")
  print ("\n")

def ping(address):

  while True:
    time.sleep(10)
    p = os.system('ping ' + address + ' -c 5')

    if p == 0:
      print('UP')
    else:
      print('DOWN'), sendmail.sendMail() # .sendMail() call function in module sendmail (file in directory)

def main():

  checkarg()
# var
  address = sys.argv[1]

# Description start program
  banner()
  ping(address)

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
