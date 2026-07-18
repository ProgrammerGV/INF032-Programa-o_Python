def conta_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
            return len(linhas)
    except FileNotFoundError:
        return -1

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo texto: ")
    qtd = conta_linhas(arquivo)
    if qtd == -1:
        print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        print(f"O arquivo possui {qtd} linha(s).")
