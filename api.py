import serial


class Arduino(object):

    def __init__(self, name='/dev/ttyACM1', port=9600, timeout=0.1):
        self.name = name
        self.port = port
        self.timeout = timeout
        self.ser = serial.Serial(self.name, self.port, timeout = self.timeout)

    def write(self, msg):
        """writes string to arduino"""
        self.ser.write(bytes(msg, encoding="ascii"))

    def control_digital_pins(self, pinNumber, state):
        """
        control digital pin on arduino
        command = ?/function or case number/pin number/ state level (0, 1) (low, high)
        """
        if state == 'HIGH':
            state_number = 1
        elif state == 'LOW':
            state_number = 0
        else:
            state_number = 0

        command = '1/2/{}/{}/'.format(pinNumber, state_number)
        self.write(msg=command)

        return 'Wrote to digital pin number {} with state {}'.format(pinNumber, state)

