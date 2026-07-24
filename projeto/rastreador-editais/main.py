import time 
import sys 
import schedule 
from rich .console import Console 
from rich .panel import Panel 
from rich .prompt import Prompt 

from src .monitor import executar_varredura 
from src .storage import ler_relatorios_recentes ,carregar_config 
from src .notifier import avisar 

console =Console ()

def exibir_menu ()->None :
    """Mostra as opções do menu principal."""
    console .print ("\n")
    console .print (Panel .fit ("[bold blue]Rastreador de Editais de Concursos[/bold blue]"))
    console .print ("[1] Executar rastreamento agora")
    console .print ("[2] Iniciar monitoramento agendado (em background)")
    console .print ("[3] Ver relatorios recentes")
    console .print ("[4] Sair")
    console .print ()

def listar_relatorios ()->None :
    """Imprime os relatórios mais recentes gerados na tela."""
    linhas =ler_relatorios_recentes ()
    if not linhas :
        avisar ("Nenhum relatorio encontrado.","yellow")
        return 

    console .print (Panel ("\n".join (linhas [:15 ]),title ="[bold green]Ultimos Registros Encontrados[/bold green]"))

def loop_agendamento ()->None :
    """Inicia o laço de repetição do schedule, travando a execução (modo background no terminal)."""
    config =carregar_config ()
    hora =config .get ("schedule_time","08:00")

    avisar (f"Iniciando agendamento diario para as {hora }. Pressione Ctrl+C para cancelar.","bold green")

    schedule .every ().day .at (hora ).do (executar_varredura )

    try :
        while True :
            schedule .run_pending ()
            time .sleep (60 )
    except KeyboardInterrupt :
        avisar ("\nAgendamento cancelado pelo usuario.","bold yellow")

def main ()->None :
    """Ponto de entrada do sistema. Controla o CLI interativo."""
    while True :
        try :
            exibir_menu ()
            opcao =Prompt .ask ("Escolha uma opcao",choices =["1","2","3","4"])

            if opcao =="1":
                executar_varredura ()
            elif opcao =="2":
                loop_agendamento ()
            elif opcao =="3":
                listar_relatorios ()
            elif opcao =="4":
                avisar ("Saindo do sistema. Ate logo!","bold cyan")
                sys .exit (0 )
        except KeyboardInterrupt :
            avisar ("\nOperacao abortada. Saindo...","bold yellow")
            sys .exit (0 )
        except Exception as e :
            avisar (f"\nErro inesperado: {e }","bold red")

if __name__ =="__main__":
    main ()
