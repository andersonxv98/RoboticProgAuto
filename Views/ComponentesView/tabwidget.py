from PyQt6.QtWidgets import QTabWidget

from Views.ComponentesView.Tabs.tabFuncoesScripts import TabScripts


class TabWidget(QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.script = TabScripts()
        self.addTab(self.script, "SCRIPTS")