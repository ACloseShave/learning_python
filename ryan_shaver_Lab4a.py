
######################################
##Preparing Variables and data types##
######################################


print("Hey cousin Mark!")
i = 3

############################
##km_convert = miles * 1.6##
############################


if i > 0:      #included to test if user has entered less than 3 negative entries for the whole program
    while i > 0:
        miles = float(input("How many miles do you want converted to kilometers? "))
        if miles < 0:           #Testing if miles is positive
            print("Try again.")
            i -= 1
        else:                   #Positive number entry
            kilometers = miles * 1.6
            print("Okay, Mark, that is", format(kilometers,'.2f'), "kilometers!")
            break
else:          #included to terminate program after 3 invalid inputs
    exit(0)




##############################################
##celsius_convert = (farenheit - 32) * (5/9)##
##############################################


if i > 0:    
    while i > 0:
        faren = float(input("How many degrees Farenheit should we convert to Celsius? "))
        if faren >= 1000:        #Testing if farenheit is too hot
            print("That's too hot, Mark!")
            i -= 1
        elif faren < 0:         #Testing if farenheit is too cold
            print("That's too cold, Mark...")
            i -= 1
        else:                   #Correct temperature range
            celsius = (faren - 32) * (5/9)
            print("Great! So, that is", format(celsius,'.2f'), "degrees Celsius!")
            break
else:
    exit(0)




#################################
##liter_convert = gallons * 3.9##
#################################

    
if i > 0:
    while i > 0:
        gallons = float(input("Now, how many gallons shall we convert to liters? "))
        if gallons < 0:
            print("I will not calculate negative numbers!")
        else:
            liters = gallons * 3.9
            print("Great, so that would be", format(liters,'.2f'), "liters!")
            break
        i -= 1
else:
    exit(0)




#############################
##kg_convert = pounds * .45##
#############################

    
if i > 0:
    while i > 0:
        pounds = float(input("Mark, what about how many pounds to kilograms? "))
        if pounds < 0:
            print("Not another negative, and I mean it!")
        else:
            kilograms = pounds * .45
            print("That is", format(kilograms,'.2f'), "in kilograms, cousin!")
            break
        i -= 1
else:
    exit(0)




############################
##cm_convert = inch * 2.54##
############################


if i > 0:
    while i > 0:
        inches = float(input("Finally, how many inches do you want converted to centimeters? "))
        if inches < 0:
            print("Error: ...is this some kind of game to you? POSITIVE numbers, Mark!")
        else:
            centi = inches * 2.54
            print("Okay, running the numbers...it's", format(centi,'.2f'), "centimeters!")
            break
        i -= 1
else:
    exit(0)




################
##finishing up##
################


print("Great! That's all I have for you!")
