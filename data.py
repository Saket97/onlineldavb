import sys
import os

def load_data(root_dir_cnn, root_dir_dm):
    """ Reads the files and returns a list of stings where each document is represented as a string """
    
    if root_dir_cnn == None:
        print("Please provide root dir for cnn news stories")
        exit(1)
    if root_dir_dm == None:
        print("Please root dir for dailymail news stories")
        exit(1)
    
    filenames_cnn = os.listdir(root_dir_cnn + "/stories/")
    filenames_cnn = [f for f in filenames if os.path.isfile(root_dir_cnn+"/stories/"+f)]
    files = [] # list of documents. each document is represented as a string
    for filename in filenames_cnn:
        with open(root_dir_cnn+"/stories/"+filename) as f:
            tmp = f.read()
            files.append(tmp)
    filenames_dm = os.listdir(root_dir_dm + "/stories/")
    filenames_dm = [f for f in filenames if os.path.isfile(root_dir_dm+"/stories/"+f)]
    for filename in filenames_dm:
        with open(root_dir_dm+"/stories/"+filename) as f:
            tmp = f.read()
            files.append(tmp)
    return files