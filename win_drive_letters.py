import string
import win32api

def get_drive_letters():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return [drive_letter.rstrip(':\\') for drive_letter in drives]

if __name__ == "__main__":
    drive_letters = get_drive_letters()
    print(drive_letters)