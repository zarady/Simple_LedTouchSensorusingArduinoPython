# Arduino-Python LED Control

## Overview
This project demonstrates simple LED control using Arduino and Python. The Arduino code reads input from either a touch sensor or Python commands to toggle an LED.

## Arduino Code
The Arduino code (`led.ino`) is designed to work with a touch sensor and respond to serial communication from Python. It toggles an LED on and off based on touch input or Python commands.

### Components
- Arduino Uno
- Touch sensor (connected to pin 2)
- LED (connected to pin 13)

## Python Code
The Python script (`GUIserial.py`) communicates with the Arduino over a serial connection. It sends commands to turn the LED on or off and receives responses from the Arduino.

### Requirements
- Python 3.x
- pyserial library (`pip install pyserial`)

## Usage
1. Connect the Arduino to the computer.
2. Upload the Arduino code to the board using COM3.
3. Run the Python script to control the LED using COM4.
4. Follow the on-screen instructions to toggle the LED.

## Instructions
- Input 'a' to turn the LED on or off.
- Input 'e' to exit the program.

## Troubleshooting
- If the Arduino port is not found, update the `arduino_port` variable in the Python script.
- Ensure the correct COM port is selected in the Python script (use COM4 if Arduino was uploaded using COM3).
- If encountering permission issues, grant necessary permissions to the COM port.

## Author
Zarady

## License
This project is licensed under the [MIT License](LICENSE).
