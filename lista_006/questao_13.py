# 13) O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
# Até 5 Kg Acima de 5 Kg
# File Duplo R$ 4,90 por Kg R$ 5,80 por Kg
# Alcatra R$ 5,90 por Kg R$ 6,80 por Kg
# Picanha R$ 6,90 por Kg R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
# as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a
# pagar.

print("--- Carnes ---")
print("1 - File Duplo")
print("2 - Alcatra")
print("3 - Picanha")

try:
    tipo = int(input("Escolha o tipo de carne (1, 2 ou 3): "))
    if tipo not in [1, 2, 3]:
        print("Opção inválida.")
        exit()
        
    quantidade = float(input("Digite a quantidade em Kg: "))
    cartao = input("A compra será feita no cartão Tabajara? (S/N): ").strip().upper()
    
    if tipo == 1:
        nome_carne = "File Duplo"
        if quantidade <= 5:
            preco_kg = 4.90
        else:
            preco_kg = 5.80
    elif tipo == 2:
        nome_carne = "Alcatra"
        if quantidade <= 5:
            preco_kg = 5.90
        else:
            preco_kg = 6.80
    elif tipo == 3:
        nome_carne = "Picanha"
        if quantidade <= 5:
            preco_kg = 6.90
        else:
            preco_kg = 7.80
            
    preco_total = quantidade * preco_kg
    
    if cartao == 'S':
        tipo_pagamento = "Cartão Tabajara"
        desconto = preco_total * 0.05
    else:
        tipo_pagamento = "Outro"
        desconto = 0.0
        
    valor_pagar = preco_total - desconto
    
    print("\n--- CUPOM FISCAL ---")
    print(f"Tipo de carne: {nome_carne}")
    print(f"Quantidade: {quantidade:.2f} Kg")
    print(f"Preço total: R$ {preco_total:.2f}")
    print(f"Tipo de pagamento: {tipo_pagamento}")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor a pagar: R$ {valor_pagar:.2f}")
    print("--------------------")

except ValueError:
    print("Entrada inválida.")
