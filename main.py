import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.kilo.textChanged.connect(self.kmtomiles)

        self.show()


    def kmtomiles(self):
        self.ui.kilo.setValue(self.ui.kilo*0.621371192)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyDialog()
    sys.exit(app.exec())
