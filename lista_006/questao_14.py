# 14) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a. Álcool:
# b. até 20 litros, desconto de 3% por litro
# c. acima de 20 litros, desconto de 5% por litro
# d. Gasolina:
# e. até 20 litros, desconto de 4% por litro
# f. acima de 20 litros, desconto de 6% por litro
# Escreva um programa em python algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
# seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
# da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

try:
    litros = float(input("Digite o número de litros vendidos: "))
    tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()
    
    preco_gasolina = 2.50
    preco_alcool = 1.90
    
    if tipo == 'A':
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
        valor_bruto = litros * preco_alcool
        valor_pagar = valor_bruto - (valor_bruto * desconto)
        tipo_nome = "Álcool"
        
    elif tipo == 'G':
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
        valor_bruto = litros * preco_gasolina
        valor_pagar = valor_bruto - (valor_bruto * desconto)
        tipo_nome = "Gasolina"
    else:
        print("Tipo de combustível inválido.")
        exit()
        
    print(f"\nResumo da Compra:")
    print(f"Combustível: {tipo_nome}")
    print(f"Quantidade: {litros:.2f} L")
    print(f"Desconto aplicado: {desconto * 100:.0f}%")
    print(f"Valor a pagar: R$ {valor_pagar:.2f}")

except ValueError:
    print("Entrada de litros inválida.")
