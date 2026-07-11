# 11) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
# limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
# adequadas.

try:
    peso = float(input("Digite o peso de peixes (em quilos): "))
    limite = 50.0
    
    if peso > limite:
        excesso = peso - limite
        multa = excesso * 4.00
        print(f"Peso lido: {peso:.2f} kg")
        print(f"Houve um excesso de {excesso:.2f} kg acima do limite de {limite} kg.")
        print(f"O valor da multa a ser paga é de R$ {multa:.2f}.")
    else:
        excesso = 0.0
        multa = 0.0
        print(f"Peso lido: {peso:.2f} kg")
        print("Não houve excesso. Peso dentro do limite estabelecido.")
        print("Multa a pagar: R$ 0.00")
        
except ValueError:
    print("Erro: Digite um valor numérico válido para o peso.")
