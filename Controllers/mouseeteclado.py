import sys
from time import sleep

import pyautogui as pya
import pynput
from pynput.keyboard import Key

from Controllers.aspectratio import AspectRatio


class MouseETeclado():
    def __init__(self):
        super().__init__()
        self.mouse = pynput.mouse
        self.keyboard = pynput.keyboard.Controller()
        self.i = 1

    def lerPosicaoMouse(self):
        print("Posição do Mouse: ", self.mouse.Controller().position)
        return
    def tamanhoDaTela(self):
        pos = (pya.size())
        x = pos.width
        y = pos.height

        return x,y
        # (0, 0, 800, 600)
    def pocisionarMouse(self, x, y):

        self.mouse.Controller().position = (x, y)
        return

    def movimentarRelativamenteAPosicaoAtual(self, x, y):
        self.mouse.Controller().move(dx=x, dy=y)
        return

    def click(self):
        self.mouse.Controller().press(self.mouse.Button.left)
        self.mouse.Controller().release(self.mouse.Button.left)
        print("Clickou: ", self.i)
        self.i += 1
        return

    def doubleClick(self):
        self.mouse.Controller().click(self.mouse.Button.left, 2)
        print("DOUBLE CLCIK")
        return

    def pressionarEspaco(self):
        self.keyboard.press(Key.space)
        print("pressionou espaço")
        return
    def pressionarEnter(self):
        self.keyboard.press(Key.enter)
        print("pressionou enter")
        return
    def pressionarTeclaEspecifica(self, tecla):

        self.keyboard.press(tecla)
        self.keyboard.release(tecla)
        return
    def escreverAlgoComTeclado(self, msg):
        print("digitando: ", msg)
        self.keyboard.type(msg)
        return

    def posicionarMouseNaBarraDeEndereco(self):
        x,y =self.tamanhoDaTela()
        posiXEndereco = x * 0.1171303074670571
        posiYEndereco = y * 0.0690104166666667
        self.pocisionarMouse(posiXEndereco, posiYEndereco)
        return

    def fazerBuscaNaBarraDeEndereco(self, url):
        sleep(3)
        self.posicionarMouseNaBarraDeEndereco()
        self.doubleClick()
        self.escreverAlgoComTeclado(url)
        self.pressionarEnter()
        return
    def clickarNoCampoDeEmailGoogleAcounts(self):

        x, y =self.tamanhoDaTela()
        posicaoX = x * 0.369692532942899
        posicaoY = y * 0.4622395833333333
        sleep(1)
        self.doubleClick()
        self.pocisionarMouse(posicaoX, posicaoY)
        return
    def clicarBntNovoContatoGoogleAcounts(self):
        #posicaoX= x * 0.0768667642752562
        #posicaoY = y * 0.23046875
        posicaoX,posicaoY = AspectRatio().posBntCriarContato()
        self.pocisionarMouse(posicaoX, posicaoY)
        self.click()
        sleep(1)
        posicaoX, posicaoY = AspectRatio().posBtnCriarContato2()
        self.pocisionarMouse(posicaoX, posicaoY)
        self.click()
        return

    def digitarCampoNomeETelefoneGoogleAcount(self, nome, telefone):
        asp = AspectRatio()
        x, y = asp.posCampoNome()
        #posicaoX = x * 0.3023426061493411
        #posicaoY = y * 0.48828125

        self.pocisionarMouse(x, y)
        self.click()
        self.escreverAlgoComTeclado(nome)
        sleep(1)

        if asp.whidth < 1024:
            print("reconheceu tamanho menor q 1024")

            self.mouse.Controller().scroll(0,-10)
            sleep(1)


        posicaoX, posicaoY = asp.posCampoTel()

        self.pocisionarMouse(posicaoX, posicaoY)
        self.click()
        sleep(1)
        self.escreverAlgoComTeclado(telefone)
        return
    def salvarContatoGoogleAcounts(self):
        x,y = AspectRatio().posSalvar()
        print("entrou em salvarContato GOOGLE ACOUTNS")
        if AspectRatio().whidth < 1024:
            self.mouse.Controller().scroll(0,10)


        sleep(2)
        self.pocisionarMouse(x, y)
        self.click()
        return

    def clickarBtnVoltar(self):
        posx, posy = AspectRatio().posBtnVoltar()
        sleep(1)
        print("X, Y : "+ posx.__str__()+"  "+  posy.__str__())
        sleep(2)
        self.pocisionarMouse(posx,posy)
        self.click()
        return

    def clickarNovoGrupoWtss(self):
        x, y = AspectRatio().posBtnNovaConverssaZap()
        sleep(1)
        self.pocisionarMouse(x,y)
        sleep(1)
        self.click()
        self.criarNovoGrupoZap()
        return

    def criarNovoGrupoZap(self):
        x, y = AspectRatio().posBtnNovoGrupoZap()
        sleep(1)
        self.pocisionarMouse(x, y)
        sleep(1)
        self.click()
        return

    def clickPrimeiraVezPesquisar(self):
        x, y = AspectRatio().posNCZgrupoContato()
        sleep(1)
        self.pocisionarMouse(x, y)
        sleep(1)
        self.click()
        return
    def digitarContatosParaGrupoZap(self, nomecompleto, n_contato):
        self.escreverAlgoComTeclado(nomecompleto)
        sleep(1)


        ratio = AspectRatio()

        ratio.changeMid(n_contato)
        ratio.changeMax(n_contato)
        ratio.chanceMax1366(n_contato)
        x, y = ratio.posContatoZap()
        sleep(1)
        self.pocisionarMouse(x, y)
        sleep(1)
        self.click()
        return
    def clickBtnConfirmarGrupo(self):
        x, y = AspectRatio().posBtnConfirmarZap()
        sleep(1)
        self.pocisionarMouse(x, y)
        sleep(1)
        self.click()
        return

    def nomeDoGrupoZap(self, n_grupo):
        self.escreverAlgoComTeclado(n_grupo)
        sleep(0.5)
        self.pressionarEnter()
        sleep(1)
        self.confirmarConvitesZap()
        return

    def confirmarConvitesZap(self):
        x, y = AspectRatio().confirmarConvite()
        sleep(1)
        self.pocisionarMouse(x, y)
        sleep(1)
        self.click()
        return