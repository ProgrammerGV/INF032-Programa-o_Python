import logging 
import os 
from datetime import datetime 
from pathlib import Path 


BASE_DIR =Path (__file__ ).parent .parent 
LOGS_DIR =BASE_DIR /"data"/"logs"


LOGS_DIR .mkdir (parents =True ,exist_ok =True )

def setup_logger ()->logging .Logger :
    """
    Configura o logger central da aplicação.
    O logger escreve num arquivo diário e no console.
    """
    logger =logging .getLogger ("RastreadorEditais")
    logger .setLevel (logging .INFO )


    if not logger .handlers :
        hoje =datetime .now ().strftime ("%Y-%m-%d")
        log_file =LOGS_DIR /f"rastreador_{hoje }.log"


        file_handler =logging .FileHandler (log_file ,encoding ='utf-8')
        file_handler .setLevel (logging .INFO )


        console_handler =logging .StreamHandler ()
        console_handler .setLevel (logging .WARNING )


        formatter =logging .Formatter (
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt ='%Y-%m-%d %H:%M:%S'
        )
        file_handler .setFormatter (formatter )
        console_handler .setFormatter (formatter )

        logger .addHandler (file_handler )
        logger .addHandler (console_handler )

    return logger 


logger =setup_logger ()
