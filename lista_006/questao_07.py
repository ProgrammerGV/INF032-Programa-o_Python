# 7.Dado um pais A, com 5.000.0000 de habitantes e uma taxa de natalidade de 3% ao ano, e um pais B com 7.000.000 de
# habitantes e uma taxa de natalidade de 2% ao ano. calcular e imprimir o tempo necessário para que a população do pais
# A ultrapasse a população do pais B;

pop_a = 5000000
taxa_a = 0.03

pop_b = 7000000
taxa_b = 0.02

anos = 0

while pop_a <= pop_b:
    pop_a += pop_a * taxa_a
    pop_b += pop_b * taxa_b
    anos += 1

print(f"Serão necessários {anos} anos para que a população do país A ultrapasse a população do país B.")
print(f"População do país A: {int(pop_a)}")
print(f"População do país B: {int(pop_b)}")
