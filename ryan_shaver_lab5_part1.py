#Program to convert measurements





print("Hey cousin Mark!")
print("Let's convert some measurements together.")


def main():
    milesToKm = float(input("How many miles do you want converted to kilometers? "))
    print("Okay, Mark, that is", format(kilometers, '.2f'), "kilometers!")

    FahToCel = float(input("How many degrees Farenheit should we convert to Celsius? "))
    print("Great! So, that is", format(celsius, '.2f'), "degrees Celsius!")

    GalToLit = float(input("Now, how many gallons shall we convert to liters? "))
    print("Great, so that would be", format(liters,'.2f'), "liters!")

    PoundsToKg = float(input("Mark, what about how many pounds to kilograms? "))
    print("That is", format(kilograms,'.2f'), "kilograms, cousin!")

    InchesToCm = float(input("Finally, how many inches do you want converted to centimeters? "))
    print("Okay, running the numbers...it's", format(centi, '.2f'), "centimeters!")

def milesToKm():
    kilometers = milesToKm * 1.6

def FahToCel():
    celsius = (FahToCel - 32) * (5/9)

def GalToLit():
    liters = gallons * 3.9

def PoundsToKg():
    kilograms = pounds * .45

def InchesToCm():
    centi = inches * 2.54

main()
