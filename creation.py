import re

RX_list = []

class RX:

    def __init__(self, model, serialnumber, output, BWL, BWH, GC, iteration): #constructor
        self.model = model
        self.serialnumber = serialnumber
        self.output = output
        self.BWL = BWL
        self.BWH = BWH
        self.GC = GC
        self.iteration = iteration
#        self.date = date

    def __repr__(self):
        return "This in an RX object"

    def print_contents(self): #may not be needed?
        print "Model: ", self.model
        print "Serial Number: ", self.serialnumber
        print "Output: ", self.output
        print "Band Width Low: ", self.BWL
        print "Bandwidh High: ", self.BWH
        print "Gain Control: ", self.GC
        print "Test Iteration: ", self.iteration

def show_RX_object(unit):
    print "Printing RX List......................"
    unit.print_contents()

def show_RX_objects():
    print "Printing RX List......................"
    for unit in len(RX_list): #I left off here! Got stuck after because It cannot get the length of RX_list which is needed for printing
        RX_list[unit].print_contents()


def request_file():

    user_file = 0

    while user_file != "":

        user_file = raw_input("Enter File Name : ") #asks for user input

        if user_file == "": #stops script if nothing has been entered
            break

        parsedfile = re.split('_', user_file) #parses name into list
        #sets the list elements equal to variables we can refer to later
        model = parsedfile[0]
        serialnumber = parsedfile[1]
        output = parsedfile[3]
        BWL = parsedfile[4]
        BWH = parsedfile[5]
        GC = parsedfile[6]
        iteration = parsedfile[7]

        A = model + "-" + serialnumber #creates new RX object name

        A = RX(0, 0, 0, 0, 0, 0, 0)  # better way to do this?
        #creates new RX object and sets its agruments values according to the variables we defined ealier
        A.model = model
        A.serialnumber = serialnumber
        A.output = output
        A.BWL = BWL
        A.BWH = BWH
        A.GC = GC
        A.iteration = iteration

        RX_list.append(A) #should add new RX object into the RX list





