def conta_vogais_consoantes(nome_arquivo):
    vogais_str = 'aeiouAEIOUáéíóúâêôãõÁÉÍÓÚÂÊÔÃÕ'
    vogais = 0
    consoantes = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            for char in conteudo:
                if char.isalpha():
                    if char in vogais_str:
                        vogais += 1
                    else:
                        consoantes += 1
        return vogais, consoantes
    except FileNotFoundError:
        return -1, -1

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo texto: ")
    v, c = conta_vogais_consoantes(arquivo)
    if v == -1:
        print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        print(f"O arquivo possui {v} vogal(is) e {c} consoante(s).")
