from PyQt6.QtWidgets import  QMessageBox


class ErrorWindow(QMessageBox):
    def __init__(self, titulo, msg):
        super(ErrorWindow, self).__init__()

        self.setWindowTitle(titulo)
        self.setText(msg)
        #self.stdBtn = QMessageBox.ButtonRole.AcceptRole
        #self.setStandardButtons(self.stdBtn)
        #self.btn = QDialogButtonBox.ButtonRole.YesRole
