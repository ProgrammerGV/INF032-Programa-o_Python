def conta_caractere(nome_arquivo, caractere):
    count = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            for char in conteudo:
                if char == caractere:
                    count += 1
        return count
    except FileNotFoundError:
        return -1

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo texto: ")
    caractere = input("Digite o caractere a ser buscado: ")
    if len(caractere) != 1:
        print("Por favor, digite apenas um caractere.")
    else:
        qtd = conta_caractere(arquivo, caractere)
        if qtd == -1:
            print(f"Arquivo '{arquivo}' não encontrado.")
        else:
            print(f"O caractere '{caractere}' aparece {qtd} vez(es) no arquivo.")
