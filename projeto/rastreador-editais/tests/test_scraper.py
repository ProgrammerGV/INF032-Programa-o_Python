import pytest 
import requests 
from requests .exceptions import Timeout ,ConnectionError 
from src .scraper import obter_html 

def test_obter_html_sucesso (mocker ):

    mock_response =mocker .Mock ()
    mock_response .text ="<html>Conteudo esperado</html>"
    mock_response .raise_for_status .return_value =None 


    mocker .patch ('requests.get',return_value =mock_response )

    html =obter_html ("https://site.com")
    assert html =="<html>Conteudo esperado</html>"

def test_obter_html_timeout (mocker ):
    mocker .patch ('requests.get',side_effect =Timeout ("Timeout error"))
    html =obter_html ("https://site.com")
    assert html is None 

def test_obter_html_connection_error (mocker ):
    mocker .patch ('requests.get',side_effect =ConnectionError ("Connection error"))
    html =obter_html ("https://site.com")
    assert html is None 
