# 12) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.• Informe ao usuário as quantidades de tinta
# a serem compradas e os respectivos preço sem 3 situações:
# • comprar apenas latas de 18 litros;
# • comprar apenas galões de 3,6 litros;
# • misturar latas e galões, de forma que o preço seja o menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

try:
    area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
    
    # 10% de folga
    area_com_folga = area * 1.10
    
    # Litros necessários
    litros_necessarios = area_com_folga / 6
    
    # Situação 1: Apenas latas de 18 litros
    latas_18 = math.ceil(litros_necessarios / 18)
    preco_latas_18 = latas_18 * 80.00
    
    # Situação 2: Apenas galões de 3,6 litros
    galoes_3_6 = math.ceil(litros_necessarios / 3.6)
    preco_galoes_3_6 = galoes_3_6 * 25.00
    
    # Situação 3: Misturar latas e galões para o menor preço
    latas_mistura = math.floor(litros_necessarios / 18)
    litros_restantes = litros_necessarios - (latas_mistura * 18)
    
    galoes_mistura = math.ceil(litros_restantes / 3.6)
    
    if (galoes_mistura * 25.00) > 80.00:
        latas_mistura += 1
        galoes_mistura = 0
        
    preco_mistura = (latas_mistura * 80.00) + (galoes_mistura * 25.00)
    
    print("\n--- Resultados ---")
    print(f"Área com 10% de folga: {area_com_folga:.2f} m²")
    print(f"Litros de tinta necessários: {litros_necessarios:.2f} L")
    print("\nOpção 1: Comprar apenas latas de 18 litros")
    print(f"Quantidade: {latas_18} latas")
    print(f"Preço total: R$ {preco_latas_18:.2f}")
    
    print("\nOpção 2: Comprar apenas galões de 3,6 litros")
    print(f"Quantidade: {galoes_3_6} galões")
    print(f"Preço total: R$ {preco_galoes_3_6:.2f}")
    
    print("\nOpção 3: Misturar latas e galões para obter o menor preço")
    print(f"Quantidade: {latas_mistura} latas de 18L e {galoes_mistura} galões de 3,6L")
    print(f"Preço total: R$ {preco_mistura:.2f}")

except ValueError:
    print("Entrada inválida. Digite um valor numérico.")
