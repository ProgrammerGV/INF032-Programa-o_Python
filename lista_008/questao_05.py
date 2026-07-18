import string
import unicodedata

def conta_letras_alfabeto(nome_arquivo):
    contagens = {letra: 0 for letra in string.ascii_lowercase}
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read().lower()
            # Removendo acentos
            conteudo = ''.join(c for c in unicodedata.normalize('NFD', conteudo)
                               if unicodedata.category(c) != 'Mn')
            
            for char in conteudo:
                if char in contagens:
                    contagens[char] += 1
        return contagens
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo texto: ")
    resultado = conta_letras_alfabeto(arquivo)
    if resultado is None:
        print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        for letra, qtd in resultado.items():
            print(f"'{letra}': {qtd}")
