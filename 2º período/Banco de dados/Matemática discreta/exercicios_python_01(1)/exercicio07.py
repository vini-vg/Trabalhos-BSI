A = {1,2,3}
B = {3,2,1}
C = {2,3,4}

print (A.issubset(C))
print (B.issubset(C))

#Resposta: False, False

print ({1,2} in 𝐴)

#Resposta: resultado esperado é verdadeiro, porém o python da como falso

D = set()
print(D in A)

#Resposta: resultado esperado é falso e o python respeita