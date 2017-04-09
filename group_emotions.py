# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:08:58 2017
sorts IEMOCAP emotion speech data into folders per emotion

@author: Philip Wolfe

## list of emotions to extract copies of:
#emot_list = ['angry', 'happy', 'sad', 'neutral',
#             'frustrated', 'excited', 'fearful',
#             'surprised', 'disgusted', 'other']


"""
import os
import glob
import shutil

# sessions
sessions = ['Session2', 'Session3', 'Session4', 'Session5']

for session in sessions:    
    # directory pathways
    label_dir = session + '/dialog/EmoEvaluation/Categorical/' # label directory
    txtfiles = glob.glob(label_dir + '*.txt') # txt files for labels
    sentence_dir = session + '/sentences/wav/' # directory with sentences of speech
    copy_dir = session + '_sorted/' # directory for the extracted sentences
    
    
    # iterate through text files
    for txtfile in txtfiles:
        # open files
        f = open(txtfile)
        # read line
        # example line: "Ses01F_impro01_F000 :Neutral state; ()"
        line = f.readline()
        
        # get filename into txt and then cut off end to get sentence subfolder name
        # do this once per text file
        filename = line.split(' ')[0]
        sentence_subfolder = filename[0:filename.rfind('_')]
        
        while line:
            # split and get emotion and file name
            parts = line.split(' ')
            sentence_fileName = parts[0]
            emotion = parts[1].strip(':;')
    #        print emotion
            
            # try to create directory for emotion if it doesn't exist
            dst = copy_dir + emotion
            try:
                os.makedirs(dst)
            except OSError:
                if not os.path.isdir(dst):
                    raise
                    
            # copy file to new folder
            # Session1\sentences\wav\Ses01F_impro01
            src = sentence_dir + sentence_subfolder +'/'+ sentence_fileName +'.wav'
            shutil.copy(src, dst)
        
            # advance a line in file
            line = f.readline()
        f.close()
    
    
    

