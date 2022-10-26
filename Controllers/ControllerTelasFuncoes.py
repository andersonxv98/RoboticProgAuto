from Controllers.classedetestes import ClasseDeTestes
from Views.errorwindow import ErrorWindow
from Views.mainwindow import MainWindow


class ControllerTelasFuncoes():
    def __init__(self):
        super(ControllerTelasFuncoes, self).__init__()
        self.window = MainWindow()
        self.errorWindow = ErrorWindow()
        self.tst = ClasseDeTestes()

        #caminho1 = self.window.tabWindow.script.component1.campo.text()
        self.window.tabWindow.script.component1.btn.clicked.connect(lambda: self.tst.adicionarContatosNoGrupoDoZap(self.getTextoOfFront("zap")))


        self.window.tabWindow.script.component2.btn.clicked.connect(lambda: self.tst.adicionarContatosNoGoogleAcounts(self.getTextoOfFront("acounts")))

        # tst.adicionarContatosNoGoogleAcounts("https://contacts.google.com/", "dataTeste/contatos.csv")
        # tst.adicionarContatosNoGrupoDoZap("dataTeste/zapteste.csv")


    def ErrorShow(self):
        self.errorWindow.show()


    def chamarTelPrincipal(self):
        self.window.show()
        return

    def getTextoOfFront(self, func):
        #result = ""
        if func == "zap":
            result = self.window.tabWindow.script.component1.campo.text()
        else:
            result = self.window.tabWindow.script.component2.campo.text()

        return result