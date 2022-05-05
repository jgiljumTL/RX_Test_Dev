import re
# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

units = [] #2d list where all the units information is stored


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    #counter = 0
    filename = "blank" #intitaly sets/defines the filename so the loop can run atleast once

while filename != "": #rune loop IF user input is not BLANK

    filename = raw_input('Enter File Name : ') #asks user for file name input
    unit_settings = re.split('_', filename) #parses each section in the unit name using '_' as the dielimiter
    units.append(unit_settings) #appends the unit settings (parsed file name) into the units list (all of the units)

    if filename != "": # prints values that have been stored in the unit_settings list that was created from the re.split line
        print "You have entered : ", (units)



if filename != "":
    print units[0][1]


with open("RX25AF_U00755_VNA_N_BWL=0,00_BWH=0,00_GC=1,50_00.s2p", 'r') as file:

    contents = file.readline()

    print(contents)
















# See PyCharm help at https://www.jetbrains.com/help/pycharm/
