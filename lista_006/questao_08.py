# 8.Chico tem 1.50m e cresce 2 centímetros por ano, enquanto Juca tem 1.10m e cresce 3 cm por ano. construir um
# programa que calcule e imprima quantos anos serão necessários para Juca seja maior que Chico;

altura_chico = 1.50
crescimento_chico = 0.02

altura_juca = 1.10
crescimento_juca = 0.03

anos = 0

while altura_juca <= altura_chico:
    altura_chico += crescimento_chico
    altura_juca += crescimento_juca
    anos += 1

print(f"Serão necessários {anos} anos para que Juca seja maior que Chico.")
print(f"Altura final de Juca: {altura_juca:.2f}m")
print(f"Altura final de Chico: {altura_chico:.2f}m")
