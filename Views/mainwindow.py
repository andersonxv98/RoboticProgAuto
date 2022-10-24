from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        print("entrou no construturo")
        self.setWindowTitle("Acho que era algo sobre Pao")
        self.labelTitulo = QLabel("RPA  de GSTI")
        fonte = QFont("Times", 20)
        self.labelTitulo.setFont(fonte)
        self.labelTitulo.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.LayoutDeCimeEnunciado = QHBoxLayout()

        self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self.LayoutDeCimeEnunciado.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.LayoutDeCimeEnunciado.addWidget(self.labelTitulo)

        print("CONSTRUTOR MAINWINDOW")

        self.LayoutGeralDaWindow = QVBoxLayout()

        self.LayoutGeralDaWindow.addLayout(self.LayoutDeCimeEnunciado)

        container = QWidget()
        container.setLayout(self.LayoutGeralDaWindow)
        self.setCentralWidget(container)


        print("CONSTRUTOR MAINWINDOW")