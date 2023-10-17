#Implemente um programa em Python para verificar se um número
#passado como argumento para um módulo está em um determinado
#intervalo de valores, também passado como argumento. Se estiver o
#módulo retorna True, senão False

def analisar_numero(numero, intervalo_inf, intervalo_sup):
    if numero >= intervalo_inf and numero <= intervalo_sup:
        return True
    return False

    resultado = verificar_numero(26,1,45)
    print(resultado)