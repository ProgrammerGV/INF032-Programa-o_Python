def cidade_mais_populosa(entrada, saida):
    maior_cidade = ""
    maior_populacao = -1
    
    try:
        with open(entrada, 'r', encoding='utf-8') as f:
            for linha in f:
                if len(linha) > 40:
                    cidade = linha[:40].strip()
                    populacao_str = linha[40:].strip()
                    if populacao_str.isdigit():
                        populacao = int(populacao_str)
                        if populacao > maior_populacao:
                            maior_populacao = populacao
                            maior_cidade = cidade
                            
        if maior_cidade:
            with open(saida, 'w', encoding='utf-8') as f_out:
                f_out.write(f"{maior_cidade} {maior_populacao}\n")
            return True
        return False
    except FileNotFoundError:
        return False

if __name__ == '__main__':
    entrada = input("Digite o arquivo de entrada: ")
    saida = input("Digite o arquivo de saída: ")
    if cidade_mais_populosa(entrada, saida):
        print("Arquivo gerado com sucesso!")
    else:
        print("Falha ao processar ou arquivo não encontrado.")
