#!/usr/bin/python3


import threading
import time



def standard_thread():
    print("Starting my standard thread")
    time.sleep(20)
    print("Ending my standard thred")

def daemon_thread():
    while True:
        print("Sending out Heartbeat signal")
        time.sleep(2)


if __name__ == "__main__":
    standard_thread = threading.Thread(target = standard_thread)
    
    daemon_thread = threading.Thread(target = daemon_thread)
    daemon_thread.setDaemon(True)
    daemon_thread.start()

    standard_thread.start()


