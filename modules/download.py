#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Atul-Kadian

import requests
import subprocess
import os
import logging
import re
import urllib2
import wget
import os.path
import ssl

def is_downloadable(url):
	h = requests.head(url, allow_redirects=True)
	header = h.headers
	content_type = header.get('content-type')
	if 'text' in content_type.lower():
		return False
	if 'html' in content_type.lower():
		return False
	return True

def download(url, userfile):
    filename='none'
    try:
	ssl._create_default_https_context = ssl._create_unverified_context
	filename = wget.download(url)
        name = re.sub('%20', ' ', filename)
	if userfile:
        	filename = os.rename(filename, userfile)
        	filename = userfile
	else:
		filename = os.rename(filename, name)
        	filename = name
    except Exception as e:
        print("Error! Unable to download file.")
        print(e)
    else:
        print(filename+ ' is successfully downloaded locally ')
        print('Starting Google Drive upload.....')
    return filename
