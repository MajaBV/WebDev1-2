brojac1 = 0
brojac2 = 0
brojac3 = 0
while True:
    number = int(input("Enter the number: "))

    if number % 3 == 0 and number % 5 == 0:
        brojac1 += 1
    elif number % 3 == 0:
        brojac2 += 1
    elif number % 5 == 0:
        brojac3 += 1

    else:
        break

print("Unesena su {0} broja djeljiva s 3 i sa 5.".format(brojac1))
print("Unesena su {0} broja djeljiva s 3 .".format(brojac2))
print("Unesena su {0} broja djeljiva sa 5.".format(brojac3))
