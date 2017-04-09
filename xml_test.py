# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 20:30:42 2017

@author: pwolf
"""
import os
import glob
#from xml.dom import minidom

label_dir = 'Session1/dialog/EmoEvaluation/Categorical/' # label directory
sentence_dir = 'Session1/sentences/wav/' # directory with sentences of speech

txtfiles = glob.glob(label_dir + '*.txt')


#xmldoc = minidom.parse(xmlfiles[0])
#itemlist = xmldoc.getElementsByTagName('attribute')
#print(len(itemlist))
#print(itemlist[0].attributes['name'].value)
#for s in itemlist:
#    print(s.attributes['name'].value)
    
# open file
f = open(txtfiles[0])
# read line
# example line: "Ses01F_impro01_F000 :Neutral state; ()"
line = f.readline()

# split into emotion and filename
parts = line.split(' ')
emotion = parts[1][1:-1] 
fileName = parts[0]

# get session folder name (only need to do once)
parts = fileName.split('_')
folderName = (parts[0] + parts[1])

while line:
    # split and get emotion and file name
    parts = line.split(' ')
    fileName = parts[0]
    emotion = parts[1][1:-1]
    
    # create emotion folder if hasn't been made, otherwise copy file to that folder
    if()
    
    

    line = f.readline()
f.close()

