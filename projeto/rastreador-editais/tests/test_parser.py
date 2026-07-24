import pytest 
from src .parser import analisar_html 

@pytest .fixture 
def html_mock ():
    return """
    <html>
        <body>
            <a href="/edital_1.pdf">Edital de Abertura</a>
            <a href="/resultado.pdf">RESULTADO PRELIMINAR</a>
            <a href="https://outrosite.com/aviso">Aviso Importante</a>
            <a href="javascript:void(0)">Link Inutil</a>
            <script>console.log('edital secreto')</script>
        </body>
    </html>
    """

def test_analisar_html_encontra_palavras (html_mock ):
    palavras =["edital","resultado"]
    url_base ="https://banca.com"

    resultados =analisar_html (html_mock ,palavras ,url_base )

    assert len (resultados )==2 


    assert resultados [0 ]['Palavra']=="edital"
    assert "Edital de Abertura"in resultados [0 ]['Trecho']
    assert resultados [0 ]['URL']=="https://banca.com/edital_1.pdf"


    assert resultados [1 ]['Palavra']=="resultado"
    assert resultados [1 ]['URL']=="https://banca.com/resultado.pdf"

def test_analisar_html_ignora_scripts (html_mock ):
    palavras =["secreto"]
    url_base ="https://banca.com"

    resultados =analisar_html (html_mock ,palavras ,url_base )


    assert len (resultados )==0 

def test_analisar_html_sem_html ():
    assert analisar_html ("",["edital"],"url")==[]
    assert analisar_html (None ,["edital"],"url")==[]
