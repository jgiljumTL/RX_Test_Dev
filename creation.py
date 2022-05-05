class RX:

    def __init__(self, model, serialnumber, output, BWL, BWH, GC, iteration):
        self.model = model
        self.serialnumber = serialnumber
        self.output = output
        self.BWL = BWL
        self.BWH = BWH
        self.GC = GC
        self.iteration = iteration
#        self.date = date

    def print_contents(self):
        print self.model
        print self.serialnumber
        print self.output
        print self.BWL
        print self.BWH
        print self.GC
        print self.iteration