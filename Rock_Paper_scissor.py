import random 

def print_line():                                                    #10 Jan 2025
    print(f"your choice = {dic[user]}")
    print(f"coumputer choice = {dic[ai]}")                           #modified: 12 Jan 2025


def determine_winner():
    if \
        (user=="r" and ai=="p") or\
        (user=="p" and ai=="s") or\
        (user=="s" and ai=="r"):
        print("You loose!")
    elif\
        (user=="r" and ai=="s") or\
        (user=="p" and ai=="r") or\
        (user=="s" and ai=="p"):
        print("You win!")
    elif (user==ai):
        print("draw!")
    else:
        print("Invalid choice!")

try:                                                                        
    while True:
        dic = {"r":"rock", "p":"paper", "s":"scissor"}
        ai = random.choice(["r", "p", "s"])
        user = input("Rock, paper or scissor (r/p/s):- ")

        print_line()

        determine_winner()
        
        ask_to_continue = input("Do you want to continue (y/n):- ")
        if ask_to_continue == "y":
            continue
        else: break

except:
    print("error!")


