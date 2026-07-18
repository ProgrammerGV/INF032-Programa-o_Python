def cadastro_telefones():
    nome_arquivo = 'cadastro.txt'
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        while True:
            telefone = input("Digite o telefone (ou '0' para sair): ")
            if telefone == '0':
                break
            nome = input("Digite o nome: ")
            
            f.write(f"{nome} - {telefone}\n")
    print(f"Cadastro salvo em '{nome_arquivo}'.")

if __name__ == '__main__':
    cadastro_telefones()
