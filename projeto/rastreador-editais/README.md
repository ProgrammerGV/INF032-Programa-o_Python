# Rastreador de Editais de Concursos

Bot automatizado para monitorar sites de bancas organizadoras de concursos (como IDECAN, FGV, Cebraspe) e buscar atualizações relevantes (editais, convocações, resultados, etc).

## Configuração

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Ajuste o arquivo `config.json` conforme necessário, adicionando ou removendo URLs e palavras-chave.

## Uso

Execute o CLI interativo:
```bash
python main.py
```
O menu oferecerá opções para varredura manual, agendamento de execução e leitura de relatórios.
