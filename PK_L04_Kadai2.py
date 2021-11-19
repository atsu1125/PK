fruit = ["apple","orange","cherry","banana","strawberry"]
apple = ["ふじ","ジョナゴールド","王林"]

def elements(l):
    for n in range(len(l)):
        print(str(n+1)+"番目の要素は"+l[n]+"です")
        n = n + 1
elements(fruit)

elements(apple)
