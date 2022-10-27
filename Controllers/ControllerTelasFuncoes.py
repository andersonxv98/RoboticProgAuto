from Controllers.classedetestes import ClasseDeTestes
from Views.ComponentesView.viewLeituraFront import ViewLeituraFront
from Views.errorwindow import ErrorWindow
from Views.mainwindow import MainWindow


class ControllerTelasFuncoes():
    def __init__(self):
        super(ControllerTelasFuncoes, self).__init__()
        self.window = MainWindow()
        #self.errorWindow = ErrorWindow()
        self.tst = ClasseDeTestes()

        #caminho1 = self.window.tabWindow.script.component1.campo.text()
        self.window.tabWindow.script.component1.btn.clicked.connect(lambda: self.tst.adicionarContatosNoGrupoDoZap(self.getTextoOfFront("zap")))
        self.window.tabWindow.script.component2.btn.clicked.connect(lambda: self.tst.adicionarContatosNoGoogleAcounts(self.getTextoOfFront("acounts")))
        self.window.tabWindow.read.component1.btn.clicked.connect(lambda: self.leitura(self.getTextoOfFront("leitura")))
        self.window.tabWindow.write.editor.btnPress2.clicked.connect(lambda: self.escrita(self.getTextoOfFront("escrita"), self.getTextoOfFront("editor")))

        # tst.adicionarContatosNoGoogleAcounts("https://contacts.google.com/", "dataTeste/contatos.csv")
        # tst.adicionarContatosNoGrupoDoZap("dataTeste/zapteste.csv")


    """def ErrorShow(self):
        self.errorWindow.show()
"""

    def chamarTelPrincipal(self):
        self.window.show()
        return

    def getTextoOfFront(self, func):
        result = self.window.tabWindow.script.component2.campo.text()
        if func == "zap":
            result = self.window.tabWindow.script.component1.campo.text()
        elif func == "leitura":
            result = self.window.tabWindow.read.component1.campo.text()
        elif func == "escrita":
            result = self.window.tabWindow.write.component1.campo.text()
        elif func == "editor":
            result = self.window.tabWindow.write.editor.textEdit.toPlainText()

        return result

    def leitura(self, path):
       msg = self.tst.leitura(path)
       v = self.window.laiyLeitura
       v.setMsg(msg)
       v.show()
       return

    def escrita(self, path, texto):
        self.tst.escrita(path, texto)
        return