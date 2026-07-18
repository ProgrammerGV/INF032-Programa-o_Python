Guia da Lista 008

Professor, criei alguns arquivos .txt extras junto com os scripts (teste.txt, teste2.txt, cidades.txt e pessoas.txt). Eu fiz isso para poder ter dados reais para testar se os meus códigos estavam funcionando e lendo os arquivos corretamente, conforme pediam os enunciados.

Os arquivos já estão formatados do jeito que cada questão exige. O cidades.txt, por exemplo, tem os nomes padronizados em 40 caracteres, e o pessoas.txt tem a data de nascimento no final.

Como rodar e testar:
Para testar, você precisa abrir o terminal diretamente dentro dessa pasta "lista_008" (senão o Python não vai encontrar os txt na hora de ler). Aí é só rodar o script normal, por exemplo:

python questao_01.py (ou py questao_01.py)

Quando o script perguntar o nome do arquivo, você pode digitar teste.txt, ou o nome do txt correspondente à questão.

Sobre os códigos:
- Em todas as questões eu usei o "with open" para garantir que os arquivos fossem fechados direitinho.
- Na questão 09, eu usei fatiamento de string (linha[:40]) pra pegar exatamente o nome da cidade.
- Nas questões 10 e 11, acabei usando a biblioteca "re" (regex) pra separar as palavras e ignorar pontuação.
- Na questão 13, eu separei a linha e peguei os 3 últimos valores usando índices negativos (-1, -2, -3) pra puxar o dia, mês e ano, assim não dá erro mesmo que o nome da pessoa seja muito grande.
