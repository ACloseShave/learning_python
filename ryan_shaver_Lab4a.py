#Program to convert measurements





print("Hey cousin Mark!\n")
print("Let's convert some measurements together.\n")





#reset while loop interruptor
limit = 0





#begin distance loop with maximum 3 failed inputs
while limit < 3:
	miles = float(input("How many miles do you want converted to kilometers? "))
	if miles < 0:
		print("Try again.")
		limit += 1
	else:
		kilometers = miles * 1.6
		print("Okay, Mark, that is", format(kilometers,'.2f'), "kilometers!")
		limit = 0





#begin temperature loop with maximum 3 failed inputs
while limit < 3:
	faren = float(input("How many degrees Farenheit should we convert to Celsius? "))
	if faren > 1000
		print("That's too hot, Mark!")
		limit += 1
	elif faren < 0:
		print("That's too cold, Mark...")
		limit += 1
	else:
		celsius = (faren - 32) * (5/9)
		print("Great! So, that is", format(celsius,'.2f'), "degrees Celsius!")
		limit = 0





#begin volume loop with maximum 3 failed inputs   
while limit < 3:
	gallons = float(input("Now, how many gallons shall we convert to liters? "))
	if gallons < 0:
		print("I will not calculate negative numbers!")
		limit += 1
	else:
		liters = gallons * 3.9
		print("Great, so that would be", format(liters,'.2f'), "liters!")
		limit = 0





#begin weight loop with maximum 3 failed inputs
while limit > 0:
	pounds = float(input("Mark, what about how many pounds to kilograms? "))
	if pounds < 0:
		print("Not another negative, and I mean it!")
		limit += 1
	else:
		kilograms = pounds * .45
		print("That is", format(kilograms,'.2f'), "kilograms, cousin!")
		limit = 0




		
#begin length loop with maximum 3 failed inputs
while limit > 0:
	inches = float(input("Finally, how many inches do you want converted to centimeters? "))
	if inches < 0:
		print("Error: ...is this some kind of game to you? POSITIVE numbers, Mark!")
		limit += 1
	else:
		centlimit = inches * 2.54
		print("Okay, running the numbers...it's", format(centi,'.2f'), "centimeters!")
		limit = 0

		



print("Great! That's all I have for you!")
