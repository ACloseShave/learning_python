#####################
##Inverted Triangle##
#####################


#Choose base size by asking for user input
#(not required by assignment, I understand)

top_row = int(input("How large should the top row be, in whole numbers?"))
top_row += 1   #corrects "off by one" errors

for i in range(top_row, 0, -1):  #minus 1 makes the next row smaller
    for j in range(i - 1):
        print('*', end='')
    print()
