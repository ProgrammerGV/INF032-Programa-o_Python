def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def exibe_fibonacci(n):
    # Exibe os termos de 1 até n (a sequência começa com os índices 0, 1, 2...)
    termos = []
    for i in range(n):
        termos.append(str(fibonacci(i)))
    print(" ".join(termos))

if __name__ == '__main__':
    try:
        n = int(input("Digite um inteiro positivo n: "))
        if n > 0:
            exibe_fibonacci(n)
        else:
            print("Por favor, digite um inteiro positivo maior que 0.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
