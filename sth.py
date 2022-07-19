import serial.tools.list_ports
from app import *


data = []
open_close = "ON"

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portVar = "COM2"

serialInst.baudrate = 9600
serialInst.port = portVar

if(serialInst.isOpen() == False):
    serialInst.open()


if __name__ == '__main__':

    #app.run(debug=True)

    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            number = packet.decode('utf').rstrip('\n\r')
            if number != "#":
                data.append(number)
                print(data)
            else:
                password = data[-3] + data[-2] + data[-1]
                user = find_user_by_password(password)
                print(user.name)
                open_close = open_close_door(user, open_close)




        

