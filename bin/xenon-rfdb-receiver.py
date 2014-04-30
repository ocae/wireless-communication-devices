# -*- coding: utf-8 -*-

import serial
import sys
import time


PORT = sys.argv[1]

ser = serial.Serial(
        port=PORT,
        stopbits=serial.STOPBITS_ONE,
        baudrate=38400,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE)

ser.setRTS(level=True)
time.sleep(1)
ser.setRTS(level=False)
time.sleep(1)

print(ser.write(ord('\0').to_bytes(1, byteorder='little')))

r = ser.read()

if int.from_bytes(r, byteorder='little') != 0x4B:
    print('Bad connection', file=sys.stderr)
    sys.exit(1)

ser.write((0x28).to_bytes(1, byteorder='little'))
ser.write((0x04).to_bytes(1, byteorder='little'))

while True:
    print(ser.read(size=1), end='')
    print()

ser.close()
sys.exit()
