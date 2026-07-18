import re

def conta_palavra(nome_arquivo, palavra):
    count = 0
    palavra_lower = palavra.lower()
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read().lower()
            
            # Utilizando expressão regular para encontrar todas as palavras (ignorando pontuações)
            palavras = re.findall(r'\b\w+\b', conteudo)
            count = palavras.count(palavra_lower)
            
        return count
    except FileNotFoundError:
        return -1

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo texto: ")
    palavra = input("Digite a palavra a ser buscada: ")
    
    qtd = conta_palavra(arquivo, palavra)
    if qtd == -1:
        print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        print(f"A palavra '{palavra}' aparece {qtd} vez(es) no arquivo.")
