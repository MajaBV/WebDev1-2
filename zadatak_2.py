x = abs(int(input("First number: ")))
y = abs(int(input("Second number: ")))

z = str(x) + str(y)
q = str(y) + str(x)

if x == 0 or y == 0:
    print("Error")
elif x >= 10 or y >= 10:
    print("Error")
elif x % 2 == 0 and y % 2 == 0 and x == y:
    print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2}".format(x, y, z))
elif x % 2 == 0 and y % 2 == 0:
    print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2} i {3}".format(x, y, z, q))
elif x % 2 == 0 and y % 2 != 0:
    print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2}".format(x, y, q))
elif x % 2 != 0 and y % 2 == 0:
    print("Parni brojevi stvoreni od znamenaka {0} i {1} su: {2}".format(x, y, z))
else:
    print("Nema parnih brojeva.")