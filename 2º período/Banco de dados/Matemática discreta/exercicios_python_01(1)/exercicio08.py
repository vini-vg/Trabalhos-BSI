A = {1,2,3}
C = {1,2,3,4,5}
D = {5,3,4,2,1}

if A.issubset(C):
    print("A é subconjunto de C")
else:
    print("Não é subconjunto de C")

if D.issubset(C) == True:
    print("D é subconjunto de C")
else:
    print("Não é subconjunto de C")
        
#Resposta: A é subconjunto de C, D é subconjunto de C
