agenda = {}

for i in range(5):
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    telefone = input("Digite o telefone: ")
    
    agenda[cpf] = [nome, idade, telefone]
    print("-")

print("\nAgenda Completa:")
for cpf, dados in agenda.items():
    print(f"{cpf}: {dados[0]}-{dados[1]}-{dados[2]}")