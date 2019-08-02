import random

win = 0
lose = 0
win1=0
win2=0
play = True

print('the door which system will choose is not having prize')
while(play):

    door = [1,2,3]
    a = random.choice(door) 
    b = int(input("Please choose a door (1-3): "))
    if a == b:
        door.remove(a)
        c = random.choice(door)
        print("You chose door {}".format(b))
        print("system choose door {}".format(c))

        door = [1,2,3]
        door.remove(c)
        door.remove(a)
        d = door[0]
        print("You're left with doors {} and {}".format(b,d))
        choice = input("Will you SWITCH to door {}? y/n: ".format(d)) 

        if choice == "y":
            print("You lost. you already had the right answer.")
            lose += 1
        else:
            print("You made the right choice")
            win += 1
            win1+= 1
        print("{} wins and {} losses".format(win,lose))
    
    else:
        door.remove(a)
        door.remove(b)
        e = door[0]
        print("You chose door {}".format(b))
        print("system choose door {}".format(e))

        print("You're left with doors {} and {}".format(a,b))
        choice = input("Will you SWITCH to door {}? y/n: ".format(a)) 

        if choice == "y":
            print("YOU WIN")
            win +=1
            win2+=1
        else:
            print("Bad luck. You chose the wrong door at the start")
            lose += 1
        print("{} wins and {} losses".format(win,lose))

    ans = input("\nPress Enter to play again, 'q' to quit")
    if len(ans) > 0: play = False

prob_strat1 = win1/(win1+win2+lose) 
prob_strat2 = win2/(win1+win2+lose)
print('probability of winning by correct guess is {}'.format(prob_strat1))
print('probability of winning by switching guess is {}'.format(prob_strat2))
