import unicodedata 
import hashlib 
from typing import Any 

def normalizar_texto (texto :str )->str :
    """
    Remove acentos, caracteres especiais e converte tudo para minúsculo.
    Isso facilita a busca de palavras-chave.
    """
    if not isinstance (texto ,str ):
        return ""


    texto_min =texto .strip ().lower ()


    texto_norm =unicodedata .normalize ('NFKD',texto_min )
    texto_sem_acento ="".join ([c for c in texto_norm if not unicodedata .combining (c )])

    return texto_sem_acento 

def gerar_hash (conteudo :Any )->str :
    """
    Gera um hash MD5 a partir de uma string ou objeto serializado.
    Utilizado para evitar notificações duplicadas do mesmo conteúdo.
    """
    if not isinstance (conteudo ,str ):
        conteudo =str (conteudo )
    return hashlib .md5 (conteudo .encode ('utf-8')).hexdigest ()
