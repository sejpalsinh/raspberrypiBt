from signal import pause
from bluedot.btcomm import BluetoothServer
from bluedot.btcomm import BluetoothAdapter
import pexpect
import os
import time
#for scaning nearby bluetooth device
def scan_bluetooth_agents():
    devices = {}
    child = pexpect.spawn('sudo bluetoothctl')
    child.sendline ('scan on')
    time.sleep(10)
    child.sendline ('scan off')
    line = child.readline()
    while b'scan off' not in line:
        if b'Device' in line:            
            line = str(line.replace(b"\r\n", b'')).strip("b'").strip("'")
            address, name = line.split('Device ')[1].split(' ', 1)
            devices[name] = address
        line = child.readline()
    child.sendline ('exit')
    return devices

# trust all the nearby bluetooth device for pairing without permission
def trust_device(address):
    child = pexpect.spawn('sudo bluetoothctl')
    child.sendline ('agent off')
    time.sleep(0.5)
    child.sendline ('pairable on')
    time.sleep(0.5)
    child.sendline ('agent NoInputNoOutput')
    time.sleep(0.5)
    child.sendline ('default-agent')
    time.sleep(0.5)
    child.sendline ('trust ' + address)
    time.sleep(2)
    #child.sendline ('pair ' + address)
    #time.sleep(10)
    child.sendline ('exit')

# call both function for scan and trust for pairing 
def scan_and_trust():
    devices = scan_bluetooth_agents()
    print(devices)
    trust_device(list(devices.values())[0])

a = BluetoothAdapter()
a.discoverable = True
a.pairable = True
a.allow_pairing(timeout=60)

scan_and_trust()
time.sleep(2)
print("Starting")
def data_received(data):
    print(data)

s = BluetoothServer(data_received)
try:
    pause()
except KeyboardInterrupt as e:
    print("cancelled by user")
finally:
    print("stopping")
    s.stop()
print("stopped")