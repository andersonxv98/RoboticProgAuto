from PyQt6.QtWidgets import QWidget, QHBoxLayout

from Views.ComponentesView.Tabs.componentepadrao import ComponentePadrao


class TabScripts(QWidget):
    def __init__(self):
        super(TabScripts, self).__init__()
        self.laioute = QHBoxLayout()
        self.component1 = ComponentePadrao("Criar Grupo No Zap", "Caminho do arquivo CSV", "", "START")
        self.component2 = ComponentePadrao("Adicionas  Contatos no GoogleAcounts", "Caminho do arquivo CSV", "", "START")


        self.laioute.addWidget(self.component1)
        self.laioute.addWidget(self.component2)

        self.setLayout(self.laioute)
