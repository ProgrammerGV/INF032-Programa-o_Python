def eh_prefixo(palavra1, palavra2):
    # Retorna True se palavra2 começa com palavra1
    # Utilizando fatiamento (slicing) para demonstração:
    # return palavra2[:len(palavra1)] == palavra1
    # Ou utilizando o método nativo:
    return palavra2.startswith(palavra1)

if __name__ == '__main__':
    p1 = input("Digite a primeira palavra (possível prefixo): ")
    p2 = input("Digite a segunda palavra: ")
    
    resultado = eh_prefixo(p1, p2)
    print(f"'{p1}' é prefixo de '{p2}'? {resultado}")
