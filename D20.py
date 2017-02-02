#!/usr/bin/env python
import random
roll = random.randint(0,20)
response = rawinput("Do you wish to roll again, (Y)es or (N)o ?")

def banner():
  print "Welcome to eDice"
  print "Press the Enter Key to Roll the D20"

def rolld20():                                    #Function for the dice.  
  print ""
  print "  /---------\  "
  print " /           \ "
  print " |           | "
  print " |     "+str(roll).zfill(2)+"    | " 
  print " |           | "
  print " \           / "
  print "  \---------/  "
  if roll == 0:
    print "OUCH!"
  if roll >= 17 and roll <= 19:
    print "POSSIBLE CRITICAL"
  if roll == 20:
    print "CRITICAL!"
'''
def main():                                       #
  banner()
  while response == "Y" or "y":
    rolld20()

if __name__ == "__main__":
  main()
'''