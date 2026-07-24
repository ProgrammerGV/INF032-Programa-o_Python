import schedule 
import time 
from src .monitor import executar_varredura 
from src .logger import setup_logger 

logger =setup_logger ()

def start ():
    logger .info ("Iniciando loop do monitor 24/7...")
    schedule .every ().day .at ('08:00').do (executar_varredura )

    while True :
        schedule .run_pending ()
        time .sleep (60 )

if __name__ =="__main__":
    start ()
