import serial


class DartboardBase(object):
    line = 'not initialized yet'
    do_log = 1
    log = []
    verbose = 1

    def __init__(self):
        pass

    def get_line(self):
        pass


class Dartboard(DartboardBase):
    def __init__(self):
        DartboardBase.__init__(self)

        self.ser = serial.Serial(
            port='/dev/ttyACM0',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0
            )
        
    def get_line(self):
        self.ser.write('A')
        x = self.ser.readline()
        while (x == '\n') or (x == self.line):
            x = self.ser.readline()

        self.line = x
        if self.do_log:
            self.log.append(x)

        if self.verbose:
            print x

        return x


class PseudoDartboard(DartboardBase):
    def __init__(self, filename):
        DartboardBase.__init__(self)

        self.f = open(filename)

    def get_line(self):

        x = self.f.readline()
        while (x == '\n') or (x == self.line):
            x = self.f.readline()

        self.line = x
        if self.do_log:
            self.log.append(x)

        if self.verbose:
            print x

        return x
