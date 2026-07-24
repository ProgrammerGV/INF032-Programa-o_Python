from datetime import datetime 
from typing import Dict ,List ,Any 

from .scraper import obter_html 
from .parser import analisar_html 
from .storage import carregar_config ,carregar_historico ,salvar_historico ,salvar_relatorio_csv 
from .utils import gerar_hash 
from .logger import logger 
from .notifier import notificar_novidades ,notificar_telegram ,avisar 

def executar_varredura ()->None :
    """
    Realiza a varredura em todas as URLs configuradas.
    Consulta o histórico para evitar duplicatas, salva o que for novo
    e notifica o usuário.
    """
    avisar ("\nIniciando varredura...","bold cyan")

    config =carregar_config ()
    urls =config .get ("urls",[])
    keywords =config .get ("keywords",[])
    timeout =config .get ("timeout_seconds",15 )

    if not urls or not keywords :
        avisar ("Nenhuma URL ou palavra-chave configurada em config.json.","bold red")
        return 

    historico =carregar_historico ()
    alertas_gerados =[]

    for url in urls :
        html =obter_html (url ,timeout )
        if not html :
            continue 
        if html :
            api_key =config .get ("ai_api_key","").strip ()

            if api_key :

                from bs4 import BeautifulSoup 
                import requests 
                from io import BytesIO 
                from PyPDF2 import PdfReader 
                from .ai_extractor import analisar_texto_com_ia ,validar_filtros 
                from urllib .parse import urljoin 

                soup =BeautifulSoup (html ,'html.parser')
                texto_puro =soup .get_text (separator =' ',strip =True )


                links_pdf =[]
                for a_tag in soup .find_all ('a',href =True ):
                    href =a_tag ['href']
                    if href .lower ().endswith ('.pdf'):
                        links_pdf .append (urljoin (url ,href ))

                for pdf_url in links_pdf [:2 ]:
                    try :
                        resp =requests .get (pdf_url ,timeout =10 )
                        if resp .status_code ==200 :
                            reader =PdfReader (BytesIO (resp .content ))
                            texto_pdf =" ".join (page .extract_text ()for page in reader .pages if page .extract_text ())
                            texto_puro +=f" [CONTEÚDO DO ARQUIVO PDF ({pdf_url })]: "+texto_pdf 
                    except Exception as e :
                        logger .error (f"Falha ao ler PDF {pdf_url }: {e }")

                extraidos =analisar_texto_com_ia (texto_puro ,config )
                filtrados =validar_filtros (extraidos ,config )

                novos_itens_temp =[]
                for f in filtrados :

                    novos_itens_temp .append ({
                    "Palavra":f"{f .get ('area','Geral')} em {f .get ('cidade','Geral')}",
                    "Trecho":f"[{f .get ('data_prova','Sem data')}] {f .get ('titulo','')}",
                    "URL":url 
                    })
            else :

                novos_itens_temp =analisar_html (html ,keywords ,url )

            resultados =novos_itens_temp 


        if url not in historico :
            historico [url ]=[]

        novos_itens =[]
        for res in resultados :

            chave_item =gerar_hash (f"{res ['Trecho']}_{res ['URL']}")

            if chave_item not in historico [url ]:

                historico [url ].append (chave_item )
                novos_itens .append (res )


                alertas_gerados .append ({
                'Data':datetime .now ().strftime ("%Y-%m-%d %H:%M:%S"),
                'URL':res ['URL'],
                'Palavra':res ['Palavra'],
                'Trecho':res ['Trecho'],
                'Status':'NOVO'
                })

        if novos_itens :
            notificar_novidades (novos_itens ,url )
            notificar_telegram (novos_itens ,config )
        else :
            logger .info (f"Nenhuma novidade encontrada para: {url }")


    salvar_historico (historico )


    if alertas_gerados :
        salvar_relatorio_csv (alertas_gerados )
        avisar (f"Varredura concluida. {len (alertas_gerados )} novos itens salvos.","bold green")
    else :
        avisar ("Varredura concluida. Nenhuma novidade encontrada.","bold green")
