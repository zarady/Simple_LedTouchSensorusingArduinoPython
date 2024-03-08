import serial
import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Open a serial connection
ser = serial.Serial(port='COM4', baudrate=9600, timeout=0.1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_data(command):
    ser.write(bytes(command, 'utf-8'))
    arduino_response = ser.readline().decode('utf-8')
    print("Arduino Response:", arduino_response)

def on_button_click(command):
    if command == 'e':
        root.destroy()
    else:
        send_data(command)

def start_program():
    start_button.grid_forget()  # Remove the start button
    button_a.grid(column=0, row=1, pady=10, padx=5)  # Show the toggle LED button
    button_exit.grid(column=1, row=1, pady=10, padx=5)  # Show the exit button

# GUI Setup
root = tk.Tk()
root.title("Arduino Control GUI")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Load and resize the image
original_image = Image.open("image.jpg")
resized_image = original_image.resize((200, 150))  # Adjust the size as needed
photo = ImageTk.PhotoImage(resized_image)
image_label = ttk.Label(frame, image=photo)
image_label.grid(column=0, row=0, pady=10, columnspan=2)  # Span two columns

# Start button to begin the program
start_button = ttk.Button(frame, text="Start Program", command=start_program)
start_button.grid(column=0, row=1, pady=10, columnspan=2)

# Button to send 'a' command (initially hidden)
button_a = ttk.Button(frame, text="Toggle LED", command=lambda: on_button_click('a'))
# button_a.grid(column=0, row=2, pady=10)  # Show it after clicking the start button

# Button to exit the GUI (initially hidden)
button_exit = ttk.Button(frame, text="Exit", command=lambda: on_button_click('e'))
# button_exit.grid(column=1, row=2, pady=10)  # Show it after clicking the start button

root.mainloop()

# Close the serial connection
ser.close()
