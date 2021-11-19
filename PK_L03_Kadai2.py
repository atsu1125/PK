hanibegin = 1
haniend = 3
haniend = haniend + 1
for x in range(hanibegin,haniend):
    for y in range(hanibegin,haniend):
        for z in range(hanibegin,haniend):
            print("x="+str(x)+", y="+str(y)+", z="+str(z)+"のとき, xy+yz+zx="+str(x*y+y*z+z*x))
