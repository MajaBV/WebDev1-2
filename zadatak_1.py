salary = int(input("You salary is: "))
work_experience = int(input("How many years of work experience do you have: "))

if work_experience >= 10:
    salary2 = round(salary + (work_experience*salary/100))
    print("Your new salary is {0} $".format(salary2))
else:
    print("Unfortunately, the conditions for a pay raise are not met.")