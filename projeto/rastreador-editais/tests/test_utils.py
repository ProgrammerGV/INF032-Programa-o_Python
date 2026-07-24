import pytest 
from src .utils import normalizar_texto ,gerar_hash 

def test_normalizar_texto ():
    assert normalizar_texto ("EDITAL DE CONVOCAÇÃO")=="edital de convocacao"
    assert normalizar_texto ("  Resultado Final  ")=="resultado final"
    assert normalizar_texto (None )==""
    assert normalizar_texto ("ação")=="acao"

def test_gerar_hash ():
    texto1 ="um texto qualquer"
    texto2 ="um texto qualquer"
    texto3 ="outro texto"

    assert gerar_hash (texto1 )==gerar_hash (texto2 )
    assert gerar_hash (texto1 )!=gerar_hash (texto3 )
    assert len (gerar_hash (texto1 ))==32 
