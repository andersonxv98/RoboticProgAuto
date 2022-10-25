import sys
from PyQt6.QtWidgets import QApplication
from Controllers.classedetestes import ClasseDeTestes
from Views.mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    tst = ClasseDeTestes()
    #tst.adicionarContatosNoGoogleAcounts("https://contacts.google.com/", "dataTeste/contatos.csv")
    tst.adicionarContatosNoGrupoDoZap("dataTeste/zapteste.csv")
    app.exec()


main()