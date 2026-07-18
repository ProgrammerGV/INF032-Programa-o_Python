def conta_vogais(nome_arquivo):
    vogais = 'aeiouAEIOUáéíóúâêôãõÁÉÍÓÚÂÊÔÃÕ'
    count = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            for char in conteudo:
                if char in vogais:
                    count += 1
        return count
    except FileNotFoundError:
        return -1

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo texto: ")
    qtd = conta_vogais(arquivo)
    if qtd == -1:
        print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        print(f"O arquivo possui {qtd} vogais.")
