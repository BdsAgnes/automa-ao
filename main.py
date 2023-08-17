import PyPDF2
import os
# mesclar pdf
merger = PyPDF2.PdfMerger()
# listar os arquivos
lista_arquivos = os.listdir("arquivos")
# ordenar a lista
lista_arquivos.sort()
print(lista_arquivos)
''' condição para verificar se os arquivos que
estão dentro pasta é em pdf'''
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
    # adiciona os arquivos dentro do mesclador
        merger.append(f"arquivos/{arquivo}")
# salva o pdf final
merger.write("PDF Final.pdf")