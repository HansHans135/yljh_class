A=[]
A.append(int(input("底: ")))
A.append(int(input("高: ")))

A.append((A[0]*A[1])/2)

print(f"\n底:{A[0]} 高:{A[1]} 面積:{A[2]}")
print(A)



#正常ㄉ方法
"""
A=[0,0,0]
A[0]=int(input("底: "))
A[1]=int(input("高: "))
A[2]=(A[0]*A[1])/2

print(A[0])
print(A[1])
print(A[2])
"""