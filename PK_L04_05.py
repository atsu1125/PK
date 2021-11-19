n = [] #リストの宣言と初期化
print(n)

for i in range(100): #for文
    n.append(i+1) #リストへの追加
print(n)

total = 0
for i in range(len(n)): #for文
    total = total + n[i]
print(total)
