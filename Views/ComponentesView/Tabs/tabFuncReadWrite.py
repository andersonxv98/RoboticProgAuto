from PyQt6.QtWidgets import QWidget, QHBoxLayout

from Views.ComponentesView.Tabs.componentepadrao import ComponentePadrao


class TabRead(QWidget):
    def __init__(self):
        super(TabRead, self).__init__()
        self.laioute = QHBoxLayout()
        self.component1 = ComponentePadrao("Ler Um arquivo", "Caminho do arquivo", "", "START")

        self.laioute.addWidget(self.component1)

        self.setLayout(self.laioute)
