#atividade 1

#def calcular_imc(peso, altura):
    #if altura > 0:
        #imc = peso / (altura  * altura)
        #return imc

    #return False

#valor_imc = calcular_imc(58, 1.83)
#print (valor_imc)

#atividade 2

def encontrar_palavras(frase):
    palavras = 0
    
    for cont in range(len(frase)):
        if frase [cont] == ' ':
            palavras = palavras + 1

    return palavras + 1

frase = input("digite uma frase: ")
numero_palavras = encontrar_palavras(frase)
print(numero_palavras)

