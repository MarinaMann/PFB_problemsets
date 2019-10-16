#!/usr/bin/env python3

myname = ('Marina')
print('My name is:', myname)

favcol = ('blue')
print('My favorite color is:', favcol)

favactivity = ('cycling long distances with hills')
print('I enjoy', favactivity)

favanimal = ('caterpillars')
print('My favorite animals(s):', favanimal)

import sys
myname = sys.argv[1]
favcol = sys.argv[2]
faactivity = sys.argv[3]
favanimal = sys.argv[4]
print(myname, favcol, favactivity, favanimal)
