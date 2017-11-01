from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "Calculator is starting up!"
print "%s/%s/%s %s:%s" %(now.month, now.day, now.year, now.hour / 12, now.minute)
sleep(1)

hint = "Don't forget to include the correct units! \nExiting....."

print "Would you like to calculate the area of a Circle or a Triangle type C or T"
option = raw_input (">  ")
option = option.upper()

if (option == "C"):
    print "What is the radius of the circle"
    radius = raw_input (">>  ")
    radius = float(radius)
    area = pi * radius ** 2
    print " The Pie is backing ......"
    sleep(1)
    print ("Area = %.2f \n%s" % (area,hint))

elif (option == "T"): 
    print "what is the base of the triangle?"
    base = raw_input (">> ")
    base = float(base)
    print "what is the height of the triangle"
    height = raw_input (">> ")
    height = float(height)
    area =  height * base / 2
    print "one, two, three!"
    sleep(1)
    print("Area = %.2f \n%s" % (area,hint))
else:
    print "I dont know what that is"

    