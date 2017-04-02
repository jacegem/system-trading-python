import sys
from PyQt5.QtWidgets import *

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)
        self.statusBar().showMessage('Ready')

    def changeStatusBar(self, msg):
        self.statusBar().showMessage(msg)

class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)

if __name__ == "__main__":
    app = QApplication([])
    dialog = MyMainWindow()
    dialog.show()
    sys.exit(app.exec_())
