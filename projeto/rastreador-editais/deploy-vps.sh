#!/bin/bash
# Script de Deploy Automático - Rastreador de Editais
# Execute este script dentro da sua Máquina Virtual (Ubuntu)

echo "🚀 Iniciando configuração do servidor..."

# 1. Atualizar pacotes
echo "📦 Atualizando pacotes do sistema..."
sudo apt-get update && sudo apt-get upgrade -y

# 2. Instalar Docker e Git
echo "🐳 Instalando Docker e Git..."
sudo apt-get install -y git apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# 3. Adicionar o usuário atual ao grupo docker (evita precisar usar sudo docker)
sudo usermod -aG docker $USER

# 4. Configurar a pasta do projeto
echo "📂 Preparando diretório do projeto..."
cd ~
if [ -d "rastreador-editais" ]; then
    echo "Repositório já existe. Puxando atualizações..."
    cd rastreador-editais
    git pull
else
    echo "⚠️ ATENÇÃO: Substitua o URL abaixo pelo link do seu repositório GitHub!"
    echo "Por enquanto criaremos a pasta vazia..."
    mkdir -p rastreador-editais
    cd rastreador-editais
fi

echo "✅ Instalação concluída!"
echo "➡️ Próximos passos:"
echo "1. Garanta que seus arquivos estão na pasta ~/rastreador-editais (você pode transferir via SCP ou git clone)"
echo "2. Rode o comando: sudo docker compose up -d --build"
