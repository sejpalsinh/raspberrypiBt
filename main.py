import RPi.GPIO as GPIO
from time import sleep
from bluedot.btcomm import BluetoothServer
from signal import pause

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

left_up_pin_no = 12
right_up_pin_no = 16
left_down_pin_no = 20
right_down_pin_no = 21

GPIO.setup(left_up_pin_no, GPIO.OUT)
GPIO.setup(right_up_pin_no, GPIO.OUT)
GPIO.setup(left_down_pin_no, GPIO.OUT)
GPIO.setup(right_down_pin_no, GPIO.OUT)

def alloff():
    GPIO.output(left_up_pin_no, 0)
    GPIO.output(right_up_pin_no, 0)
    GPIO.output(left_down_pin_no, 0)
    GPIO.output(right_down_pin_no, 0)


def go_forword():
    alloff()
    GPIO.output(left_up_pin_no, 1)
    GPIO.output(right_up_pin_no, 1)

def go_backword():
    alloff()
    GPIO.output(left_down_pin_no, 1)
    GPIO.output(right_down_pin_no, 1)

def right_turn():
    alloff()
    GPIO.output(left_up_pin_no, 1)
    GPIO.output(right_down_pin_no, 1)

def left_turn():
    alloff()
    GPIO.output(right_up_pin_no, 1)
    GPIO.output(left_down_pin_no, 1)
    
def data_received(data):
    print(data)

s = BluetoothServer(data_received)
pause()

"""
while True:
    go_forword()
    sleep(2)
    go_backword()
    sleep(2)
    right_turn()
    sleep(2)
    left_turn()
    sleep(2)"""