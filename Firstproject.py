'''import random
import sys
import os'''

bottletext1 = "Bottles of beer"
bottletext1sing = "Bottle of beer"
bottletext2 = "on the wall!"
bottletext3 = "take one down, pass it around,"
bottletext3sing = "take it down, pass it around"

for xopp in range(1,100):
    x =100-xopp
    if x>2:
        print(x,bottletext1,bottletext2,x,bottletext1,"...",bottletext3, x-1, bottletext1, bottletext2, '\n')
    elif x==2:
        print(x, bottletext1, bottletext2, x, bottletext1, "...", bottletext3, x - 1, bottletext1sing, bottletext2, '\n')
    else:
        print(x, bottletext1sing, bottletext2, x, bottletext1sing, "...", bottletext3sing, x - 1, bottletext1, bottletext2,
              '\n')
        
