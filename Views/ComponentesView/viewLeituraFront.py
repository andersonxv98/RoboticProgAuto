from PyQt6.QtGui import QWindow, QFont
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout


class ViewLeituraFront(QVBoxLayout):
    def __init__(self, msg):
        super(ViewLeituraFront, self).__init__()
        self.msg = msg
        self.lb = QLabel(msg)
        fonte = fonte = QFont("Times", 20)
        self.lb.setFont(fonte)

        self.addWidget(self.lb)
        self.lb.hide()

    def setMsg(self, msg):
        self.msg = msg
        self.lb.setText(self.msg)

    def show(self):
        self.lb.show()

    def hide(self):
        self.lb.hide()