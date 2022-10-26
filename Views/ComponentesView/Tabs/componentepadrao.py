from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QWidget


class ComponentePadrao(QWidget):
    def __init__(self, nome_lb_topo, nome_lb, nome_tb,nome_btn_gatilho):
        super(ComponentePadrao, self).__init__()
        self.lsthis = QVBoxLayout()

        fonte = QFont("Times", 20)

        self.btn = QPushButton(nome_btn_gatilho)
        self.label_top = QLabel(nome_lb_topo)
        self.label_top.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.label_top.setFont(fonte)
        self.lb_campo = QLabel(nome_lb)
        self.lb_campo.setFont(fonte)
        self.campo = QLineEdit(nome_tb)


        self.lay1 = QHBoxLayout()
        self.lay1.addWidget(self.lb_campo)
        self.lay1.addWidget(self.campo)



        self.lsthis.addWidget(self.label_top)
        self.lsthis.addLayout(self.lay1)
        self.lsthis.addWidget(self.btn)

        self.setLayout(self.lsthis)