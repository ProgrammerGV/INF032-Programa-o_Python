from rich .console import Console 
from rich .panel import Panel 
from rich .table import Table 
from typing import List ,Dict 
import requests 

from .logger import logger 

console =Console ()

def exibir_cabecalho ()->None :
    """Exibe o cabeçalho do programa no terminal."""
    console .print (Panel .fit ("[bold blue]Rastreador de Editais de Concursos[/bold blue]",border_style ="blue"))

def notificar_novidades (novidades :List [Dict [str ,str ]],url :str )->None :
    """
    Exibe um painel de alerta rico informando que novos conteúdos foram encontrados.
    """
    if not novidades :
        return 

    table =Table (show_header =True ,header_style ="bold magenta")
    table .add_column ("Palavra",style ="cyan",width =15 )
    table .add_column ("Trecho",style ="white")

    for item in novidades :
        table .add_row (item ['Palavra'],item ['Trecho'])

    console .print (f"\n[bold green][NOVO][/bold green] Encontrado(s) {len (novidades )} iten(s) em: [underline]{url }[/underline]")
    console .print (table )
    console .print ()

def notificar_telegram (novidades :List [Dict [str ,str ]],config :Dict )->None :
    """Envia notificação dos novos itens achados para o Telegram configurado, de forma individual."""
    token =config .get ("telegram_token","").strip ()
    chat_id =config .get ("telegram_chat_id","").strip ()
    api_key =config .get ("ai_api_key","").strip ()

    if not token or not chat_id or not novidades :
        return 

    url_api =f"https://api.telegram.org/bot{token }/sendMessage"

    gerar_resumo =None 
    if api_key :
        try :
            from .ai_extractor import gerar_resumo_notificacao 
            gerar_resumo =gerar_resumo_notificacao 
        except ImportError :
            pass 

    for item in novidades :
        palavra =item .get ('Palavra','Alerta').replace ('<','&lt;').replace ('>','&gt;')
        trecho =item .get ('Trecho','N/A').replace ('<','&lt;').replace ('>','&gt;')
        link =item .get ('URL','')

        resumo_ia =""
        if gerar_resumo :
            resumo_ia_raw =gerar_resumo (trecho ,config )

            resumo_ia =resumo_ia_raw .replace ('<','&lt;').replace ('>','&gt;')

        html_msg =f"🚨 <b>NOVO ALERTA ENCONTRADO!</b> 🚨\n\n"
        html_msg +=f"🏢 <b>Alvo/Palavra:</b> {palavra }\n"

        trecho_curto =trecho [:250 ]+"..."if len (trecho )>250 else trecho 
        html_msg +=f"📄 <b>Detalhe:</b> <i>{trecho_curto }</i>\n\n"

        if resumo_ia :
            html_msg +=f"🤖 <b>Resumo da IA:</b>\n{resumo_ia }\n\n"

        html_msg +=f"🔗 <a href='{link }'>Ver Detalhes na Página Original</a>"

        payload ={
        "chat_id":chat_id ,
        "text":html_msg ,
        "parse_mode":"HTML",
        "disable_web_page_preview":False 
        }

        try :
            r =requests .post (url_api ,json =payload ,timeout =10 )
            r .raise_for_status ()
            logger .info (f"Notificacao enviada via Telegram com sucesso para o item '{palavra }'")
        except Exception as e :
            logger .error (f"Erro ao enviar notificacao via Telegram: {e }")

def avisar (mensagem :str ,estilo :str ="yellow")->None :
    """Printa uma mensagem simples usando rich."""
    console .print (f"[{estilo }]{mensagem }[/{estilo }]")
