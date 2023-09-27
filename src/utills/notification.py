"""
This file contains notification related functions

"""
from plyer import notification
import sys
import subprocess


def windowsNotifer(title: str, message: str, name: str, timeout: int):
    notification.notify(
    title=title,
    message=message,
    app_name=name,
    timeout=timeout
    )

def macOS(title: str, message: str):

    applescript = f'display notification "{message}" with title "{title}"'

    subprocess.run(["osascript", "-e", applescript])


def liniux(title: str, message: str, timeout: int):
    
    subprocess.run(["notify-send", "-t", str(timeout), title, message])


def showNotification(title: str='Add title', message: str='Add message', appName: str='Add appname', timeout: int=10):

    if sys.platform.startswith('win'):
        windowsNotifer(title, message, appName, timeout)
    elif sys.platform.startswith('darwin'):
        macOS(title, message)
    elif sys.platform.startswith('linux'):
        liniux(title, message, timeout)
    