def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def lista_primos_ate(n):
    primos = []
    for i in range(1, n + 1):
        if eh_primo(i):
            primos.append(str(i))
    print(" ".join(primos))

if __name__ == '__main__':
    try:
        n = int(input("Digite um inteiro positivo n: "))
        if n > 0:
            print(f"Primos de 1 até {n}:")
            lista_primos_ate(n)
        else:
            print("Por favor, digite um inteiro positivo maior que 0.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
