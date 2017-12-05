

def rgb_hex():
    invalid_msg = "You have entered an invalid number, please try again"
    red = int(raw_input("what is the value for red? >>   \n"))
    if red < 0 or red > 255:
        print invalid_msg
        return
    green = int(raw_input("what is the value of green? >>   \n"))
    if green <0 or green > 255:
        print invalid_msg
        return    
    blue = int(raw_input("what is the value of blue? >>   \n"))
    if blue < 0 or blue > 255:
        print invalid_msg
        return
    val = hex(red)[2:].zfill(2) + hex(green)[2:].zfill(2) + hex(blue)[2:].zfill(2)
    val = val.upper()
    print "\n************************\n\nThe hex value is %s\n\n************************\n" %val

def hex_rgb():
    invalid_msg = "You have entered an invalid number, please try again"
    hex_val = raw_input("what is the hex value you would like to convert? >>  ")
    if len(hex_val) != 6:
        print invalid_msg
        return
    else:
        hex_valr = hex_val[0:2]
        hex_valg = hex_val[2:4]
        hex_valb = hex_val[4:6]
        r = int(hex_valr,16)
        g = int(hex_valg,16)
        b = int(hex_valb,16)
        print "\n***********************************\n\nThe RGB Value would be (%s, %s, %s)\n\n***********************************\n" %(r, g, b)  


def convert():
    while True:
        option = raw_input("Enter 1 to convert RGB to Hex\nEnter 2 to covert Hex to RGB\nEnter X to Exit\n >>  ")
        if option == "1":
            rgb_hex()
        elif option == "2":
            hex_rgb()
        elif option == "x":
            break
        elif option == "X":
            break 
        else:
            break

convert()