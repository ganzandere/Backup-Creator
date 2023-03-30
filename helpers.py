"""Defines helper functions for the application."""
import string
import win32api


def get_drive_letters():
    """Uses pywin32 to find all drive letters."""
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return [drive_letter.rstrip(':\\') for drive_letter in drives]
