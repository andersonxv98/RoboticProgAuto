import sys
import pyautogui as pya
import pynput
from pynput.keyboard import Key

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
        print(pya.size())

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

    def pressionarEspaco(self):
        self.keyboard.press(Key.space)
        print("pressionou espaço")
    def pressionarEnter(self):
        self.keyboard.press(Key.enter)
        print("pressionou enter")

    def pressionarTeclaEspecifica(self, tecla):

        self.keyboard.press(tecla)
        self.keyboard.release(tecla)
        return
    def escreverAlgoComTeclado(self, msg):
        print("digitando: ", msg)
        self.keyboard.type(msg)