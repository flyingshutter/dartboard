


class PseudoDartboard(object):
    line = 'not initialized yet'
    do_log = 1
    log = []
    verbose = 1

    def __init__(self, filename):
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
