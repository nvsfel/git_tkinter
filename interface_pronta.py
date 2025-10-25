



#Fazer chamada api
import requests

url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"

payload = {}
headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


#Ler PDf
import PyPDF2
   
def Get_text_from_PDFfiles_usingPyPDF2(in_PdfFile):  
    reader = PyPDF2.PdfReader(in_PdfFile) 
    print(reader.pages[0].extract_text())


#Interface
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
    test['command'] = lambda: Get_text_from_PDFfiles_usingPyPDF2()
    test.pack()



    root.mainloop()
