import random                                                              #10 Jan 2025
ai = random.randint(1, 100)

# use try and except function to avoid error  

while True:
    try:                  
        user = int(input("guess a number between 1 and 100:- "))
        if user>ai:
            print("Too High..!")
            continue
        elif user<ai:
            print("Too low..!")
            continue
        elif user<0 or user>100:
            print("Invalid input!")
            continue
        else:
            print("Congratulation! you guessed the right number")
            break
    except:
        print("Invalid input!")
