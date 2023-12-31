import ships
import random

# User interface , ask user for a nr.

def get_shot(guesses):

    ok = "n"
    while ok == "n":
        try:
            shot = input("Please enter a nr :" )
            shot = int(shot)
            if shot < 0 or shot > 99:
                print("please type a nr between 0/99")
            elif shot in guesses :
                print("Already in use !!  please try again ! ")
            else:
                ok = "y"
                break
        except:
            print("incorrect !!  please try again ! ")
    return shot

# Table and function for hit, miss, and comp

def show_board(hit,miss,comp):                      
    print("            battleships    ")
    print()
    print("     0  1  2  3  4  5  6  7  8  9")


    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place  in hit:
                ch = " o "
            elif place  in comp:
                ch = " 0 "

            row = row + ch
            place = place + 1
        print(x," ",row)


# Check if user answer hit mis or comp. "check shot"

def check_shot(shot,boat1,boat2,hit,miss,comp):

    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    
    elif shot in boat2:
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
        else:
            comp.append(shot)
    else:
        miss.append(shot)     

    return boat1,boat2,hit,miss,comp


boat1 = [46,47,48,]
boat2 = [22,23,24,25]


hit = []
miss = []
comp = []

for i in range(100):
    guesses = hit + miss + comp
    shot = get_shot(guesses)
    boat1,boat2,hit,miss,comp = check_shot(shot,boat1,boat2,hit,miss,comp)
    show_board(hit,miss,comp)

    if len(boat1) < 1 and len(boat2) <1:
        print("you win ")
        break
print("Finishd")