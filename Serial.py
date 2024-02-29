import serial
import glob
import os

'''
# Automatically find the Arduino port on Linux
def find_arduino_port():
    ports = glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')
    return ports[0] if ports else None

find_arduino_port = '/dev/ttyCOM3'

# Replace with your Arduino's serial port (e.g., 'COM3' on Windows or find_arduino_port() on Linux)
arduino_port = find_arduino_port
if arduino_port is None:
    print("Arduino port not found.")
    exit()
'''
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Open a serial connection
ser = serial.Serial(port='COM4', baudrate=9600,timeout=0.1)

# Send data to Arduino

clear_screen()
while True:
    
    data = str(input('''Please enter a key:
                     'a' to On/Off the LED
                     'e' to exit \n\n'''))
    if data == 'a':
        ser.write(bytes('a', 'utf-8'))
        arduino_response = ser.readline().decode('utf-8')
        print("Arduino Response:", arduino_response)
        
    elif data == 'b':
        ser.write(bytes('b', 'utf-8'))
    elif data == "e":
        break
    else:
        print("Invalid Input, Please read instruction properly")

ser.write(data.encode())
ser.write(b'Hello Arduino from Python!\n')


# Close the serial connection
ser.close()
