
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
        if ".json" in path:
            f = open(path)
            # a dictionary ESCREVA ISso
            data = json.load(f)
            for lk in data:
                print(lk)
                for nb in data[lk]:
                    print(nb)

            f.close()
            return True,
        return False

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
        if ".txt" in path:
            f = open(path, "r")
            msg= []
            for line in f.readlines():
                print(line)
                msg.append(line)
            f.close()
            return True,  msg
        return False, []

    def escreverTxt(self, path, lista_msg):
        with open(path, 'w') as f:
            for msg in lista_msg:
                f.write(msg+"\n")
            f.close()
        return

    def lerCsv(self, path):
        result = []
        with open(path, mode='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            for row in csvFile:
                low = (row[0])
                vector = low.split(";")
                print(vector[0])
                result.append(vector)
                #for cell in row:
                 #   print(cell)
            file.close()

        return result

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

        for food in root_vet:
            print(food)
            for atrib in food:
                print("     ",atrib)
                print("         ",atrib.text)

            #for name in food.findtext("name"):
             #   print(name)

        print(root_vet[0][1].text) # formato de atributos parecido com json
        print(root_vet[0][0].text) #le o texto

        return

    def escreverXml(self, path, root, atrib, values_atribs):
        #formato = {a, b, {c1, c2}, {d1, d2}, {e1, e2}}

        data = ET.Element(root) #criando novo elemento
        for x in range(len(atrib)):
            element1 = ET.SubElement(data, atrib[x])
            for i in range(len(values_atribs[x])):
                element2 = ET.SubElement(element1, values_atribs[x][i])
                element2.text =(values_atribs[x][i])

        b_xml = ET.tostring(data)
                # with operation mode `wb` (write + binary)
        with open(path, "wb") as f:
            f.write(b_xml)

        f.close()
        return