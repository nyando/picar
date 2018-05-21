#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import socket
import sys
import time
import atexit

HOST = '0.0.0.0'
PORT = 8888

FORWARD = 1
BACK    = 2
LEFT    = 3
RIGHT   = 4
CIRCLE  = 5
EXIT    = 6

mh = Adafruit_MotorHAT(addr=0x60)
MOTOR_LEFT = 3
MOTOR_RIGHT = 2
direction = True # True if going forward, False if going backward
speed_left = 0
speed_right = 0

def handle_command(command):
    global direction
    global speed_left
    global speed_right

    if command == FORWARD:
        print('forward...')
        if not direction:
            direction = True
            mh.getMotor(MOTOR_LEFT).run(Adafruit_MotorHAT.FORWARD)
            mh.getMotor(MOTOR_RIGHT).run(Adafruit_MotorHAT.FORWARD)
            speed_left = 25
            speed_right = 25
        elif speed_left + 25 <= 255 and speed_right + 25 <= 255:
            speed_left += 25
            speed_right += 25
        else:
            speed_left = 255
            speed_right = 255
    elif command == BACK:
        print('backward...')
        if direction:
            direction = False
            mh.getMotor(MOTOR_LEFT).run(Adafruit_MotorHAT.BACKWARD)
            mh.getMotor(MOTOR_RIGHT).run(Adafruit_MotorHAT.BACKWARD)
            speed_left = 25
            speed_right = 25
        elif speed_left + 25 <= 255 and speed_right + 25 <= 255:
            speed_left += 25
            speed_right += 25
        else:
            speed_left = 255
            speed_right = 255
    elif command == LEFT:
        print('left...')
        if direction:
            speed_left = 100
            speed_right = 0
        else:
            speed_left = 0
            speed_right = 100
    elif command == RIGHT:
        print('right...')
        if direction:
            speed_left = 0
            speed_right = 100
        else:
            speed_left = 100
            speed_right = 0
    elif command == CIRCLE:
        print('circle...')
        speed_left = 150
        speed_right = 50
    elif command == EXIT:
        sys.exit()

    print(speed_left)
    print(speed_right)
    mh.getMotor(MOTOR_LEFT).setSpeed(speed_left)
    mh.getMotor(MOTOR_RIGHT).setSpeed(speed_right)

def turn_off_motors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turn_off_motors)

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0, None)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed with error code: ' + str(msg))
        sys.exit()
    print('bind complete, waiting for connection')
    s.listen(1)
    conn, addr = s.accept()
    data = conn.recv(4, socket.MSG_WAITALL)
    comm = int.from_bytes(data, byteorder='big')
    print(comm)
    handle_command(comm)
    s.close()
