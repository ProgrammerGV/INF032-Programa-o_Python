import requests 
from bs4 import BeautifulSoup 
from typing import List ,Dict 
from .logger import logger 

def buscar_concursos_diretorio (regiao :str ="nacional")->List [Dict [str ,str ]]:
    """
    Busca os concursos abertos no Brasil através do PCI Concursos.
    Regiões suportadas: nacional, sul, sudeste, centro-oeste, nordeste, norte.
    """
    url =f"https://www.pciconcursos.com.br/concursos/{regiao }/"
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    try :
        response =requests .get (url ,headers =headers ,timeout =15 )
        if response .status_code !=200 :
            logger .error (f"Erro ao buscar diretorio: {response .status_code }")
            return []

        soup =BeautifulSoup (response .content ,'html.parser')
        concursos =[]

        for div in soup .find_all ('div',class_ ='ca'):
            titulo_tag =div .find ('a')
            if not titulo_tag :
                continue 

            titulo =titulo_tag .text .strip ()
            link =titulo_tag ['href']

            uf_tag =div .find ('div',class_ ='cc')
            uf =uf_tag .text .strip ()if uf_tag else "BR"


            detalhes_tag =div .find ('div',class_ ='cd')
            if detalhes_tag :
                textos =list (detalhes_tag .stripped_strings )
                vagas_salario =textos [0 ]if len (textos )>0 else ""
                cargo =textos [1 ]if len (textos )>1 else ""
                nivel =textos [2 ]if len (textos )>2 else ""
            else :
                vagas_salario ,cargo ,nivel ="","",""

            data_tag =div .find ('div',class_ ='ce')
            data_limite =data_tag .text .strip ()if data_tag else ""

            concursos .append ({
            'titulo':titulo ,
            'link':link ,
            'uf':uf ,
            'vagas_salario':vagas_salario ,
            'cargo':cargo ,
            'nivel':nivel ,
            'data_limite':data_limite 
            })

        return concursos 

    except Exception as e :
        logger .error (f"Falha de conexao ao buscar diretorio: {e }")
        return []
