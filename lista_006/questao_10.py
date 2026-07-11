# 10.Criar um programa que deixe entrar com 10 números positivos e imprima a raiz quadrada de cada numero. para cada
# entrada de dados devera haver um trecho de "proteção" para que um numero negativo não seja aceito.
import math

numeros_lidos = 0

while numeros_lidos < 10:
    try:
        num = float(input(f"Digite o {numeros_lidos + 1}º número positivo: "))
        if num < 0:
            print("Erro: O número não pode ser negativo. Tente novamente.")
        else:
            raiz = math.sqrt(num)
            print(f"A raiz quadrada de {num} é {raiz:.4f}")
            numeros_lidos += 1
    except ValueError:
        print("Erro: Entrada inválida. Digite um número.")
