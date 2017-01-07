#!/usr/bin/env python
# This program is using Python 3 :/
#This is my attempt to create a Dice Rolling program to use in absence of having the real thing

import random                                   #Moved to the top of the program for aesthetics
endprogram=0
num=random.randint(1,6)
runthis= input("Would you like to roll the dice? ")

def banner():
  print("Welcome to eDice")                       #Changed indentation of print statements
  print("Press the Enter Key to Roll the D6")
  print("Press 'q' to quit the program")
  print("")

def diceroll():  
  if num  = 1:                               #Fixed indentation (syntax) error
    print("[----------]")
    print("[          ]")
    print("[     1    ]")
    print("[          ]"
    print("[----------]")
    print()
    Print("Type 'q' to Quit")
    runthis

  elif num = 2:
    print("[----------]")
    print("[          ]")
    print("[  2   2   ]")
    print("[          ]")
    print("[----------]")
    print()
    runthis

  elif num = 3:
    print("[----------]")
    print("[  3       ]")
    print("[     3    ]")
    print("[        3 ]")
    print("[----------]")
    print()
    runthis

  elif num = 4:
    print("[----------]")
    print("[  4    4  ]")
    print("[          ]")
    print("[  4    4  ]")
    print("[----------]")
    print()
    runthis

  elif num = 5:
    print("[----------]")
    print("[  5     5 ]")
    print("[     5    ]")
    print("[  5     5 ]")
    print("[----------]")
    print()
    runthis

  elif num = 6:
    print("[----------]")
    print("[  6    6  ]")
    print("[  6    6  ]")
    print("[  6    6  ]")
    print("[----------]")
    print("")
    runthis

  else:
    print ("Sorry, wrong input, try again")
    main()
 
def main():  
  banner()
  while runthis = "Y" or "y":
    diecroll()

if __name__ == "__main__":
  main()
