#matriz 3x3 direta
#matriz_inicDireta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#for linha in range(0, 3):
    #print("Linha", linha)
    
#for coluna in range(0, 3):
    #print(matriz_inicDireta[linha][coluna])
    
#matriz 3x4 dinâmica    
#nLinhas = 3
#nColunas = 4
#matriz_dinamica = [0] * nLinhas


#matriz de notas para 3 alunos com 4 notas cada
#for linha in range(nLinhas):
    #matriz_dinamica[linha] = [0] * nColunas
    
#print(matriz_dinamica)

#nAlunos = 3
#nNotas = 4

#matriz = [0] * nAlunos

#for aluno in range(nAlunos):
#    matriz[aluno] = [0] * nNotas
    
#for aluno in range(nAlunos):
#    for nota in range(nNotas):
#        matriz[aluno] [nota] = float(input("digite uma nota: "))
     
#for aluno in range(nAlunos):
#   soma = 0
#    for nota in range (nNotas):
#        soma = soma + matriz[aluno] [nota]
#        media = soma /4
    
#    print("nota", aluno, "=", media)




nLinhas = 2
nColunas = 2
matrizA = [0] * nLinhas
matrizB = [0] * nLinhas
matrizC = [0] * nLinhas
for linha in range(nLinhas):
    matrizA[linha] = [0] * nColunas
    matrizB[linha] = [0] * nColunas
    matrizC[linha] = [0] * nColunas
print('Matriz A')

for linha in range(nLinhas):
    for coluna in range(nColunas):
        matrizA[linha][coluna] = int(input('Digite um valor: '))
print('Matriz B')

for linha in range(nLinhas):
    for coluna in range(nColunas):
        matrizB[linha][coluna] = int(input('Digite um valor: '))

for linha in range(nLinhas):
    for coluna in range(nColunas):
        matrizC[linha][coluna] = matrizA[linha][coluna] + matrizB[linha][coluna]
print(matrizC)
    
    
    
