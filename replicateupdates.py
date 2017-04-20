#!/usr/bin/env python

# Copyright (c) 2017, Willer Penton Posada
#
#  version 1.0 
#  created on April 2017
#
#
#-----------------------------------------------------------------------
# This script is for upload files to diferents host, loading the list of host from a file, the list of files to upload from a directory ans using an ftp username, password and port
#
import sys
from ftpUtils import FtpWpp
from workWithioFiles import IOFilesUtils
import os

#This script take a list of host from a file, read a list of files with a specific extension give by parameters, and with a same ftp user and password, 
#it connect to each of the host in the file of host read and upload every of the files read.

#Arguments
#  sys.argv[1] path in where find the files to upload by ftp
#  sys.argv[2] extension of the type of files to upload 
#  sys.argv[3] file with the host to upload the files
#  sys.argv[4] ftp username
#  sys.argv[5] ftp password
#  sys.argv[6] ftp port

#Example of usage :   ./replicateupdates.py /home/feedupdates/current/ *.zip /home/apache/pctoupdate.conf ftp_username ftp_password ftp_port

fioutils = IOFilesUtils(0)  #this is a class to work with files 
list_files_to_upload = fioutils.readFilesFromFolderInToArray( sys.argv[1], sys.argv[2] )
hosts = fioutils.readFileInToArray( sys.argv[3] )

for h in hosts:
	for f in list_files_to_upload:
		print(h + " " + f)
        ftpconn = FtpWpp(h, sys.argv[4], sys.argv[5], sys.argv[6])
        if ftpconn.IsConnected:
            if os.path.exists(f):
                ftpconn.upload_file(f)
            else:
                print('fail upload to ' + h + ' - file not found: ' + f)    
            ftpconn.disconnect_ftp()        
        else:
			    print('--------------------------------fail to connect to ' + h) 


