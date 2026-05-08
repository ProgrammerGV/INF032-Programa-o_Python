semana = {}

semana["Segunda-feira"] = ["Programação Python", "Lógica de Programação"]
semana["Terça-feira"] = ["Estrutura de Dados em C", "Desenvolvimento Web"]
semana["Quarta-feira"] = ["Banco de Dados", "Programação Orientada a Objetos (Java)"]
semana["Quinta-feira"] = ["Engenharia de Software", "Sistemas Operacionais"]
semana["Sexta-feira"] = ["Projeto Integrador", "Redes de Computadores"]

semana["Sábado"] = []
semana["Domingo"] = []

print("Cronograma de Aulas da Semana:")
print("-" * 30)

for dia, aulas in semana.items():
    if aulas: 
        print(f"{dia}: {', '.join(aulas)}")
    else:
        print(f"{dia}: Nenhuma aula programada. Dia de descanso!")