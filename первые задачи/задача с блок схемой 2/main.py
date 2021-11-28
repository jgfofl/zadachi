#!/usr/bin/env python3
# -*- encoding: utf-8-*-
if__name__="__maim__"
import math
x= float(input("x?"))
if x <= 3.5:
    y=2 * x**2 + math.cos( x )
elif 3.5 < x <= 5:
    y=x + 1
else:
    y=2 * x - x**2
print("y",y)


