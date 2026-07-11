# 4.Cadastro de alunos: Leia repetidamente nome e três notas de cada aluno (pare quando o nome for FIM). Para cada
# aluno, armazene um dicionário {"nome": ..., "notas": [...]} dentro de uma lista. Ao final, imprima a média de
# cada aluno e um status: "aprovado" se média >= 7, "recuperação" se 5 <= média < 7, e "reprovado" se média < 5.
# Em seguida, mostre a quantidade de alunos em cada status.

alunos = []

while True:
    nome = input("Nome do aluno (FIM para encerrar): ")
    if nome.upper() == "FIM":
        break
    
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota de {nome}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve ser entre 0 e 10.")
            except ValueError:
                print("Nota inválida.")
    
    alunos.append({"nome": nome, "notas": notas})

status_contagem = {"aprovado": 0, "recuperação": 0, "reprovado": 0}

print("\n--- Resultados ---")
for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    
    if media >= 7:
        status = "aprovado"
    elif 5 <= media < 7:
        status = "recuperação"
    else:
        status = "reprovado"
        
    status_contagem[status] += 1
    
    print(f"Aluno: {aluno['nome']} | Média: {media:.2f} | Status: {status}")

print("\n--- Resumo ---")
for status, qtd in status_contagem.items():
    print(f"Alunos em {status}: {qtd}")
