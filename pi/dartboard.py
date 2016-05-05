import serial


class DartboardBase(object):
    line = 'not initialized yet'
    do_log = 1
    log = []
    verbose = 1

    def __init__(self):
        pass

    def query_line(self):
        pass

    def get_msg(self):
        x = self.query_line()
        self.line = x
        if self.do_log:
            self.log.append(x)
        if self.verbose:
            print x
        return self.parse_line(x)

    def parse_line(self, x):
        tmp = x.replace(':', '#').replace('@', '#').split('#')
        msg = {}
        for i in [1, 3, 5, 7, 9, 11, 13]:
            msg[tmp[i]] = tmp[i+1]
        msg['Players'] = int(msg['Players'])
        return msg


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
        
    def query_line(self):
        self.ser.write('A')
        x = self.ser.readline()
        while (x == '\n') or (x == self.line):
            x = self.ser.readline()
        return x


class PseudoDartboard(DartboardBase):
    def __init__(self, filename):
        DartboardBase.__init__(self)
        self.f = open(filename)

    def query_line(self):
        x = self.f.readline()
        while (x == '\n') or (x == self.line):
            x = self.f.readline()
        return x
