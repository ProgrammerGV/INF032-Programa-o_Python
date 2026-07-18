def junta_arquivos(arq1, arq2, saida):
    try:
        with open(arq1, 'r', encoding='utf-8') as f1:
            conteudo1 = f1.read()
            
        with open(arq2, 'r', encoding='utf-8') as f2:
            conteudo2 = f2.read()
            
        with open(saida, 'w', encoding='utf-8') as f_out:
            f_out.write(conteudo1)
            # Adiciona quebra de linha caso o arquivo 1 não termine com uma
            if conteudo1 and not conteudo1.endswith('\n'):
                f_out.write('\n')
            f_out.write(conteudo2)
            
        return True
    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return False

if __name__ == '__main__':
    arq1 = input("Digite o nome do primeiro arquivo: ")
    arq2 = input("Digite o nome do segundo arquivo: ")
    saida = input("Digite o nome do arquivo de saída: ")
    
    if junta_arquivos(arq1, arq2, saida):
        print(f"Arquivo '{saida}' gerado com sucesso contendo a união de '{arq1}' e '{arq2}'.")
    else:
        print("Não foi possível gerar o arquivo de saída.")
