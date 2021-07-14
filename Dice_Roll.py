import random

def Dn1():
    x=random.randint(1, 6)
    print(x)


if __name__ == '__main__':

    while(True):
        i2=input("Enter your player_Name: ")
        i1=input("Enter 'r' to roll the dice and 'q' to quit: ")

        if i1=='r':
            print(i2)
            Dn1()

        elif i1=='q':
            break


