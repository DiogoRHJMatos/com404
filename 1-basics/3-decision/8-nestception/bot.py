print("Where should I look?")
where = input()

if(where == "in the bedroom"):
    print("Where in the bedroom should I look?")
    bed_a = input()

    if(bed_a == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

elif(where == "in the bathroom"):
    print("Where in the bathroom should I look?")
    bath_a = input()

    if(bath_a == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")

elif(where == "in the lab"):
    print("Where in the lab should I look?")
    lab_a = input()

    if(lab_a == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

else:
    print("I do not know where that is but I will keep looking.")