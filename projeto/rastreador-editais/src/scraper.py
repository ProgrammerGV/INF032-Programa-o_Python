import requests 
from fake_useragent import UserAgent 
from typing import Optional 
from requests .exceptions import Timeout ,ConnectionError ,HTTPError 

from .logger import logger 

def obter_html (url :str ,timeout :int =15 )->Optional [str ]:
    """
    Realiza a requisição GET para a URL especificada e retorna o HTML.
    Utiliza User-Agent aleatório para evitar bloqueios.
    Retorna None em caso de falha.
    """
    try :
        ua =UserAgent ()
        headers ={'User-Agent':ua .random }

        logger .info (f"Buscando URL: {url }")

        resposta =requests .get (url ,headers =headers ,timeout =timeout )
        resposta .raise_for_status ()

        return resposta .text 

    except HTTPError as e :
        logger .error (f"Erro HTTP ao acessar {url }: {e }")
    except ConnectionError as e :
        logger .error (f"Erro de Conexao ao acessar {url }: {e }")
    except Timeout as e :
        logger .error (f"Timeout ao acessar {url } (Tempo maximo: {timeout }s): {e }")
    except Exception as e :
        logger .error (f"Erro inesperado ao acessar {url }: {e }")

    return None 
