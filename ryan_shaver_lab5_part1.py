#Program to convert measurements



#greeting and explanation of program
print("Hey cousin Mark!")
print("Let's convert some measurements together.")



def main():
    #reset while loop interruptor
    limit = 0

    #milestoKm loop
    while limit < 3:
        miles = float(input("How many miles do you want converted to kilometers? "))
        if miles < 0:
            print("Try again with positive numbers.")
            miles = float(input("How many miles do you want converted to kilometers? "))
            limit += 1
        else:
            MilesToKm(miles)
            limit = 3    #break would be simpler, but prof is against Break statements and wants logic to exit
    limit = 0
    
    #FahToCel while loop
    while limit < 3:
        fah = float(input("How many degrees Farenheit should we convert to Celsius? "))
        if fah > 1000:
            print("That's too hot, Mark!")
            limit += 1
        elif fah < 0:
            print("That's too cold, Mark...")
            limit += 1
        else:
            FahToCel(fah)
            limit = 3
    limit = 0
    
    #GalToLit while loop
    while limit < 3:
        gallons = float(input("Now, how many gallons shall we convert to liters? "))
        if gallons < 0:
            print("I will not calculate negative numbers!")
            limit += 1
        else:
            GalToLit(gallons)
            limit = 3
    limit = 0
    
    #PoundsToKg while loop
    while limit < 3:
        pounds = float(input("Mark, what about how many pounds to kilograms? "))
        if pounds < 0:
            print("Not another negative, and I mean it!")
            limit += 1
        else:
            PoundsToKg(pounds)
            limit = 3
    limit = 0
    
    #InchesToCm while loop
    while limit < 3:
        inches = float(input("Finally, how many inches do you want converted to centimeters? "))
        if inches < 0:
            print("...is this some kind of game to you? POSITIVE numbers, Mark!")
            limit += 1
        else:
            InchesToCm(inches)
            limit = 3
    limit = 0
    
#Defining functions that Main passes to
def MilesToKm(milesToKm):
    kilometers = milesToKm * 1.6
    print("Okay, Mark, that is", format(kilometers, '.2f'), "kilometers!")
    
def FahToCel(FahToCel):
    celsius = (FahToCel - 32) * (5/9)
    print("Great! So, that is", format(celsius, '.2f'), "degrees Celsius!")
    
def GalToLit(GalToLit):
    liters = GalToLit * 3.9
    print("Great, so that would be", format(liters,'.2f'), "liters!")
    
def PoundsToKg(PoundsToKg):
    kilograms = PoundsToKg * .45
    print("That is", format(kilograms,'.2f'), "kilograms, cousin!")
    
def InchesToCm(InchesToCm):
    centi = InchesToCm * 2.54
    print("Okay, running the numbers...it's", format(centi, '.2f'), "centimeters!")
    
main()
