# 3.Pesquisa de preços: Leia pares produto/preço positivos e armazene cada item como {"produto": ...,
# "preco": ...} em uma lista, parando quando o preço lido for 0. Calcule e imprima: menor preço, maior preço e preço
# médio. Depois, imprima apenas os produtos com preço acima da média.

produtos = []

while True:
    nome = input("Nome do produto (ou digite 'fim' com preço 0 para sair): ")
    try:
        preco = float(input(f"Preço de {nome} (0 para encerrar): "))
        if preco == 0:
            break
        if preco < 0:
            print("O preço deve ser positivo.")
            continue
        
        produtos.append({"produto": nome, "preco": preco})
    except ValueError:
        print("Preço inválido.")

if produtos:
    precos = [item["preco"] for item in produtos]
    menor_preco = min(precos)
    maior_preco = max(precos)
    preco_medio = sum(precos) / len(precos)
    
    print(f"\nMenor preço: R$ {menor_preco:.2f}")
    print(f"Maior preço: R$ {maior_preco:.2f}")
    print(f"Preço médio: R$ {preco_medio:.2f}")
    
    print("\nProdutos com preço acima da média:")
    for item in produtos:
        if item["preco"] > preco_medio:
            print(f"{item['produto']}: R$ {item['preco']:.2f}")
else:
    print("Nenhum produto foi cadastrado.")
