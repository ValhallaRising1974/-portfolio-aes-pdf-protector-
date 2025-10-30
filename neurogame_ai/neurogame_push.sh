#!/bin/bash

# Configurar identidade do Git
git config --global user.name "Seth Agnar Kristensen"
git config --global user.email "elixirofexistence@proton.me"

# Verificar status do repositório
echo "📂 Verificando alterações..."
git status

# Adicionar todos os arquivos modificados
echo "🌀 Adicionando arquivos..."
git add .

# Criar commit
echo "💬 Realizando commit..."
git commit -m "🌌 Commit inicial do projeto NeuroGame AI por Seth Agnar Kristensen"

# Realizar push
echo "🚀 Enviando ao GitHub..."
git push origin main

# Confirmação final
echo "✅ Upload completo para o repositório NeuroGame-AI!"
