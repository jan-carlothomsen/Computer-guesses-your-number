from random import randint
smallest = 1
biggest = 100
intent = 1
intake = ""
while not intake == "c":
    print(intent, " search between", smallest, " and ", biggest)
    if biggest < smallest:
        print ("don´t cheat")
    else:
        number = randint(smallest, biggest)
    intake = input("{}? ".format(number)).lower()
    if intake == "s":
        smallest = number + 1
    elif intake == "b":
        biggest = number - 1
    intent += 1
    #s input = to small
    #b input = to big
    #c input = correct answer