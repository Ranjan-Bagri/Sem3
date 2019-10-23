from matOpr import matSum, matScp,matTrans,matMul

u=[[-2],[4],[1]]
v=[[3],[-2],[1]]
ux=[[0,-u[2][0],u[1][0]],[u[2][0],0,-u[0][0]],[-u[1][0],u[0][0],0]]
print(matMul(ux,v))