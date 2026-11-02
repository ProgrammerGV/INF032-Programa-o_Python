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

## Demonstração pública

O Blueprint `render.yaml` do [portfólio](https://github.com/ProgrammerGV/programmergv.github.io) prepara a hospedagem gratuita do painel web. A demonstração está publicada no serviço existente em https://inf032-programa-o-python.onrender.com/, mantido no plano Free.

Com `RASTREADOR_PUBLIC_DEMO=1`, a aplicação usa duas fontes oficiais fixas, varredura manual com intervalo mínimo de dois minutos, histórico separado em `data/public-demo` e nenhuma credencial de Telegram ou IA. Alterações de configuração são bloqueadas no servidor e os controles correspondentes ficam desabilitados na interface. O histórico da hospedagem gratuita pode reiniciar quando o serviço reiniciar.

A demonstração instala `requirements-demo.txt` e inicia com `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 1 --timeout 120`. O comando de produção não usa o servidor de desenvolvimento com debug. A rota `/healthz` permite verificar a disponibilidade.

Treze testes locais passaram, incluindo configuração fixa sem credenciais, bloqueio das alterações públicas e intervalo entre varreduras.
