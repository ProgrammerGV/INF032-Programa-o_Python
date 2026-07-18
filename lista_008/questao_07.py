def converter_maiusculas(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            
        conteudo_maiusculo = conteudo.upper()
        
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(conteudo_maiusculo)
            
        return True
    except FileNotFoundError:
        return False

if __name__ == '__main__':
    entrada = input("Digite o nome do arquivo de entrada: ")
    saida = input("Digite o nome do arquivo de saída: ")
    
    sucesso = converter_maiusculas(entrada, saida)
    if sucesso:
        print(f"Arquivo gerado com sucesso: '{saida}'.")
    else:
        print(f"Arquivo '{entrada}' não encontrado.")
