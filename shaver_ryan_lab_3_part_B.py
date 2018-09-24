########################################
#     GROSS INCOME FOR SALES STAFF     #
########################################



########################
#      Section 1:      #
#  User Input Prompts  #
########################

name_of_employee = input("Enter the salesperson's first and last name:")


months_employed = input("How many months has " + name_of_employee + " worked for SoftwarePirates Inc.?")
months_employed = int(months_employed)


sales_amount_in_dollars = input("How much (in USD) has " + name_of_employee + " made in sales this month?")
sales_amount_in_dollars = float(sales_amount_in_dollars)


days_of_vacation_this_month = input("How many vacation days has " + name_of_employee + " taken this month?")
days_of_vacation_this_month = int(days_of_vacation_this_month)


bonus_rate_initial = 0
base_salary_per_month = 2000


########################
#      Section 2:      #
#   Vacation Penalty   #
########################

if days_of_vacation_this_month > 3:
    penalty = 200
else:
    penalty = 0


########################
#       Section 3:     #
#    Amount of Sales   #
########################

if months_employed < 3:
    bonus_rate_final = 0
    if sales_amount_in_dollars < 10000:
        commission = 0
    elif 10000 <= sales_amount_in_dollars <= 100000:
        commission = .02
    elif 100001 <= sales_amount_in_dollars <= 500000:
        commission = .15
    elif 500001 <= sales_amount_in_dollars <= 1000000:
        commission = .28
    else:
        commission = .35
elif 3 < months_employed < 60:
    if sales_amount_in_dollars < 10000:
        commission = 0
        commission = int(commission)
        bonus_rate_initial = 0
    elif 10000 <= sales_amount_in_dollars <= 100000:
        commission = 0.02
        commission = float(commission)
        bonus_rate_initial = 0
    elif 100001 <= sales_amount_in_dollars <= 500000:
        commission = 0.15
        commission = float(commission)
        bonus_rate_initial = 1000
    elif 500001 <= sales_amount_in_dollars <= 1000000:
        commission = 0.28
        commission = float(commission)
        bonus_rate_initial = 5000
    elif sales_amount_in_dollars > 1000001:
        commission = 0.35
        commission = float(commission)
        bonus_rate_initial = 100000
else:
    bonus_rate_final = bonus_rate_initial + 1000


########################
#       Section 4:     #
#     Gross Salary     #
########################

gross_salary = sales_amount_in_dollars * commission + base_salary_per_month + bonus_rate_final - penalty


print("Name:",name_of_employee)
print("Base Salary:                         ","$",
      format(base_salary_per_month,',.2f'),
      sep='')
print("Sales:                               ","$",
      format(sales_amount_in_dollars,',.2f'),
      sep='')
print("Commission:                          ",
      format(commission,'.0%'),
      sep='')
print("Rate Bonus:                          ","$",
      format(bonus_rate_initial,',.2f'),
      sep='')
print("Tenure Bonus:                        ","$",
      format(bonus_rate_final,',.2f'),
      sep='')
print("Vacation Penalty:                    ","$",
      format(penalty,',.2f'),
      sep='')
print("Total Amount:                        ","$",
      format(gross_salary,',.2f'),
      sep='',)