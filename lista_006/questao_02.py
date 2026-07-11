# 2.Sistema de votação: Dado um dicionário de candidatos (ex.: {1: "Ana", 2: "Bruno", 3: "Carla"}), leia votos
# inteiros até 0. Conte apenas votos válidos (chaves existentes); contabilize inválidos separadamente. Ao final, mostre:
# total de votos por candidato, percentual de cada um sobre os válidos, total de inválidos e o(s) vencedor(es). Em caso de
# empate, informe quais empataram.

candidatos = {1: "Ana", 2: "Bruno", 3: "Carla"}
votos_validos = {1: 0, 2: 0, 3: 0}
votos_invalidos = 0

print("Candidatos:")
for num, nome in candidatos.items():
    print(f"{num} - {nome}")
print("0 - Encerrar votação")

while True:
    try:
        voto = int(input("Digite o número do candidato (0 para encerrar): "))
        if voto == 0:
            break
        
        if voto in candidatos:
            votos_validos[voto] += 1
        else:
            votos_invalidos += 1
    except ValueError:
        print("Voto inválido. Digite um número inteiro.")
        votos_invalidos += 1

total_validos = sum(votos_validos.values())

print("\n--- Resultado da Votação ---")
for num, nome in candidatos.items():
    qtd_votos = votos_validos[num]
    percentual = (qtd_votos / total_validos * 100) if total_validos > 0 else 0
    print(f"{nome}: {qtd_votos} votos ({percentual:.2f}%)")

print(f"Total de votos inválidos: {votos_invalidos}")

if total_validos > 0:
    max_votos = max(votos_validos.values())
    vencedores = [candidatos[num] for num, votos in votos_validos.items() if votos == max_votos]
    
    if len(vencedores) == 1:
        print(f"Vencedor: {vencedores[0]}")
    else:
        print(f"Empate entre: {', '.join(vencedores)}")
else:
    print("Nenhum voto válido registrado.")
