from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout

from Views.ComponentesView.tabwidget import TabWidget
from Views.ComponentesView.viewLeituraFront import ViewLeituraFront


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        print("entrou no construturo")
        #ELEMENTOS FILHOS LABEL TITuLO
        self.setWindowTitle("Acho que era algo sobre Pao")
        self.labelTitulo = QLabel("RPA  de GSTI")
        fonte = QFont("Times", 20)
        self.labelTitulo.setFont(fonte)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #ELEMENTOS FILHOS EXTERNOS
        self.LayoutDeCimeEnunciado = QHBoxLayout()
        self.tabWindow = TabWidget()
        self.laiyLeitura = ViewLeituraFront("teste")
        self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.LayoutDeCimeEnunciado.addWidget(self.labelTitulo)

        print("CONSTRUTOR MAINWINDOW")

        #IMPLEMENTAçÃO E ADICçÂO LAYOUTGERALDAJANELA
        self.LayoutGeralDaWindow = QVBoxLayout()
        self.LayoutGeralDaWindow.addLayout(self.LayoutDeCimeEnunciado)
        self.LayoutGeralDaWindow.addWidget(self.tabWindow)
        self.LayoutGeralDaWindow.addLayout(self.laiyLeitura)
        container = QWidget()
        container.setLayout(self.LayoutGeralDaWindow)
        self.setCentralWidget(container)


        print("CONSTRUTOR MAINWINDOW")