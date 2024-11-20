import serial
ser = serial.Serial('COM3', 115200, timeout=1) 
def receive_data():
    if ser.in_waiting > 0:
        data = ser.readline().decode('uft-8').strip()
        return data
    return data
