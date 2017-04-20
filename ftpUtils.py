# Copyright (c) 2017, Willer Penton Posada
#
#  version 1.0 
#  created on January 2017
#
#
#-----------------------------------------------------------------------
# This script is a class to make operations with FTP
#
#Member properties
#
#    IsConnected  #true or false if the connection was successful
#
#Functions:
#
#    print_line(self, result)  #print a string in the standard output
#    connect_ftp(self, serverFtp, userFtp, passwordFtp, portFtp)  #connect to a ftp with a host, user and password
#    upload_file(self, upload_file_path)  #upload a file to the host connected
#    disconnect_ftp(self)  #disconnect to the host connected
#
# Use:
#    from ftpUtils import FtpWpp
#
#    f = FtpWpp("myFtpServer", "myFtpUser", "myFtpPassword", "myFtpPort")
#    f.upload_file("./fileToUpload.txt")
#    f.disconnect_ftp()
#
import socket
from ftplib import FTP
import sys

########### TO MODIFY ############

BINARY_STORE = True # if False then line store (not valid for binary files (videos, music, photos...))

###########################################


class FtpWpp(object):


    def __init__(self, serverFtp, userFtp, passwordFtp, portFtp):
        self.IsConnected = self.connect_ftp(serverFtp, userFtp, passwordFtp, portFtp)


    def print_line(self, result):
        print(result)


    def connect_ftp(self, serverFtp, userFtp, passwordFtp, portFtp):
        #Connect to the server
        self.ftpObj = FTP()

        try:
            
            #connecting...
            print('Connecting to ' + serverFtp + '...port...' + portFtp)
            self.ftpObj.connect(serverFtp, portFtp, timeout=2)

            #logging...        
            print('login with ' + userFtp + '...password...' + passwordFtp)
            self.ftpObj.login(userFtp, passwordFtp)

            #logged
            print('logged')
            return True

        except socket.timeout as err:
            print('not logged', err)
            return False

        except socket.error as err:
            print('not logged', err)
            return False

        except:
            print('not logged')
            return False


    def upload_file(self, upload_file_path):
        #Open the file
        if self.IsConnected == False:
            return False
        try:
            upload_file = open(upload_file_path, 'r')
        
            #get the name
            path_split = upload_file_path.split('/')
            final_file_name = path_split[len(path_split)-1]
    
            #transfer the file
            print('Uploading ' + final_file_name + '...')
        
            if BINARY_STORE:
                self.ftpObj.storbinary('STOR '+ final_file_name, upload_file)
            else:
                #self.ftp.storlines('STOR ' + final_file_name, upload_file, print_line)
                self.ftpObj.storlines('STOR '+ final_file_name, upload_file)
            
            print('Upload finished.')
            return True

        except IOError:
            print ("No such file or directory...")
            return False

        except:
            print ("not upload")
            return False


    def disconnect_ftp(self):
        if self.IsConnected == False:
            return False
        self.ftpObj.quit()

