# 1. Entrar como n's números e imprimir o triplo de cada. o programa encerra quando entrar com o numero 999;

while True:
    try:
        numero = float(input("Digite um número (999 para sair): "))
        if numero == 999:
            break
        print(f"O triplo de {numero} é {numero * 3}")
    except ValueError:
        print("Entrada inválida. Digite um número.")
