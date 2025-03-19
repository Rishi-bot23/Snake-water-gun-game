import random
import sys
 # 1 is for  snake
 # 2 is for water
 # 3 is for gun

computer = random.choice([1,2,3])
youstr = input("enter your choise[SNAKE,WATER,GUN] :").lower()# gets input from user and comverts in into lower case
youdisc = { "snake" : 1, "water" : 2, "gun" : 3} #disc allocating values to the keys
reversedisc = {1 : "SNAKE", 2: "WATER" , 3: "GUN"} # reversedisc for printing user input as well as computer input

if youstr not in youdisc: 
  print("invalid input")
  sys.exit()#stops the code if invalid input

you = youdisc[youstr]

print(f" you choose :{reversedisc[you]}\n computer choose :{reversedisc[computer]}")

if (computer == you):
    print("its a draw")
else:
    if(computer == 1 and you == 2):
        print(" computer win!! you lose!!")

    elif(computer == 1 and you ==3):
        print(" computer lose!! you win!!")

    elif(computer == 2 and you ==1):
         print(" computer lose!! you win!!")
    elif(computer == 2 and you ==3):
         print(" computer win!! you lose!!")
    elif(computer == 3 and you ==1):
       print(" computer win!! you lose!!")
    elif(computer == 3 and you ==2):
        print(" computer lose!! you winn!!")
    else:
       print(" something went wrong")

    
