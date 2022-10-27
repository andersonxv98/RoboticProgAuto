from PyQt6.QtWidgets import QWidget, QHBoxLayout

from Views.ComponentesView.Tabs.componentepadrao import ComponentePadrao
from Views.ComponentesView.Tabs.editor import Editor


class TabWrite(QWidget):
    def __init__(self):
        super(TabWrite, self).__init__()

        self.laioute = QHBoxLayout()
        self.component1 = ComponentePadrao("Escrever Um tipo de arquivo", "Caminho do arquivo", "", "START")
        self.editor = Editor()
        self.laioute.addWidget(self.component1)
        self.laioute.addWidget(self.editor)
        self.setLayout(self.laioute)