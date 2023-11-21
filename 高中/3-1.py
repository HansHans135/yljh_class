a=float(input("身高(cm)"))
b=float(input("體重(kg)"))

A=b/((a/100)**2)
print(A)
if A<18.5:
    print("體重過輕")
elif 18.5<=A and A<24:
    print("正常範圍")
elif 24<=A and A<27:
    print("過重")
elif 27<=A and A<30:
    print("輕度肥胖")
elif 30<=A and A<35:
    print("中度肥胖")
else:
    print("重度肥胖")