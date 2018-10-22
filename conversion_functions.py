###################################################
##  Conversion functions called by Lab 5 Part 2  ##
###################################################

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
