def conta_letra(string, letra):
    contador = 0
    for char in string:
        if char == letra:
            contador += 1
    return contador

if __name__ == '__main__':
    string = input("Digite uma string: ")
    letra = input("Digite a letra que deseja contar: ")
    
    if len(letra) == 1:
        quantidade = conta_letra(string, letra)
        print(f"A letra '{letra}' aparece {quantidade} vez(es) na string fornecida.")
    else:
        print("Por favor, digite apenas uma letra para buscar.")
