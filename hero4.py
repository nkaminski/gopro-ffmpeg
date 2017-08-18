#!/usr/bin/env python3
import requests
import os,time,sys
from time import sleep
import threading
import socket

def video():
    r=requests.get("http://10.5.5.9/gp/gpControl/execute?p1=gpStream&c1=restart")
    print(r.text)
    time.sleep(3.0);
    os.system("ffplay -fflags nobuffer -f:v mpegts -probesize 8192 udp://:8554")

def keepalive():

        def get_command_msg(id):
            return "_GPHD_:%u:%u:%d:%1lf\n" % (0, 0, 2, 0)

        UDP_IP = "10.5.5.9"
        UDP_PORT = 8554
        KEEP_ALIVE_PERIOD = 250
        KEEP_ALIVE_CMD = 2
        MESSAGE = get_command_msg(KEEP_ALIVE_CMD)

        print("UDP target IP:", UDP_IP)
        print("UDP target port:", UDP_PORT)
        print("message:", MESSAGE)

        if sys.version_info.major >= 3:
          MESSAGE = bytes(MESSAGE, "utf-8")

        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            sleep(KEEP_ALIVE_PERIOD/1000)

exitFlag = 0

class kathread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        keepalive()
        print("Exiting " + self.name)

thread1 = kathread(1, "Thread-1")

# Start new Threads
thread1.start()
video()
print("Exiting Main Thread")
