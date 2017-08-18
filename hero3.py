#!/usr/bin/env python3
import requests
import getpass
import os,time,sys
from time import sleep
import threading

def video():
    os.system("ffplay -fflags nobuffer -f:v hls http://10.5.5.9:8080/live/amba.m3u8")

def keepalive(pwd):

        while True:
            print("refresh...")
            requests.get("http://10.5.5.9/camera/PV?t=%s&p=%%02" % pwd)
            time.sleep(1.0)

exitFlag = 0

class kathread (threading.Thread):
    def __init__(self, threadID, name, pwd):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        keepalive(pwd)
        print("Exiting " + self.name)


pwd = getpass.getpass()
thread1 = kathread(1, "Thread-1", pwd)

# Start new Threads
thread1.start()
time.sleep(3.0);
video()
print("Exiting Main Thread")
