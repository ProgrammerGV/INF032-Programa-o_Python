def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def menu():
    print("Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    escolha = input("Escolha uma opção (1 ou 2): ")

    if escolha == '1':
        c = float(input("Digite a temperatura em Celsius: "))
        f = celsius_para_fahrenheit(c)
        print(f"{c:.2f} Celsius é igual a {f:.2f} Fahrenheit")
    elif escolha == '2':
        f = float(input("Digite a temperatura em Fahrenheit: "))
        c = fahrenheit_para_celsius(f)
        print(f"{f:.2f} Fahrenheit é igual a {c:.2f} Celsius")
    else:
        print("Opção inválida.")

if __name__ == '__main__':
    menu()
