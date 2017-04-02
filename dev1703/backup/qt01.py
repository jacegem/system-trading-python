import sys
from PyQt5.QtWidgets import *

from qt.untitled import Ui_Dialog


class XDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = XDialog()
    dlg.show()
    app.exec_()