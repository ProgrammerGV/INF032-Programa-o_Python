def eh_perfeito(num):
    if num <= 1:
        return False
    soma_fatores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_fatores += i
    return soma_fatores == num

def lista_perfeitos_ate(n):
    perfeitos = []
    for i in range(1, n + 1):
        if eh_perfeito(i):
            perfeitos.append(str(i))
    if perfeitos:
        print(" ".join(perfeitos))
    else:
        print("Nenhum número perfeito encontrado.")

if __name__ == '__main__':
    try:
        n = int(input("Digite um inteiro positivo n: "))
        if n > 0:
            print(f"Números perfeitos até {n}:")
            lista_perfeitos_ate(n)
        else:
            print("Por favor, digite um inteiro positivo maior que 0.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
