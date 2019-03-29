#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script scrapes the WikiQuote of the day and sends in to you in an e-mail.
The current script is set-up for Gmail but can be adjusted easily. In order to 
Run this properly you need to adjust the config file first. 
"""

import quote_scraper 
import quote_mail

try:
    message = quote_scraper.scrape()
    quote_mail.send_email(message)
    print("Success")
except Exception as e:
    print (e.message, e.args)
