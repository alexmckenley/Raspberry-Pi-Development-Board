import serial, time, struct

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, bytesize=8, timeout=0)

while 1:

    foo = struct.pack('B', 8)  # here you are packing the number 1 as a binary.
    port.write(foo)
    time.sleep(.5)
    rcv = port.read(1)
    temp = port.read()
    #lst = list(rcv)
    
    
    rcv = bin(ord(rcv))[2:].rjust(8, '0')
    #rcv is now a string of 8 1's and 0's
    
    
    print rcv[0]
    print rcv[7]
    print "--------------"
    time.sleep(.5)
    #time.sleep(1)
    
    
    
      
 # import struct
#foo = struct.pack('B', 1)  # here you are packing the number 1 as a binary.


