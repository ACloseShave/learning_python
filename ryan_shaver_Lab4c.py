##############################################
##Converting numeric grades to letter grades##
##############################################




grade_to_enter = 'y'              #defines starting loop control condition
total_score = 0                   #sets total score of numeric grades to 0
grades_entered = 0                #sets initial grades entered as 0

###############                   #inputing grades from the user input
##Grade input##                   #in order to calculate a total amount
###############                   #and later to average the class grades


while grade_to_enter == 'y': 
    print("Do you have a grade to enter?")
    grade_to_enter = input("Enter 'y' for YES:")

    if grade_to_enter == 'y':
        numeric_grade = int(input("Enter your numeric grade in whole numbers: "))
        if numeric_grade < 0:     #to meet the -1 requirement
            exit(0)
        elif 0 <= numeric_grade < 60:
            print("You made an F! Why didn't you study?")
        elif 60 <= numeric_grade < 70:
            print("You made a D! You need to study longer!")
        elif 70 <= numeric_grade < 80:
            print("You made a C! At least you technically passed!")
        elif 80 <= numeric_grade < 90:
            print("You made a B! Well done, but you could do better!")
        elif 90 <= numeric_grade < 100:
            print("You made a A! You are helping that bell curve!")
        elif 100 <= numeric_grade < 101:
            print("You got a perfect A...Did you cheat somehow?")
        else:
            print("It's not possible to score more than 100.")  #counteracts skewing the average
            grades_entered -= 1   #counteracts an off-by-one error from an above 100 grade
    elif grade_to_enter == 'n':
        break
    else:
        exit(0)
    total_score = total_score + numeric_grade  #running total of numeric grade values
    grades_entered += 1       #tracking number of grades for later average
        

average_score = total_score / grades_entered    #defining average score


print("Total score: ", total_score)    #prints sum of numeric grades (not necessary, but helps for testing math)



####################################
##Calculating average letter grade##
####################################

if 0 <= average_score < 60:
    average_score = "F"
elif 60 <= average_score < 70:
    average_score = "D"
elif 70 <= average_score < 80:
    average_score = "C"
elif 80 <= average_score < 90:
    average_score = "B"
else:
    average_score = "A"


print("Average grade for the class: ", average_score)   #prints average letter grade for class
print("Number of grades entered: ", grades_entered)     #prints number of grades entered


