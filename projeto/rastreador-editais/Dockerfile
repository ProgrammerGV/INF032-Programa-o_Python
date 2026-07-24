FROM python:3.12-slim

WORKDIR /app

# Instala dependências do sistema necessárias para compilar pacotes
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código do projeto
COPY . .

# Comando default (pode ser sobrescrito pelo docker-compose)
CMD ["python", "main.py"]
