import sys
from PyQt6.QtWidgets import QApplication
from Controllers.classedetestes import ClasseDeTestes
from Views.mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window =MainWindow()
    window.show()
    tst = ClasseDeTestes()
    tst.testar()

    app.exec()


main()