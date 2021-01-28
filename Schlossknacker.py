import smbus 
import time 

address = 0x48
bus = smbus.SMBus(1)
y = 0x48

while True :
    bus.write_byte(address,y)
    value = bus.read_byte(address)
    print(value)
    time.sleep(0.5)