import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        okButton2 = QPushButton("OK2")
        okButton3 = QPushButton("OK3")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        # hbox.addWidget(okButton2)
        # hbox.addWidget(okButton3)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        #vbox.setAlignment(Qt.Qt.AlignCenter)
        vbox.addStretch(0)
        # vbox.addWidget(okButton2)
        # vbox.addWidget(okButton3)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())