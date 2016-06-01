'''import random
import sys
import os'''

#broke up lyrics into blocks for easy calling in for loop
bottletext1 = "Bottles of beer"
#separate line for singular bottle - though it may take less resources for directly putting this in to the for loop
bottletext1sing = "Bottle of beer"
bottletext2 = "on the wall!"
bottletext3 = "take one down, pass it around,"
#same thing here, for singular bottle
bottletext3sing = "take it down, pass it around"

#for loop runs from 1-100, wasn't sure that I could have it count down instead, so used a simple variable to reverse it
for xopp in range(1,100):
    x =100-xopp
    #includes all loops until 2 bottles of beer, as the lyric would change to incorporate a single bottle
    if x>2:
        print(x,bottletext1,bottletext2,x,bottletext1,"...",bottletext3, x-1, bottletext1, bottletext2, '\n')
    elif x==2:
        print(x, bottletext1, bottletext2, x, bottletext1, "...", bottletext3, x - 1, bottletext1sing, bottletext2, '\n')
    else:
        print(x, bottletext1sing, bottletext2, x, bottletext1sing, "...", bottletext3sing, x - 1, bottletext1, bottletext2,
              '\n')
        
