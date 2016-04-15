import serial
import time


class DartboardBase:
    line = 'not initialized yet'
    dateline = 'not initialized yet'
    msg = 'not initialized yet'
    do_log = 1
    log = []
    verbose = 1

    def __init__(self):
        pass

    def query_line(self):
        pass

    def update_msg(self):
        x = self.query_line()
        self.line = x
        self.dateline = x[:-1] + 'Time:' + str(time.time()) + '#'
        if self.do_log:
            self.log.append(self.dateline)
        if self.verbose:
            print self.dateline
        self.msg = self.parse_line(x)
        return self.msg

    def parse_line(self, x):
        tmp = self.dateline.replace(':', '#').replace('@', '#').split('#')
        msg = {}
        for i in [1, 3, 5, 7, 9, 11, 13, 15, 17]:
            msg[tmp[i]] = tmp[i+1]
        try:
            msg['Players'] = int(msg['Players'])
            msg['Time'] = float(msg['Time'])
        except:
            pass
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
        #self.ser.write('A')
        x = self.ser.readline()
        
        while (x == '') or (x == self.line):
            x = self.ser.readline()
            success = False
            while not success:
                y = self.ser.readline()
                while (y == ''):
                    y = self.ser.readline()
                if y in x:
                    success = True
                    x = y
                else:
                    x = y
                    
            
        return x


class PseudoDartboard(DartboardBase):
    def __init__(self, filename):
        DartboardBase.__init__(self)
        self.f = open(filename)

    def query_line(self):
        x = self.f.readline()[:-1]
        while (x == '') or (x == self.line):
            x = self.f.readline()[:-1]
        return x
