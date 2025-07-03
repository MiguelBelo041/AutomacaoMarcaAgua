# Aplicacao de Marca d'Agua em PDF

## Descricao
Esta aplicacao adiciona marca d'agua aos PDFs de forma simples e rapida, mantendo o texto original do documento.

## Como Usar

### Opcao 1: Executavel (.exe)
1. Execute o arquivo MarcaDagua.exe
2. A aplicacao processara automaticamente todos os PDFs da pasta "PDF sem marca da agua"
3. Os arquivos processados serao salvos na pasta "PDF com marca da agua"

### Opcao 2: Codigo Python
1. Instale as dependencias: pip install -r requirements.txt
2. Execute: python adicionar_marca_dagua.py

## Estrutura de Pastas
```
botPythonMarcaDaAgua
├── MarcaDagua.exe          # Executavel principal
├── marcaAgua.png           # Imagem da marca d'agua
├── criptografar.png        # Imagem adicional (opcional)
├── PDF sem marca da agua   # PDFs originais
└── PDF com marca da agua   # PDFs processados
```

## Funcionalidades
- Marca d'agua: Adiciona marca d'agua com 90% de opacidade
- Texto preservado: Mantem o texto original do PDF
- Processamento rapido: Sem conversao para imagens
- Alta qualidade: Preserva a qualidade original do documento

## Requisitos
- Windows 10/11
- Nao precisa instalar Python (versao executavel)
- Para versao Python: instalar dependencias com pip install -r requirements.txt

## Resultado
Os PDFs processados terao:
- Marca d'agua visivel
- Texto original preservado e copiavel
- Qualidade original mantida
- Processamento rapido

## Importante
- Coloque os PDFs que deseja processar na pasta "PDF sem marca da agua"
- Os arquivos processados aparecerao na pasta "PDF com marca da agua"
- A aplicacao processa automaticamente todos os arquivos .pdf encontrados

## Solucao de Problemas
- Se o executavel nao abrir, verifique se o antivirus nao esta bloqueando
- Certifique-se de que as pastas "PDF sem marca da agua" e "PDF com marca da agua" existem
- Verifique se o arquivo "marcaAgua.png" esta presente no diretorio 
=======
# AutomacaoMarcaAgua
Automação para por marca da agua em documentos .pdf em massa. 
Apenas Substituir o arquivo "marcaAgua.png" para a marca da água que deseja colocar
Criar pastas "PDF com marca da agua" e "PDF sem marca da agua"

