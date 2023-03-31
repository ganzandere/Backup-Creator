"""Defines helper functions for the application."""
import os
import shutil

import win32api


def get_drive_letters():
    """Uses pywin32 to find all drive letters."""
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return [drive_letter.rstrip(':\\') for drive_letter in drives]


def file_copier(file, destination, doprefix, prefix, mode):
    """Parses the .txt file, modifies the path with destination argument. If doprefix is True, prefix added after the drive letter. 
    Previews the move if mode is False and actually copies the files if mode is True."""
    root = os.path.dirname(file)
    file = os.path.join(root, file)
    log = []

    if doprefix:
        if prefix != "":
            destination = f"{destination}\\{prefix}\\"

    with open(file) as f:
        for line in f:
            oldfile = os.path.abspath(line).replace('\n', '')
            newfile = f"{destination}{oldfile.split(':')[1]}"
            newfile = os.path.normpath(newfile)
            if mode:
                log.append(f"{oldfile}\n{newfile}\n\n")
                if not os.path.isdir(os.path.dirname(newfile)):
                    os.makedirs(os.path.dirname(newfile))
                shutil.copy2(oldfile, newfile)
            else:
                log.append(f"{oldfile}\n{newfile}\n\n")
    return log
