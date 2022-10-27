from PyQt6.QtWidgets import QTabWidget

from Views.ComponentesView.Tabs.tabFuncReadWrite import TabRead
from Views.ComponentesView.Tabs.tabFuncoesScripts import TabScripts
from Views.ComponentesView.Tabs.tabWrite import TabWrite


class TabWidget(QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.script = TabScripts()
        self.read = TabRead()
        self.write = TabWrite()
        self.addTab(self.script, "SCRIPTS")
        self.addTab(self.read, "Leitura")
        self.addTab(self.write, "Escrita")