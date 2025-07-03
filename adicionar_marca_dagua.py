import os
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def adicionar_marca_dagua_simples(arquivo_pdf, marca_dagua, pasta_saida):
    """Adiciona marca d'agua simples ao PDF mantendo o texto original"""
    print(f"Adicionando marca d'agua em {os.path.basename(arquivo_pdf)}...")
    
    # Abre o PDF original
    pdf_reader = PdfReader(arquivo_pdf)
    pdf_writer = PdfWriter()
    
    # Carrega e prepara a marca d'agua
    marca_img = Image.open(marca_dagua).convert('RGBA')
    dados = marca_img.getdata()
    novos_dados = []
    for item in dados:
        # Define opacidade de 90%
        novos_dados.append((item[0], item[1], item[2], int(item[3] * 0.9)))
    marca_img.putdata(novos_dados)
    
    # Salva marca d'agua temporariamente
    temp_marca_path = 'temp_marca_agua.png'
    marca_img.save(temp_marca_path, format='PNG')
    
    # Processa cada pagina
    for pagina_num in range(len(pdf_reader.pages)):
        pagina = pdf_reader.pages[pagina_num]
        
        # Obtem as dimensoes da pagina
        largura = float(pagina.mediabox.width)
        altura = float(pagina.mediabox.height)
        
        # Cria um buffer para a marca d'agua
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=(largura, altura))
        
        # Adiciona a marca d'agua
        c.drawImage(temp_marca_path, 0, 0, width=largura, height=altura, preserveAspectRatio=True, mask='auto')
        c.save()
        buffer.seek(0)
        
        # Cria um PDF temporario com a marca d'agua
        marca_pdf = PdfReader(buffer)
        marca_pagina = marca_pdf.pages[0]
        
        # Combina a pagina original com a marca d'agua
        pagina.merge_page(marca_pagina)
        
        # Adiciona a pagina ao PDF de saida
        pdf_writer.add_page(pagina)
        
        buffer.close()
    
    # Remove arquivo temporario da marca d'agua
    os.remove(temp_marca_path)
    
    # Salva o PDF com marca d'agua
    nome_arquivo = os.path.basename(arquivo_pdf)
    caminho_saida = os.path.join(pasta_saida, nome_arquivo)
    
    with open(caminho_saida, 'wb') as arquivo_saida:
        pdf_writer.write(arquivo_saida)

def main():
    pasta_entrada = "PDF sem marca da agua"
    pasta_saida = "PDF com marca da agua"
    marca_dagua = "marcaAgua.png"

    # Verifica se a pasta de saida existe
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Verifica se a marca d'agua existe
    if not os.path.exists(marca_dagua):
        print(f"Erro: Arquivo {marca_dagua} nao encontrado!")
        return

    # Processa todos os PDFs na pasta de entrada
    for arquivo in os.listdir(pasta_entrada):
        if arquivo.lower().endswith('.pdf'):
            caminho_arquivo = os.path.join(pasta_entrada, arquivo)
            print(f"Processando: {arquivo}")
            try:
                adicionar_marca_dagua_simples(caminho_arquivo, marca_dagua, pasta_saida)
                print(f"Concluido: {arquivo}")
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {str(e)}")

if __name__ == "__main__":
    main() 