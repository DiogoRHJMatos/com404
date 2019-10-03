print("What type of cover does the book have? (soft/hard)")
cover_t = input()

if(cover_t == "soft"):
    print("Is the book perfect-bound? (yes/no)")
    per_bou = input()

    if(per_bou == "yes"):
        print("Soft cover, perfect-bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

elif(cover_t == "hard"):
    print("Books with hard covers can be more expensive!")

else:
    print("beep didnt understand")
