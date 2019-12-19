number = int(input("Početna vrijednost: "))
brojac = 0

while True:
    if number < 1:
        print("Error")
        break
    while number > 1:
        if number % 2 == 0:
            new_number = int(number / 2)
            brojac += 1
        else:
            new_number = int((number * 3) + 1)
            brojac += 1

        number = new_number

        print("Slijedeća vrijednost: {0}".format(new_number))
    print("Krajnja vrijednost: {0}, broj koraka: {1}.".format(number, brojac))
    break



