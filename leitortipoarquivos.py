
import xml.etree.ElementTree as ET #element tree xml
from io import StringIO

from PyPDF2 import PdfReader
from fpdf import FPDF
import pandas as pd
import csv
import json

class LeitorClassTyp():
    def __init__(self):
        super().__init__()

    def lerJson(self, path):
        f = open(path)
        # a dictionary ESCREVA ISso
        data = json.load(f)
        for lk in data:
            print(lk)
            for nb in data[lk]:
                print(nb)

        f.close()
        return

    def recursJson(self, data):
        for param in data:
            print(param)
            self.recursJson(param)

        return


    def escreverJson(self, path, dicionario):
        #json_object = json.dumps(dicionario)
        print(dicionario)
        with open(path, "w") as outfile:
            json.dump(dicionario, outfile)
            outfile.close()
        return

    def lerTxt(self, path):
        f = open(path, "r")
        for line in f.readlines():
            print(line)
        f.close()
        return

    def escreverTxt(self, path, lista_msg):
        with open(path, 'w') as f:
            for msg in lista_msg:
                f.write(msg+"\n")
            f.close()
        return

    def lerCsv(self, path):
        df = pd.read_csv(path)
        print(df.to_string())
        for row in df:
            print(df)
            #for cell in row:
             #   print(cell)

        return

    def escreverCsv(self, path, header, data):
        with open(path, 'w', encoding='UTF8') as f:
            writer = csv.writer(f, delimiter=' ')
            # write the header

            writer.writerow(header)

            # write the data
            writer.writerow(data)
        f.close()
        return
    def lerPdf(self, path):
        reader = PdfReader(path)
        #number_of_pages = len(reader.pages)
        textoporpagina = []
        for page in reader.pages:
            text = page.extract_text()
            print(text)
            textoporpagina.append(text)

        print(textoporpagina)
        return

    def escreverPdf(self, path, titulo, subtitulo, lista):
        pdf = FPDF()
        # Add a page
        pdf.add_page()
        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=15)
        # create a cell
        pdf.cell(200, 10, txt=titulo,
                 ln=1, align='C')
        # add another cell
        pdf.cell(200, 10, txt=subtitulo,
                 ln=2, align='C')
        #f = open("myfile.txt", "r")
        # insert the texts in pdf
        for x in lista:
            pdf.cell(200, 10, txt=x, ln=1, align='L')
        # save the pdf with name .pdf
        pdf.output(path)
        return

    def lerXml(self, path):
        arvore = ET.parse(path)
        root_vet = arvore.getroot()

        print(root_vet) #le os elemento
        print(root_vet[0].attrib) #le em formato de atributos parecido com json
        print(root_vet[0][0].text) #le o texto

        return

    def escreverXml(self, path, lista_elementos):
        #formato = {a, b, {c1, c2}, {d1, d2}, {e1, e2}}
        for elemento1 in lista_elementos():
            data = ET.Element(elemento1) #criando novo elemento
            for child in elemento1:
                element1 = ET.SubElement(data, child) #criando subelemento do elemento pai (data)

                for child2 in child:
                    s_elem1 = ET.SubElement(element1, child2) #sub elementos do element1

                    # Adicionando attributos nas tags
                    # `items`
                    for tipo in child2:
                        s_elem1.set('type', tipo)

                    # Adiconando Texto entre elementos
                    # subtag
                        for texto in tipo:
                            s_elem1.text = texto


                    # Converter para xml data to byte object,
                    # stream
            b_xml = ET.tostring(data)

                    # with operation mode `wb` (write + binary)
            with open(path, "ab") as f:
                f.write(b_xml)

            f.close()
        return