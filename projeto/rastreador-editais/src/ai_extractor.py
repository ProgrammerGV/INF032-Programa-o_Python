import json 
from typing import List ,Dict 
import google .generativeai as genai 
from .logger import logger 

def analisar_texto_com_ia (texto :str ,config :Dict )->List [Dict ]:
    """
    Envia o texto para o Google Gemini extrair:
    - Titulo (Nome do concurso/edital)
    - Cidade/Estado
    - Area (Saúde, TI, Educação, etc)
    - Data_Prova
    """
    api_key =config .get ("ai_api_key","").strip ()

    if not api_key :
        return []

    try :
        genai .configure (api_key =api_key )

        model =genai .GenerativeModel ('gemini-1.5-flash')

        prompt =f"""
Você é um assistente especialista em analisar textos de concursos públicos e licitações.
Leia o texto abaixo, que foi extraído de uma página web confusa, e extraia os concursos, editais, convocações ou resultados mencionados.

Retorne APENAS um array JSON válido contendo objetos com os seguintes campos (sem nenhum markdown extra, apenas o array raw):
[
  {{
    "titulo": "Nome resumido do edital/concurso",
    "cidade": "Cidade ou Estado (se não souber, retorne 'N/A')",
    "area": "A área de atuação (ex: Saúde, TI, Educação, Policial, Geral, etc. Se não souber, retorne 'N/A')",
    "data_prova": "Data da prova ou inscrições (se não souber, retorne 'N/A')"
  }}
]

Se o texto não contiver nenhum concurso válido, retorne um array vazio [].

TEXTO:
{texto [:5000 ]} # Limita a 5000 chars para não estourar o limite
"""
        response =model .generate_content (prompt )

        raw_text =response .text .replace ("```json","").replace ("```","").strip ()

        try :
            resultados =json .loads (raw_text )
            if isinstance (resultados ,list ):
                return resultados 
            return []
        except json .JSONDecodeError :
            logger .error (f"Erro ao parsear resposta da IA como JSON: {raw_text }")
            return []

    except Exception as e :
        logger .error (f"Erro na comunicação com a API do Gemini: {e }")
        return []

def validar_filtros (concursos_extraidos :List [Dict ],config :Dict )->List [Dict ]:
    """Filtra os concursos que a IA achou batendo com as cidades e areas do usuario"""
    cidades_desejadas =[c .lower ()for c in config .get ("filtros_cidades",[])]
    areas_desejadas =[a .lower ()for a in config .get ("filtros_areas",[])]


    if not cidades_desejadas and not areas_desejadas :
        return concursos_extraidos 

    aprovados =[]

    for c in concursos_extraidos :
        cidade_achada =c .get ("cidade","").lower ()
        area_achada =c .get ("area","").lower ()

        cidade_ok =False 
        area_ok =False 

        if not cidades_desejadas or cidade_achada =='n/a'or any (cid in cidade_achada for cid in cidades_desejadas ):
            cidade_ok =True 

        if not areas_desejadas or area_achada =='n/a'or any (area in area_achada for area in areas_desejadas ):
            area_ok =True 

        if cidade_ok and area_ok :
            aprovados .append (c )

    return aprovados 

def gerar_resumo_notificacao (texto :str ,config :Dict )->str :
    """
    Usa o Gemini para gerar uma frase curta e engajadora para o Telegram,
    focada em destacar a oportunidade (vagas, salários, órgão).
    """
    api_key =config .get ("ai_api_key","").strip ()

    if not api_key :
        return ""

    try :
        genai .configure (api_key =api_key )
        model =genai .GenerativeModel ('gemini-1.5-flash')

        prompt =f"""
Você é um assistente de marketing especializado em concursos públicos.
Leia o trecho abaixo referente a um edital ou concurso encontrado.
Escreva APENAS UMA frase curta, vibrante e direta (máximo 2 linhas) para enviar no Telegram.
O foco deve ser convencer o candidato de que é uma boa oportunidade (destaque número de vagas, salários altos ou o peso do órgão, se mencionado).
NÃO use saudações. VÁ DIRETO AO PONTO. Pode usar no máximo 1 ou 2 emojis na frase.

TRECHO DO CONCURSO:
{texto [:2000 ]}
"""
        response =model .generate_content (prompt )
        return response .text .strip ()
    except Exception as e :
        logger .error (f"Erro ao gerar resumo de notificacao com IA: {e }")
        return ""
