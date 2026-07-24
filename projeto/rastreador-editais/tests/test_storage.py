import pytest 
import json 
from src .storage import carregar_historico ,salvar_historico ,HISTORICO_FILE 

def test_salvar_e_carregar_historico (tmp_path ,mocker ):

    arquivo_temp =tmp_path /"historico.json"
    mocker .patch ('src.storage.HISTORICO_FILE',arquivo_temp )


    dados ={"https://banca.com":["hash1","hash2"]}
    salvar_historico (dados )

    assert arquivo_temp .exists ()


    carregado =carregar_historico ()
    assert carregado ==dados 

def test_carregar_historico_inexistente (tmp_path ,mocker ):
    arquivo_temp =tmp_path /"nao_existe.json"
    mocker .patch ('src.storage.HISTORICO_FILE',arquivo_temp )

    assert carregar_historico ()=={}
