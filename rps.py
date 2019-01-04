from random import randint 
import os

def main():
    c_sc = 0
    u_sc = 0
    comp_in = str(randint(1,3))
    user_in = 4
    while user_in != '0':
        try:
            user_in = str(input("Wish to play Press\n 0 to EXIT\n 1 for Rock\n 2 for Paper \n 3 for Scissor \n 4 for Score\n\n"))
            clear()
        except:
            clear()
            print("Invalid input try again\n")
            continue
        if comp_in == user_in:
            print("It's a Draw\n")
        else:
            if user_in == '1':
                if comp_in == '2':
                    c_sc+=1
                    lost()
                elif comp_in == '3':
                    u_sc+=1
                    win()
            elif user_in == '2':
                if comp_in == '3':
                    c_sc+=1
                    lost()
                elif comp_in == '1':
                    u_sc+=1
                    win()
            elif user_in == '3':
                if comp_in == '1':
                    c_sc+=1
                    lost()
                elif comp_in == '2':
                    u_sc+=1
                    win()
            else:
                print('Current Score\n Human: %s Computer: %s\n'%(u_sc,c_sc))
def lost():
    print ("You Lose\n")
def win():
    print('You Win\n')
def clear():
    os.system('clear')
main()