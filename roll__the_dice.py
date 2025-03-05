def game():
    import random                                                            #10 Jan 2025
    while True:
        user = input("Roll the dice (y/n):- ")
        if user=="y":
            D1 = random.randint(1, 6)
            D2 = random.randint(1, 6)
            print(f"({D1}, {D2})")
        elif user=="n":
            print("Thanks for playing!")
            break 
        else:
            print("invalid choice")
            continue

game()


