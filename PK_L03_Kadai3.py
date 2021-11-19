hanibegin = 1
haniend = 5
haniend = haniend + 1
bai = 4

for x in range(hanibegin,haniend):
    for y in range(hanibegin,haniend):

        if (x + y) % bai == 0:
            print("x+y="+str(x+y)+"は"+str(bai)+"の倍数です")
        else:
            print("x+y="+str(x+y)+"は"+str(bai)+"の倍数ではありません")
