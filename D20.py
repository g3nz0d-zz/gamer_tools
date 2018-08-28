#!/usr/bin/env python
import random
roll = random.randint(0,20)

def banner():
  print ""
  print "----- Welcome to eDice -----"
  print ""

def rolld20():                                    #Function for the dice.  
  print ""
  print "  /---------\  "
  print " /           \ "
  print " |           | "
  print " |     "+str(roll).zfill(2)+"    | " 
  print " |           | "
  print " \           / "
  print "  \---------/  "
  print ""
  if roll == 0:
    print "OUCH!"
  if roll >= 17 and roll <= 19:
    print "POSSIBLE CRIT!"
  if roll == 20:
    print "!!!CRIT!!!"

def main():
  banner()
  rolld20()

if __name__ == "__main__":
  main()
