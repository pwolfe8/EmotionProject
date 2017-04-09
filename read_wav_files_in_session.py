# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 22:19:38 2017

@author: pwolfe8

Reads wav files in a sorted session folder (1,2,3,4, or 5) and adds it to 
a big dictionary holding each emotion:
 'Anger',
 'Disgust',
 'Excited',
 'Fear',
 'Frustration',
 'Happiness',
 'Neutral',
 'Other',
 'Sadness',
 'Surprise'
 
and within that entry for the emotion is another dictionary 
holding each file 0...numFiles
 
"""
import os
from scipy.io import wavfile

bigData = {} # currently file name is bigData. choose different name if needed

# maxlen = 0
# sessionNumbers = [1,2,3,4,5] #choose a session number to grab
# for sessionNumber in sessionNumbers:
sessionNumber = 1
sessionName = 'Session' + str(sessionNumber) + '_sorted/'
emotions = os.listdir(sessionName)
for emotion in emotions:        
    wavFiles = os.listdir(sessionName + emotion)
    
    emotionData = {}
    i = 0
    for wavFile in wavFiles: 
        fs, data = wavfile.read(sessionName + emotion + '/' + wavFile)
#        print fs, len(data)
        if(len(data) > maxlen):
            maxlen = len(data)
        emotionData[i]= data
        i += 1
    bigData[emotion] = emotionData

# so now you can grab the emotions like this:
#   bigData.keys()
#
# and grab list of the files inside like this:
#   bigData['Anger'].keys()
#
# have fun because all the sentences are different length...


# print maxlen

