#!/usr/bin/env python3

#always have to initialize the programs prior to the commands
import sys

myname = ('Marina')

#If I were to share this script with someone else, and they wanted it to output their name, not my name, they need to run the script and add their name at the end. Basically like "changing" the script from unix. 
#Called hardcoding
#The placement of sys.argv argument is Important! 
#If sys.argv argument is before 'myname=('Marina')' then it will error unless a name is always provided from the unix comandline. 
#If it's after 'myname=('Marina')' then it'll print My name, UNLESS I provide an alternative name, then it'll print that name.

myname = sys.argv[1]
print('My name is:', myname)

favcol = ('blue')
favcol = sys.argv[2]
print('My favorite color is:', favcol)

favactivity = ('cycling long distances with hills')
favactivity = sys.argv[3]
print('I enjoy', favactivity)

favanimal = ('caterpillars')
favanimal = sys.argv[4]
print('My favorite animals(s):', favanimal)

#starting after this assignment, I'll be splitting up each problem and saving them as successive, indepented files that I can go back to later and track my progression through the learning material. 
