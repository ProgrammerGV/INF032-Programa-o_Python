from bs4 import BeautifulSoup 
from typing import List ,Dict 

from .utils import normalizar_texto 

def analisar_html (html :str ,palavras_chave :List [str ],url_base :str )->List [Dict [str ,str ]]:
    """
    Analisa o conteúdo HTML e busca por links ou textos que contenham as palavras-chave.
    Retorna uma lista de dicionários contendo os achados.
    """
    resultados =[]

    if not html :
        return resultados 

    soup =BeautifulSoup (html ,'html.parser')


    for tag in soup (['script','style','svg','img','noscript','meta']):
        tag .decompose ()


    links =soup .find_all ('a')

    palavras_norm =[normalizar_texto (p )for p in palavras_chave ]

    for link in links :
        texto_link =link .get_text (strip =True )
        texto_link_norm =normalizar_texto (texto_link )
        href =link .get ('href')


        if not texto_link or not href or href .startswith ('#')or href .startswith ('javascript'):
            continue 


        for p_norm ,p_original in zip (palavras_norm ,palavras_chave ):
            if p_norm in texto_link_norm :

                if href .startswith ('/'):

                    from urllib .parse import urljoin 
                    link_completo =urljoin (url_base ,href )
                elif not href .startswith ('http'):
                    link_completo =url_base .rstrip ('/')+'/'+href 
                else :
                    link_completo =href 

                resultados .append ({
                'Palavra':p_original ,
                'Trecho':texto_link ,
                'URL':link_completo 
                })

                break 

    return resultados 
