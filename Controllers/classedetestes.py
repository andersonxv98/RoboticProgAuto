import multiprocessing
import subprocess
from time import sleep
from Controllers.mouseeteclado import MouseETeclado
from Controllers.leitortipoarquivos import LeitorClassTyp


class ClasseDeTestes():
    def __init__(self):
        super(ClasseDeTestes, self).__init__()


    def testar(self):
        print("Hello World!")
        automatic = MouseETeclado()
        ''' classLeitorEscrit = LeitorClassTyp()
        i = 1
        while (i > 0):
            automatic.pressionarEspaco()
            i -= 1
        '''
        """# automatic.escreverAlgoComTeclado("ESCREVA ISso")
        # automatic.movimentarRelativamenteAPosicaoAtual(0,0)

        # testes de leitor e escrita de arquivos
        listaDic = ["Ainda que eu falasse a lingua dos anjos", "Que eu falasse a lingua dos homens",
                    "Sem amor, Eu nada seria", "è só o amor", "è Só o amorm, que conhece  o que é vdd"]

        nome_arquivoTxt = "monteCastelo.txt"
        classLeitorEscrit.lerTxt("dataTeste/leitura.txt")
        classLeitorEscrit.escreverTxt("dataTeste/" + nome_arquivoTxt, listaDic)
        classLeitorEscrit.lerJson("dataTeste/ESPECTROTempesfuria.json")

        dictiona = {"the fool": ["Te bar", "te Exemple", "The mother", "The god", "the son"], "Futas": ["banana",
                                                                                                        "maça", "uva",
                                                                                                        "salada mista"],
                    "Siga": ["em frente", ["olhe para o", "lado", "se liga no mestiço"]]}

        classLeitorEscrit.escreverJson("dataTeste/escreviESaiCorrendo.json", dictiona)

        classLeitorEscrit.lerPdf("dataTeste/TCC_questes.pdf")

        pdfTeste = ["I ve denounced my ethnicity",
                    "In favor of something more kawaii",
                    "Claim the land of the rising Sun",
                    "Where one piece comes from"]

        classLeitorEscrit.escreverPdf("dataTeste/pd_escrito.pdf", "PDF GERADO PELO AUTOMATO HUGO CABRET",
                                      "DESENHA A LUA Ae MANO", pdfTeste)

        classLeitorEscrit.lerCsv("dataTeste/cliente_valor_troco.csv")
        classLeitorEscrit.escreverCsv("dataTeste/novo_escrito.csv", ["teste1", "teste2", "teste3"],
                                      [0, 1, 2, 3, 4, 5, 6, 7, 8])


        pokemon = "pokemon"
        tipo = ["agua", "fogo", "planta", "eletrico", "voador"]
        values_tipo =[["squirlt", "totodile", "pimplup"], ["charizard", "ponyta"], ["chikorita", "treeko"],  ["pikachu"], ["pedgey"] ]

        classLeitorEscrit.lerXml("dataTeste/exemplexaml.xml")

        classLeitorEscrit.escreverXml("dataTeste/gerado.xml", pokemon, tipo, values_tipo)"""

        process = subprocess.run("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe https://www.twitch.tv/")
        # start the process
        automatic.tamanhoDaTela()
        automatic.pocisionarMouse(0,0)

