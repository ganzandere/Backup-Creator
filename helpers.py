"""Defines helper functions for the application."""
import os
import shutil
import string

import win32api


def get_drive_letters():
    """Uses pywin32 to find all drive letters."""
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return [drive_letter.rstrip(':\\') for drive_letter in drives]



def file_copier(destination, file, mode, insert, insertext):
    """Copies the files"""
    root = os.path.dirname(file)
    file = os.path.join(root, file)
    log = []

    if insert:
        if insertext != "":
            destination = destination + "\\" + insertext

    with open(file) as f:
        for line in f:
            oldline = os.path.abspath(line).replace('\n','')            
            #newline = os.path.join(destination, oldline.split(':')[1])
            newline = destination + oldline.split(":")[1]

            if mode:
                log.append('copying: \n' + oldline + "\n" + newline + "\n")
                # if not os.path.isdir(os.path.dirname(newline)):
                #     os.makedirs(os.path.dirname(newline))
                # shutil.copy2(oldline, newline)
            else:
                log.append('preview: \n' + oldline + "\n" + newline + "\n")
            #print ('copying: ', oldline)
    return log