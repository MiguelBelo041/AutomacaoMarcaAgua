@echo off
REM Navega até a pasta do projeto
cd /d C:\Users\Administrativo02\Documents\AutomacaoMarcaDAgua

echo ----------------------------------------
echo Inicializando repositório (caso ainda nao exista)...
git init

echo ----------------------------------------
echo Configurando identidade do Git...
git config user.name "MiguelBelo041"
git config user.email "miguel123belo@gmail.com"

echo ----------------------------------------
echo Adicionando repositório remoto...
git remote remove origin 2>nul
git remote add origin https://github.com/MiguelBelo041/AutomacaoMarcaAgua.git

echo ----------------------------------------
echo Adicionando todos os arquivos...
git add .

echo ----------------------------------------
set /p msg="Digite a mensagem do commit: "
git commit -m "%msg%"

echo ----------------------------------------
echo Configurando branch como main...
git branch -M main

echo ----------------------------------------
echo Enviando arquivos para o GitHub...
git push -u origin main

echo ----------------------------------------
echo Processo concluido!
pause
