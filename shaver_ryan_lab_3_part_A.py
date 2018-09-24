#Preparing Variables and data types

#km_convert = miles * 1.6
miles = input("Hey Cousin Mark! How many miles do you want converted to kilometers? ")
miles = int(miles)
if miles < 0:
    print("Error: Mark, don't tell me negative numbers!")
else:
    kilometers = miles * 1.6
    print("Okay, Mark, that is", kilometers, "kilometers!")

    #celsius_convert = (farenheit - 32) * (5/9)
    faren = input("Now, Markie parkie, how many degrees Farenheit should we convert to Celsius? ")
    faren = int(faren)
    if faren > 1000:
        print("Error: Hey, you know that's too hot, Mark!")
    elif faren < 0:
        print("Error: Seriously? Mark, I said positive numbers. Be reasonable!")
    else:
        celsius = (faren - 32) * (5/9)
        print("Great, Mark! So, that is", celsius, "degrees Celsius!")

        #liter_convert = gallons * 3.9
        gallons = input("Now, Markimus, how many gallons shall we convert to liters? ")
        gallons = float(gallons)
        if gallons < 0:
            print("Error: Dude, Mark, stop giving me negative numbers!")
        else:
            liters = gallons * 3.9
            print("Great, so that would be", liters, "liters!")

            #kg_convert = pounds * .45
            pounds = input("Markipoo, tell me how many pounds to convert to kilograms: ")
            pounds = float(pounds)
            if pounds < 0:
                print("Error: You're pushing your luck with these negatives, Markus!")
            else:
                kilograms = pounds * .45
                print("That is", kilograms, "in kilograms, cousin!")

                #cm_convert = inch * 2.54
                inches = input("Finally, how many inches do you want converted to centimeters? ")
                inches = float(inches)
                if inches < 0:
                    print("Error: ...is this some kind of game to you? POSITIVE numbers, Mark!")
                else:
                    centi = inches * 2.54
                    print("Okay, running the numbers...it's", centi, "centimeters!")