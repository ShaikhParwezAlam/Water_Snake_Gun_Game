
from logging import exception
from random import randint
import sys
def gameDecide(user,c): 
    if user==c:
        return None
    elif c=='w':
        if user=='s':
            return True 
        elif user=='g':
            return False 
    elif c=='g':
        if user=='s':
            return False
        elif user=='w':
            return True 
    elif c=='s':
        if user=='w':
            return False 
        elif user=='g':
            return True 
print(' Welcome \n   to\n The Game')
count=0
loss=0
while 1:
    r=randint(1,3)
    c=' '
    if(r==1):
        c='s'
    elif(r==2):
        c='w'
    elif(r==3):
        c=='g'
    while 1:
        user=input('Choose Water(w),Gun(g),Snake(s) : ')
        try:
            if(user=='g' or user=='s' or user=='w'):
                break
            elif(user=='0'):
                r=count-loss
                if(r<=0):
                    print("Oopps ! You Lost The Game")
                    print("Better Luck Next Time")
                    sys.exit()
                else:
                    print(f"You Won {r} Times")
                    print("Thank you for Playing")
                    sys.exit()
            else:
                raise ValueError
        except ValueError:
            print("choose again or\nif you want to exit press 0")
            continue
    result=gameDecide(user,c)
    if result:
        count=count+1
        print('You Win!')
        print('if you want to exit press 0...Else')
    elif result==False:
        loss=loss+1
        print('You Lose!')  
        print('if you want to exit press 0...Else') 
    else:
        print('Match Tie')
        print('if you want to exit press 0...Else')
        