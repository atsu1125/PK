r = 100
bai = 2
n = []

for i in range(r):
    n.append(i+1)

total = 0
count = 0

for i in range(len(n)):
    if n[count] % bai == 0:
        total = total + n[count]
        count = count + 1
    else:
        count = count + 1
    
print(total)
