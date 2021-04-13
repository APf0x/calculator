import time
import os
while True:
# incoming features
#if you find any errors plz contact me in some way i dont know how tho from now on i will explain what am i doing and how does it work.
#logo: this is the logo of the programm
#i put this while true just for restarting the program when it finishes go see at the end of the code for further info 

    
    os.system('color a')
    
    print('''


█████████████████████████████████████████████████████████████
█─▄▄▄─██▀▄─██▄─▄███─▄▄▄─█▄─██─▄█▄─▄████▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀█
█─███▀██─▀─███─██▀█─███▀██─██─███─██▀██─▀─████─███─██─██─▄─▄█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀

''')

    time.sleep(1)

#and APf0x/redfox is my name it is made by me.

    print('''

█▀▄▀█ ▄▀█ █▀▄ █▀▀   █▄▄ █▄█   ▄▀█ █▀█ █▀▀ █▀█ ▀▄▀
█░▀░█ █▀█ █▄▀ ██▄   █▄█ ░█░   █▀█ █▀▀ █▀░ █▄█ █░█

''') 

#from here the program starts    

    print ('''
- to perform the triangle, press 1 ;
- to execute the square and rectangle press 2;
''')
    
#first part just for choosing whith geometric form u want to calculate
    
    while True:
        choise = input('Enter a number corresponding to your selected operation ---> ')
        if choise in ['1', '2', '3', '4']:
            break
    #this is option 1 triangle there will be other 2 options maybie one more in the future
    if choise == "1":
        print('\nyou chose: 1 rettangolo\n')
        print('''
          - to execute the perimeter, press <11>;
          - to perform the area, press <12>;
          ''')
        while True:
            triangle = input("Enter a number corresponding to your selected operation ---> ")
            if triangle in ['11', '12']: 
               break
        #these are the 2 options i wat talking abought the first is for the perimeter and the second one is for the area
        if triangle == "11":
            a = int(input("the first side: "))
            b = int(input("the second: "))
            c = int(input("the third: ")) 
            d = a+b+c
            print(d)
            
        elif triangle == "12":
            a = int(input("the first side: "))
            b = int(input("the second: "))
            c = a*b/2
            print(c)
            

    elif choise == "2":
        print('\nyou chose: 2 square and rectangle\n')
        print('''
          - to execute the perimeter, press <21>;
          - to perform the area, press <22>;
          ''')
        while True:
            square = input("Enter a number corresponding to your selected operation ---> ")
            if square in ['21', '22']: 
               break
        if square == "21":
            a = int(input("the first side: "))
            b = int(input("the second: "))
            c = int(input("the third: ")) 
            d = int(input("the fourth:"))
            e = a+b+c+d
            print(e)
        elif square == "22":
            a = int(input("the first side: "))
            b = int(input("the second: "))
            c = a*b
            print(c)
            time.sleep(1)

            
        

#this is why at the start i put a while. there are 2 options the first is for restarting the program and the second is for quitting
    while True:
        time.sleep(1)
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        os.system('cls')
        continue
    else:
        print("Goodbye")
        break


