# Copyright (c) 2017, Willer Penton Posada
#
#  version 1.0 
#  created on January 2017
#
#
#-----------------------------------------------------------------------
# This script is a class with some useful things to get
#
#Member properties
#
#    
#
#Functions:
#
#    print_line(self, result)  #print a string in the standard output
#    sendEmail( self, fromEmail, toEmail, _subject, _txtBody, _htmlBody )  #send an email
#    cpu_usage(self)   # to get the cpu usage of the pc
#
#
# Use:
#    from utils.py import ToolsUtils
#
#    u = ToolsUtils()
#    u.
#    u.
#

import sys
import glob
import psutil;
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

########### TO MODIFY ############


###########################################


class ToolsUtils(object):

    #//////////////////////////////////////////////////
    #def __init__(self):
    #    self.

    #//////////////////////////////////////////////////
    def print_line(self, result):
        print(result)

    #/////////////////////////////////////////////////
    def sendEmail( self, fromEmail, toEmail, _subject, _txtBody, _htmlBody ):
        
        try:
            
            me = fromEmail
            you = toEmail

            msg = MIMEMultipart('alternative')
            msg['Subject'] = _subject
            msg['From'] = me
            msg['To'] = you

            text = _txtBody
            html = _htmlBody

            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')

            msg.attach(part1)
            msg.attach(part2)

            s = smtplib.SMTP('localhost')
            s.sendmail(me, you, msg.as_string())
            s.quit()
           
        except:
            print("Unexpected error sendind an email:", sys.exc_info()[0])
            raise
    
    #//////////////////////////////////////////////////////////
    def cpu_usage(self):
		
		try:
			
			return psutil.cpu_percent()
			
        except:
            print("Unexpected error getting the cpu usage of the pc:", sys.exc_info()[0])
            raise			
