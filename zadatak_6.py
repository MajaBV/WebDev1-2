numbers = input("Početna vrijednost: ")
brojac = 0
separate = list(numbers)[::-1]
for number in separate:
    print(int(number)**2)
    brojac += 1
print("Number has {0} digits".format(brojac))