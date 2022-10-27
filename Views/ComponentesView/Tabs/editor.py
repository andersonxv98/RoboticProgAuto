
from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton


class Editor(QWidget):

    def __init__(self):
        super(Editor, self).__init__()
        self.setWindowTitle("QTextEdit")
        self.resize(300, 270)

        self.textEdit = QTextEdit()
        self.btnPress1 = QPushButton("Limpar Editor")
        self.btnPress2 = QPushButton("Salvar")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)


    def btnPress1_Clicked(self):
        self.textEdit.setPlainText("")
