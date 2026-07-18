def substitui_vogais(nome_arquivo):
    vogais = 'aeiouAEIOUáéíóúâêôãõÁÉÍÓÚÂÊÔÃÕ'
    novo_nome = 'saida_q06.txt'
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            
        for v in vogais:
            conteudo = conteudo.replace(v, '*')
            
        with open(novo_nome, 'w', encoding='utf-8') as f:
            f.write(conteudo)
            
        return novo_nome
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo texto: ")
    resultado = substitui_vogais(arquivo)
    if resultado is None:
        print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        print(f"Arquivo gerado com sucesso: '{resultado}'.")
