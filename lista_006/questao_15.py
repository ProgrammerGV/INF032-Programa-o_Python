# 15) Agenda de tarefas (CLI): Mantenha uma lista de dicionários de tarefas, cada um com {"titulo": ...,
# "prioridade": 1-5, "status": "aberta"|"concluida"}. Em um laço, aceite comandos:
# ● ADD: ler titulo e prioridade e incluir tarefa com status "aberta".
# ● DONE: ler titulo e marcar a tarefa correspondente como "concluida" (se existir).
# ● LIST: imprimir as tarefas ordenadas por prioridade (menor número = maior prioridade), mostrando título,
# prioridade e status; se houver um texto FILTRO=aberta ou FILTRO=concluida, liste apenas as do filtro.
# ● EXIT: encerrar o programa.

tarefas = []

print("--- Agenda de Tarefas ---")
print("Comandos: ADD, DONE, LIST, EXIT")

while True:
    comando_input = input("\nDigite um comando: ").strip().split(maxsplit=1)
    
    if not comando_input:
        continue
        
    comando = comando_input[0].upper()
    
    if comando == "ADD":
        titulo = input("Título da tarefa: ").strip()
        try:
            prioridade = int(input("Prioridade (1-5, sendo 1 a mais alta): "))
            if 1 <= prioridade <= 5:
                tarefas.append({"titulo": titulo, "prioridade": prioridade, "status": "aberta"})
                print("Tarefa adicionada com sucesso.")
            else:
                print("Prioridade deve ser entre 1 e 5.")
        except ValueError:
            print("Prioridade inválida.")
            
    elif comando == "DONE":
        titulo = input("Título da tarefa a concluir: ").strip()
        encontrada = False
        for tarefa in tarefas:
            if tarefa["titulo"] == titulo:
                tarefa["status"] = "concluida"
                encontrada = True
                print("Tarefa marcada como concluída.")
                break
        if not encontrada:
            print("Tarefa não encontrada.")
            
    elif comando == "LIST":
        filtro = None
        if len(comando_input) > 1:
            arg = comando_input[1].upper()
            if arg == "FILTRO=ABERTA":
                filtro = "aberta"
            elif arg == "FILTRO=CONCLUIDA":
                filtro = "concluida"
                
        tarefas_ordenadas = sorted(tarefas, key=lambda x: x["prioridade"])
        
        print("\n--- Lista de Tarefas ---")
        for tarefa in tarefas_ordenadas:
            if filtro and tarefa["status"] != filtro:
                continue
            print(f"[{tarefa['status'].upper()}] Prioridade: {tarefa['prioridade']} | Título: {tarefa['titulo']}")
            
    elif comando == "EXIT":
        print("Encerrando a agenda de tarefas...")
        break
        
    else:
        print("Comando inválido.")
