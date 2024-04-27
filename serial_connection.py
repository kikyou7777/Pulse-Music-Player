import serial

def setup_serial(port='COM4', baudrate=115200, timeout = 1):
    return serial.Serial(port = port, baudrate = baudrate, parity = 'N', stopbits= 1, timeout = timeout)

# def read():
#     # Update the port later
#     arduino = serial.Serial(port = 'COM4', baudrate = "115200", timeout =.1)
#
#     #https://projecthub.arduino.cc/ansh2919/serial-communication-between-python-and-arduino-663756
#     #Used this to create serial connection, also asked ChatGPT, and it recommended adding "in_waiting"

def read_bpm(arduino):
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
        print("Raw line read from Arduino:", data)  # Debugging line
        try:
            bpm = int(data)  # Assuming the Arduino is just sending integer BPM values
            #print("Parsed BPM value:", bpm)
            return bpm
        except ValueError:
            #print("Failed to parse BPM values")
            return None
    else:
        print("No data available")
        return None

