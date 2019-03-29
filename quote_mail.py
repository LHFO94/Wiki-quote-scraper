#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
import config

def send_email(message):
    """ This function sends an email, please setup config file first
        program is set-up for gmail atm.
    
    """
    # Change these
    subject = 'Qoute Of The Day'
    try:
        # Connect to gmail-server connection
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        # Login to sever
        s.login(user=config.EMAIL, password=config.PASSWORD)
        # Contains the message
        message = f'Subject: {subject}\n\n{message}'     
        # Send e-mail
        s.sendmail(config.EMAIL, config.TOADDR, message)
        # Close connection
        s.quit()
        return 0
    except Exception as e:
        print (e.message, e.args)
        return 1
    
    