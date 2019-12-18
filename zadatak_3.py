money = int(input("Enter the amount you want: "))

if money < 0:
    print("Error")

if money >= 50:
    print("Broj novčanice od 50 kn: {0}".format(int(money/50)))
    money = money % 50

if money >= 20:
    print("Broj novčanice od 20 kn: {0}".format(int(money/20)))
    money = money % 20

if money >= 5:
    print("Broj novčanice od 5 kn: {0}".format(int(money/5)))
    money = money % 5

if money >= 2:
    print("Broj novčanice od 2 kn: {0}".format(int(money/2)))
    money = money % 2

if money >= 1:
    print("Broj novčanice od 1 kn: {0}".format(int(money/1)))
