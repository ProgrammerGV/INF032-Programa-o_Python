import json 
import csv 
import pandas as pd 
from datetime import datetime 
from pathlib import Path 
from typing import Dict ,List ,Any 

from .logger import logger 

BASE_DIR =Path (__file__ ).parent .parent 
DATA_DIR =BASE_DIR /"data"
RELATORIOS_DIR =DATA_DIR /"relatorios"
CONFIG_FILE =BASE_DIR /"config.json"
HISTORICO_FILE =DATA_DIR /"historico.json"


DATA_DIR .mkdir (parents =True ,exist_ok =True )
RELATORIOS_DIR .mkdir (parents =True ,exist_ok =True )

def carregar_config ()->Dict [str ,Any ]:
    """Lê o arquivo config.json."""
    if not CONFIG_FILE .exists ():
        logger .error (f"Arquivo de configuracao nao encontrado: {CONFIG_FILE }")
        return {"urls":[],"keywords":[],"schedule_time":"08:00","timeout_seconds":15 }

    try :
        with open (CONFIG_FILE ,'r',encoding ='utf-8')as f :
            return json .load (f )
    except json .JSONDecodeError as e :
        logger .error (f"Erro ao decodificar config.json: {e }")
        return {"urls":[],"keywords":[],"schedule_time":"08:00","timeout_seconds":15 }

def salvar_config (dados :Dict [str ,Any ])->None :
    """Grava as novas configurações no config.json."""
    try :
        with open (CONFIG_FILE ,'w',encoding ='utf-8')as f :
            json .dump (dados ,f ,indent =2 ,ensure_ascii =False )
    except Exception as e :
        logger .error (f"Erro ao salvar config.json: {e }")

def carregar_historico ()->Dict [str ,List [str ]]:
    """Lê o histórico JSON para checar o que já foi visto."""
    if not HISTORICO_FILE .exists ():
        return {}

    try :
        with open (HISTORICO_FILE ,'r',encoding ='utf-8')as f :
            return json .load (f )
    except json .JSONDecodeError as e :
        logger .error (f"Erro ao decodificar historico.json: {e }")
        return {}

def salvar_historico (historico :Dict [str ,List [str ]])->None :
    """Grava os hashes de conteúdo já vistos no histórico."""
    try :
        with open (HISTORICO_FILE ,'w',encoding ='utf-8')as f :
            json .dump (historico ,f ,indent =4 ,ensure_ascii =False )
    except Exception as e :
        logger .error (f"Erro ao salvar historico.json: {e }")

def salvar_relatorio_csv (dados :List [Dict [str ,str ]])->None :
    """
    Grava os novos alertas de hoje em um CSV na pasta de relatórios.
    """
    if not dados :
        return 

    hoje =datetime .now ().strftime ("%Y-%m-%d")
    arquivo_csv =RELATORIOS_DIR /f"relatorio_{hoje }.csv"

    arquivo_existe =arquivo_csv .exists ()

    colunas =['Hash_ID','Data','URL','Palavra','Trecho','Status']

    try :
        with open (arquivo_csv ,mode ='a',newline ='',encoding ='utf-8')as csvfile :
            writer =csv .DictWriter (csvfile ,fieldnames =colunas )

            if not arquivo_existe :
                writer .writeheader ()

            for linha in dados :
                if 'Hash_ID'not in linha :
                    from .utils import gerar_hash 
                    linha ['Hash_ID']=gerar_hash (linha .get ('Trecho','')+linha .get ('URL',''))
                if 'Status'not in linha :
                    linha ['Status']='Novo'
                linha_filtrada ={k :v for k ,v in linha .items ()if k in colunas }
                writer .writerow (linha_filtrada )
        logger .info (f"Relatorio salvo em: {arquivo_csv }")
    except Exception as e :
        logger .error (f"Erro ao salvar relatorio CSV: {e }")

def ler_relatorios_recentes ()->List [str ]:
    """Lê os últimos relatórios CSV gerados para mostrar no menu CLI."""
    arquivos =list (RELATORIOS_DIR .glob ("*.csv"))
    if not arquivos :
        return []

    arquivos .sort (reverse =True )
    linhas_preview =[]

    try :
        with open (arquivos [0 ],mode ='r',encoding ='utf-8')as csvfile :
            reader =csv .DictReader (csvfile )
            for row in reader :
                linhas_preview .append (f"[{row ['Data']}] {row ['URL']} - {row ['Palavra']}")
    except Exception as e :
        logger .error (f"Erro ao ler relatorios: {e }")

    return linhas_preview 

def carregar_todos_relatorios ()->pd .DataFrame :
    """
    Lê todos os relatórios CSV já gerados e retorna um único DataFrame (para o Streamlit).
    """
    arquivos =list (RELATORIOS_DIR .glob ("*.csv"))
    if not arquivos :
        return pd .DataFrame (columns =['Hash_ID','Data','URL','Palavra','Trecho','Status'])

    dfs =[]
    for arq in arquivos :
        try :
            df =pd .read_csv (arq )
            dfs .append (df )
        except Exception as e :
            logger .error (f"Erro ao ler {arq } com pandas: {e }")

    if dfs :
        df_final =pd .concat (dfs ,ignore_index =True )

        if 'Hash_ID'not in df_final .columns :
            df_final ['Hash_ID']='old_'+df_final .index .astype (str )
        if 'Status'not in df_final .columns :
            df_final ['Status']='Novo'


        df_final =df_final .sort_values (by ='Data',ascending =False )
        return df_final 
    return pd .DataFrame (columns =['Hash_ID','Data','URL','Palavra','Trecho','Status'])

def limpar_todo_historico ()->None :
    """Remove todos os CSVs e o JSON de controle"""
    for f in RELATORIOS_DIR .glob ("*.csv"):
        f .unlink ()
    if HISTORICO_FILE .exists ():
        HISTORICO_FILE .unlink ()

def alterar_status (hash_id :str ,novo_status :str )->None :
    """Busca o item nos CSVs e altera o status dele"""
    arquivos =list (RELATORIOS_DIR .glob ("*.csv"))
    for arq in arquivos :
        df =pd .read_csv (arq )
        if 'Hash_ID'in df .columns :
            mask =df ['Hash_ID']==hash_id 
            if mask .any ():
                df .loc [mask ,'Status']=novo_status 
                df .to_csv (arq ,index =False )
                break 
