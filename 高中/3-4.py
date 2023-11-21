import random
a=random.randint(1,10)
u=0

while u!=a:
    u=int(input("猜吧: "))
    if u>a :
        print("太大了")
    else:
        print("太小了")
        
print("猜到了")