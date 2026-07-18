import string
import re
import unicodedata

def estatisticas_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            
        num_caracteres = len(conteudo)
        
        # Separar por espaços, tabs e novas linhas
        palavras = [p for p in re.split(r'\s+', conteudo) if p]
        num_palavras = len(palavras)
        
        # Numero de linhas
        linhas = conteudo.split('\n')
        num_linhas = len(linhas)
        # Ajuste: se o arquivo terminar com nova linha, o último item do split é uma string vazia
        # Isso significa que a última linha foi apenas um '\n', o que pode não contar como nova linha de conteúdo.
        if conteudo.endswith('\n'):
            num_linhas -= 1
        
        if num_caracteres == 0:
            num_linhas = 0
            
        # Contar letras ignorando acentos
        conteudo_limpo = ''.join(c for c in unicodedata.normalize('NFD', conteudo.lower())
                               if unicodedata.category(c) != 'Mn')
                               
        contagem_letras = {letra: 0 for letra in string.ascii_lowercase}
        for char in conteudo_limpo:
            if char in contagem_letras:
                contagem_letras[char] += 1
                
        return num_caracteres, num_linhas, num_palavras, contagem_letras
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    arquivo = input("Digite o nome do arquivo texto: ")
    resultado = estatisticas_arquivo(arquivo)
    
    if resultado is None:
        print(f"Arquivo '{arquivo}' não encontrado.")
    else:
        chars, linhas, palavras, cont_letras = resultado
        print(f"Número de caracteres: {chars}")
        print(f"Número de linhas: {linhas}")
        print(f"Número de palavras: {palavras}")
        print("Frequência de cada letra:")
        for letra, qtd in cont_letras.items():
            if qtd > 0:
                print(f"'{letra}': {qtd}")
