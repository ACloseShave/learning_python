#Program to convert measurements





print("Hey cousin Mark!")
print("Let's convert some measurements together.")


def main():
    miles = float(input("How many miles do you want converted to kilometers? "))
    milesToKm(miles)

    fah = float(input("How many degrees Farenheit should we convert to Celsius? "))
    FahToCel(fah)

    gallons = float(input("Now, how many gallons shall we convert to liters? "))
    GalToLit(gallons)

    pounds = float(input("Mark, what about how many pounds to kilograms? "))
    PoundsToKg(pounds)
 
    inches = float(input("Finally, how many inches do you want converted to centimeters? "))
    InchesToCm(inches)

def milesToKm(milesToKm):
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
