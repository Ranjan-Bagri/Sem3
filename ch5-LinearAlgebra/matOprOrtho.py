from matOpr import matTrans,matMul
a0,a1,a2=1/3**0.5,1/2**0.5,1/6**0.5
a=[[a0,a0,a0],[a1,-a1,0],[a2,a2,-2*a2]]

at=matTrans(a)
ata=matMul(at,a)
aat=matMul(a,at)

print("     a^ta")

for i in range(len(a)):
    for j in range(len(a)):
        print("%0.3f,"%ata[i][j],end="")
    print("")
print("     aa^t")
for i in range(len(a)):
    for j in range(len(a)):
        print("%0.3f   "%aat[i][j],end="")
    print("")
