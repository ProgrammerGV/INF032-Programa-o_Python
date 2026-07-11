# 9.Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores de consumo. para cada
# consumidor, são digitados os seguintes dados:
# a)Numero do consumidor;
# b)Quantidade de kWh consumidos durante o mês;
# c)tipo do consumidor -> 1-residencial, preço em reias de kWh = 0,3 / 2-comercial, preço em reias de kWh = 0,5 /
# 3-industrial, preço em reias de kWh = 0,7. Os dados devem ser lidos ate que seja encontrado um consumidor com
# numero 0(zero). calcular e imprimir: a) o custo total para cada consumidor; b)o total de consumo para os 3(três) tipos
# de consumidor; c)a media de consumo dos tipos 1 e 2.

precos = {1: 0.3, 2: 0.5, 3: 0.7}
consumo_total_por_tipo = {1: 0, 2: 0, 3: 0}
quantidade_consumidores_tipo = {1: 0, 2: 0, 3: 0}

while True:
    try:
        numero = int(input("\nNúmero do consumidor (0 para encerrar): "))
        if numero == 0:
            break
            
        kwh = float(input("Quantidade de kWh consumidos: "))
        if kwh < 0:
            print("Quantidade de kWh não pode ser negativa.")
            continue
            
        tipo = int(input("Tipo do consumidor (1-residencial, 2-comercial, 3-industrial): "))
        if tipo not in [1, 2, 3]:
            print("Tipo inválido.")
            continue
            
        custo = kwh * precos[tipo]
        print(f"Custo total para o consumidor {numero}: R$ {custo:.2f}")
        
        consumo_total_por_tipo[tipo] += kwh
        quantidade_consumidores_tipo[tipo] += 1
        
    except ValueError:
        print("Entrada inválida. Digite valores numéricos corretos.")

print("\n--- Resultados Gerais ---")
print("Total de consumo por tipo:")
print(f"Residencial (1): {consumo_total_por_tipo[1]:.2f} kWh")
print(f"Comercial (2): {consumo_total_por_tipo[2]:.2f} kWh")
print(f"Industrial (3): {consumo_total_por_tipo[3]:.2f} kWh")

soma_kwh_1_2 = consumo_total_por_tipo[1] + consumo_total_por_tipo[2]
qtd_1_2 = quantidade_consumidores_tipo[1] + quantidade_consumidores_tipo[2]

if qtd_1_2 > 0:
    media_1_2 = soma_kwh_1_2 / qtd_1_2
    print(f"Média de consumo dos tipos 1 e 2: {media_1_2:.2f} kWh por consumidor")
else:
    print("Não houve consumidores dos tipos 1 e 2 para calcular a média.")
