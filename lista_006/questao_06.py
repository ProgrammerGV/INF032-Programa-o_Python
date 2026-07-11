# 6.Contagem de palavras: Leia linhas de texto até uma linha vazia. Construa um dicionário de frequências de palavras
# ignorando maiúsculas/minúsculas e pontuações simples (ex.: , . ; : ! ?). Ao final, mostre as 5 palavras mais
# frequentes e suas contagens (se houver menos de 5, mostre todas), e também a quantidade total de palavras diferentes.

frequencias = {}

print("Digite linhas de texto (deixe uma linha vazia para encerrar):")
while True:
    linha = input()
    if not linha:
        break
        
    linha = linha.lower()
    for pontuacao in ",.;:!?":
        linha = linha.replace(pontuacao, " ")
        
    palavras = linha.split()
    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1

print("\n--- Resultados ---")
quantidade_diferentes = len(frequencias)
print(f"Quantidade total de palavras diferentes: {quantidade_diferentes}")

palavras_ordenadas = sorted(frequencias.items(), key=lambda item: item[1], reverse=True)

print("\nPalavras mais frequentes:")
for palavra, contagem in palavras_ordenadas[:5]:
    print(f"{palavra}: {contagem}")
