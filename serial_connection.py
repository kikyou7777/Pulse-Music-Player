import serial

def setup_serial(port='COM4', baudrate=115200, timeout=0.1):
    return serial.Serial(port, baudrate, timeout)

def read():
    # Update the port later
    arduino = serial.Serial(port = 'COM4', baudrate = "115200", timeout =.1)

    #https://projecthub.arduino.cc/ansh2919/serial-communication-between-python-and-arduino-663756
    #Used this to create serial connection, also asked ChatGPT, and it recommended adding "in_waiting"
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline()
            minBPM = data.split()[0]
            maxBPM = data.split()[1]

            return minBPM, maxBPM

    
