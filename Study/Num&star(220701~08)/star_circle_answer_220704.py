# 220704 자습
# 원을 만들어요

r = 15

for star_row in range(-r,r+1):
    for star_col in range(-r,r+1):
        if((star_row*star_row)+(star_col*star_col))<=(r*r):
            print("*",end="")
        else:
            print(" ",end="")
    print()