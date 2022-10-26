from PyQt6.QtWidgets import QDialogButtonBox, QMessageBox


class ErrorWindow(QMessageBox):
    def __init__(self):
        super(ErrorWindow, self).__init__()

        self.setWindowTitle("ERRO")
        self.setText("Caminho ou Arquivo não encontrado, verifique se o mesmo Existe OniChan")
        #self.stdBtn = QMessageBox.ButtonRole.AcceptRole
        #self.setStandardButtons(self.stdBtn)
        #self.btn = QDialogButtonBox.ButtonRole.YesRole
