import PyPDF2

#tramitações no PDF

def pegar_texto(pdf):
    reader = PyPDF2.PdfReader(pdf)
    return reader.pages[0].extract_text()


import requests

#chamada API

def pegar_feriados(ano_corrido):
    url = "https://date.nager.at/api/v3/PublicHolidays/" + ano_corrido + "/BR"

    payload = {}
    headers = {
        'accept': 'application/json',
        'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    dias_feriado = re.findall(r'(?<="date":")(\d{4}-\d{2}-\d{2})*', response.text)
    return dias_feriado

import re

#comparar e separar

def pegar_datas(text):
    anos = set(re.findall(r'\d{4}', text))
    
    feriados = [feriado for ano in anos for feriado in pegar_feriados(ano)]
    
    datas = re.findall(r'\d{4}-\d{2}-\d{2}', text)
    
    encontrados = [data for data in datas if data in feriados]

    print(encontrados)
    return encontrados

#interface
import tkinter

def go():
    root = tkinter.Tk()
    root.title("Titulo da janela")
    root.resizable(True, True)

    texto3 = tkinter.Label(text = "Insira o diretório:")
    texto3.pack()

   
    caixa_texto = tkinter.Entry(root)
    caixa_texto.pack(pady=5)
        
    test = tkinter.Button(root, text="LER PDF")
    test['command'] = lambda: pegar_datas(pegar_texto(caixa_texto.get()))   
    test.pack()


    root.mainloop()
