#!/usr/bin/env python
import random
roll = random.randint(0,20)

def banner():
  print "Welcome to eDice"
  print "Press the Enter Key to Roll the D20"

def rolld20():                                    #This is a virtual d20 sided dice
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

rolld20()
