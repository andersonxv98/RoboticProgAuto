import multiprocessing
import subprocess
from time import sleep

from Controllers.aspectratio import AspectRatio
from Controllers.mouseeteclado import MouseETeclado
from Controllers.leitortipoarquivos import LeitorClassTyp
import maskpass  # importing maskpass library


class ClasseDeTestes():
    def __init__(self):
        super(ClasseDeTestes, self).__init__()
        self.automatic = MouseETeclado()

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


    def adicionarContatosNoGoogleAcounts(self, csvcaminho):
        classLeitorEscrit = LeitorClassTyp()
        matrix = classLeitorEscrit.lerCsv(csvcaminho)
        url = "https://contacts.google.com/"
        process = subprocess.run("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe "+url)
        # start the process
        automatic = MouseETeclado()

        """automatic.tamanhoDaTela()
        automatic.clickarNoCampoDeEmailGoogleAcounts()

        automatic.pressionarEnter()
        automatic.escreverAlgoComTeclado(email)

        automatic.escreverAlgoComTeclado(senha)
        automatic.pressionarEnter()

        #automatic.pocisionarMouse(0, 0)
"""
        espera = 5
        sleep(6) #aguardar 1 minuto para  logar  em google acounts
        print("PRINT MATRIX: ", matrix )
        for contato in matrix:
            arranomtel = []
            for val in contato:
                print("VALOR DENTRO LOOP CONTATO", val)
                arranomtel.append(val)
            automatic.clicarBntNovoContatoGoogleAcounts()
            sleep(espera)
            automatic.digitarCampoNomeETelefoneGoogleAcount(arranomtel[0].__str__(), arranomtel[1].__str__())
            sleep(espera)
            automatic.salvarContatoGoogleAcounts()
            sleep(espera)
            if AspectRatio().aspec_ratio <= 4/3:
                automatic.clickarBtnVoltar()
                sleep(1)

    def adicionarContatosNoGrupoDoZap(self, csvcaminho):
        classLeitorEscrit = LeitorClassTyp()
        matrix = classLeitorEscrit.lerCsv(csvcaminho)
        url = "https://web.whatsapp.com/"
        subprocess.run("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe " + url)
        sleep(15)
        self.automatic.clickarNovoGrupoWtss()
        print(matrix)
        self.automatic.clickPrimeiraVezPesquisar()
        i = 1
        for contato in matrix:
            nome = contato[0]
            self.automatic.digitarContatosParaGrupoZap(nome, i)
            i+=1
            sleep(0.5)
        #self.automatic.clickBtnConfirmarGrupo()
        #sleep(0.5)
        #self.automatic.nomeDoGrupoZap("oFuturoJaComecouETaAutomatizado")


