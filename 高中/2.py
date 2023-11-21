A=[]
A.append(float(input("身高(cm): ")))
A.append(float(input("體重(kg): ")))

A.append(A[1]/((A[0]/100)**2))

print(f"\n身高(cm):{A[0]} 體重(kg):{A[1]} BMI:{A[2]}")
print(A)


#2
"""
A=[0,0,0]
A[0]=int(float(input("身高(cm): ")))
A[1]=int(float(input("體重(kg): ")))
A[2]=A[1]/((A[0]/100)**2)

print(A[0])
print(A[1])
print(A[2])
"""



#1
"""
A=[]
A.append(int(input("底: ")))
A.append(int(input("高: ")))

A.append((A[0]*A[1])/2)

print(f"\n底:{A[0]} 高:{A[1]} 面積:{A[2]}")
print(A)

#

A=[0,0,0]
A[0]=int(input("底: "))
A[1]=int(input("高: "))
A[2]=(A[0]*A[1])/2

print(A[0])
print(A[1])
print(A[2])
"""