import time
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please drink water Now!!",
            message = "It will keep you hydrated.",
            app_icon = "D:\Py\Python files\Water Reminder\WaterGlass.ico",
            timeout = 2 
        )
        time.sleep(60*60)


    #Control + C In terminal, use this to exit the program
    #pythonw.exe .\main.py In terminal, it will run in background 
