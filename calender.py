""" this is a program for updateing and adding events to your calender"""

from time import sleep, strftime



user_name = "Mike" 

calendar = { 11: "go to dentist"}

def welcome (user):
    print "welcome to your calendar " + user
    print "Your calander is starting....."
    sleep(1)
    print strftime("%A %d, %Y")
    print strftime("%I:%M:%S")
    sleep(1)
    print "What would you like to do?"

def start_calendar ():
    welcome(user_name)
    start = True
    while start == True:
        print "A to Add\nU to Update\nV to View\nD to Delete\nX to Exit"
        user_choise = raw_input(">  ")
        user_choise = user_choise.upper()
        if user_choise == "A":
            dateadd = raw_input("What date would you like to add? >   ")
            reminder = raw_input("What would you like to add on that date?>  ")
            dateadd = int(dateadd)
            calendar[dateadd] = reminder 
            print "Success, that has been added"
        elif user_choise == "V":
            if len(calendar.keys()) < 1:
                print "The Calendar is empty"
            else:
                print calendar
        elif user_choise == "U":
            date = raw_input("What date would you like to update?>  ")
            update = raw_input("what would you like to add to that date?>  ")
            date = int(date)
            del calendar[date]
            calendar[date] = update
            print "Sucess, The " + str(date) + " has been updated!"
        elif user_choise == "D":
            deldate = raw_input("what date would you like to remove?>  ")
            deldate = int(deldate)
            del calendar[deldate]
            print "The " + str(deldate) + " has been deleted."
        elif user_choise == "X":
            break

        else:
            start = False

start_calendar()