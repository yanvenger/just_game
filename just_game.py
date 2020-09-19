checker = ["", "", "", ""]
counter = 0
for n in checker:
    checker[counter] = input(f"step {counter+1}. type char y(=yes) and n(=no)")
    while checker[counter] not in "yn":
        print("Wrong statement, please try again\n")
        checker[counter] = input(f"still step {counter+1}. type char y(=yes) and n(=no)")
    counter += 1

print(">>>is the system online?")
if checker[0] == "y":
    print("...yes!")
    print(">>>don't even touch it!!!")
    print(">>>All ist OK")
else:
    print("...damn no!")
    print(">>>is it your fault?")
    if checker[1] == "no":
        print("...no!")
        print(">>>you're save")
    else:
        print("...damn yes!")
        print(">>>you idiot!!!")
        print(">>>has anyone noticed it?")
        if checker[2] == "n":
            print("...no!")
            print(">>>nobody will ever find you, you're save!!!")
        else:
            print("...yes")
            print(">>>you're f***ed!")
            print(">>>can you blame it on someone else?")
            if checker[3] == "n":
                print("...damn, no I can't!")
                print(">>>you're really f***ed!!!")
            else:
                print("Thank god, yes")
                print(">>> Don't worry someone else is f***ed :)")
