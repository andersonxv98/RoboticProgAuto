import sys
from PyQt6.QtWidgets import QApplication

from Controllers.ControllerTelasFuncoes import ControllerTelasFuncoes



def main():
    app = QApplication(sys.argv)
    cn =ControllerTelasFuncoes()
    cn.chamarTelPrincipal()
    #cn.ErrorShow()
    app.exec()


main()