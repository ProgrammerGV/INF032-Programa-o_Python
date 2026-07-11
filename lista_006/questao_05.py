# 5.Controle de estoque: Comece com um dicionário de estoque (ex.: {"teclado": 12, "mouse": 5, "monitor":
# 2}). Leia pedidos no formato produto e qtd até produto == "FIM".
# Se houver quantidade suficiente, desconte do estoque; caso contrário, registre o pedido em uma lista pendentes (cada
# item um dicionário com {"produto": ..., "qtd": ...}). Ao final, mostre o estoque atualizado e a lista de
# pendentes.

estoque = {"teclado": 12, "mouse": 5, "monitor": 2}
pendentes = []

while True:
    produto = input("Digite o nome do produto (FIM para encerrar): ").lower()
    if produto == "fim":
        break
    
    if produto not in estoque:
        print("Produto não existe no estoque.")
        continue
        
    try:
        qtd = int(input(f"Quantidade desejada de {produto}: "))
        if qtd <= 0:
            print("Quantidade deve ser maior que zero.")
            continue
            
        if estoque[produto] >= qtd:
            estoque[produto] -= qtd
            print(f"Pedido atendido! Restam {estoque[produto]} de {produto} no estoque.")
        else:
            print(f"Estoque insuficiente. Quantidade disponível: {estoque[produto]}. Pedido adicionado aos pendentes.")
            pendentes.append({"produto": produto, "qtd": qtd})
            
    except ValueError:
        print("Quantidade inválida.")

print("\n--- Estoque Atualizado ---")
for prod, qtd in estoque.items():
    print(f"{prod}: {qtd}")

print("\n--- Lista de Pendentes ---")
if pendentes:
    for item in pendentes:
        print(f"Produto: {item['produto']}, Quantidade: {item['qtd']}")
else:
    print("Não há pedidos pendentes.")
