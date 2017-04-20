# Copyright (c) 2017, Willer Penton Posada
#
#  version 1.0 
#  created on January 2017
#
#
#-----------------------------------------------------------------------
# This script is a class to make operations with files
#
#Member properties
#
#    
#
#Functions:
#
#    print_line(self, result)  #print a string in the standard output
#    readFilesFromFolderInToArray( self, _pathToRead, _filterFiles )  #read all the name files from a directory (parameter _pathToRead)  and with a filter for the type of the file (*.txt, *.zip, ..) and return a list with all the files names
#    readFileInToArray( self, _fileName )  #read the content of a file (parameter _fileName) and return a list with of content of the file
#    readFileInString( self, _fileName )   #read the content of a file (parameter _fileName)  and return a list with of content of the file
#
# Use:
#    from workWithioFiles.py import IOFilesUtils
#
#    f = IOFilesUtils()
#    f.
#    f.
#
import sys
import glob

###########################################


class IOFilesUtils(object):

    #//////////////////////////////////////////////////
    def __init__(self, _saveLogs):
        self.saveLogs = _saveLogs

    #//////////////////////////////////////////////////
    def print_line(self, result):
        print(result)

    #/////////////////////////////////////////////////
    def readFilesFromFolderInToArray( self, _pathToRead, _filterFiles ):
        
        try:
            
            return glob.glob( _pathToRead + _filterFiles ) #Ex: "/home/adam/*.txt"
           
        except IOError:
            print ("IOError...")

    #/////////////////////////////////////////////////
    def readFileInToArray( self, _fileName ):

        try:
            with open(_fileName) as f:
                content = f.readlines()
            content = [x.strip() for x in content] 
            return content

        except IOError:
            print ("IOError...")
            return []

    #/////////////////////////////////////////
    def readFileInString( self, _fileName ):

        try:
            with open (_fileName, "r") as myfile:
                content=myfile.readlines()
            return content

        except IOError:
            print ("IOError...")
