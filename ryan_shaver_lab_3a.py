#Preparing Variables and data types

#km_convert = miles * 1.6
miles = float(input("Hey Cousin Mark! How many miles do you want converted to kilometers? "))
if miles < 0:
    print("Error: Mark, don't tell me negative numbers!")
else:
    kilometers = miles * 1.6
    print("Okay, Mark, that is", format(kilometers,'.2f'), "kilometers!")

    #celsius_convert = (farenheit - 32) * (5/9)
    faren = float(input("Now, Markie parkie, how many degrees Farenheit should we convert to Celsius? "))
    if faren > 1000:
        print("Error: Hey, you know that's too hot, Mark!")
    elif faren < 0:
        print("Error: Seriously? Mark, I said positive numbers. Be reasonable!")
    else:
        celsius = (faren - 32) * (5/9)
        print("Great, Mark! So, that is", format(celsius,'.2f'), "degrees Celsius!")

        #liter_convert = gallons * 3.9
        gallons = float(input("Now, Markimus, how many gallons shall we convert to liters? "))
        if gallons < 0:
            print("Error: Dude, Mark, stop giving me negative numbers!")
        else:
            liters = gallons * 3.9
            print("Great, so that would be", format(liters,'.2f'), "liters!")

            #kg_convert = pounds * .45
            pounds = float(input("Markipoo, tell me how many pounds to convert to kilograms: "))
            if pounds < 0:
                print("Error: You're pushing your luck with these negatives, Markus!")
            else:
                kilograms = pounds * .45
                print("That is", format(kilograms,'.2f'), "in kilograms, cousin!")

                #cm_convert = inch * 2.54
                inches = float(input("Finally, how many inches do you want converted to centimeters? "))
                if inches < 0:
                    print("Error: ...is this some kind of game to you? POSITIVE numbers, Mark!")
                else:
                    centi = inches * 2.54
                    print("Okay, running the numbers...it's", format(centi,'.2f'), "centimeters!")
