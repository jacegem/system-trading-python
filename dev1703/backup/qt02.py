
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import logging

class QPlainTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)

class MyDialog(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)

        # 레이블,Edit,버튼 컨트롤
        lblName = QLabel("Name")
        editName = QLineEdit()
        btnOk = QPushButton("OK")
        logTextBox = QPlainTextEditLogger(self)
        # You can format what is printed to text box
        logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)
        testButton = QPushButton(self)
        testButton.setText('Test Me')
        testButton.clicked.connect(self.test)

        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(editName)
        layout.addWidget(btnOk)
        layout.addWidget(logTextBox.widget)
        layout.addWidget(testButton)

        # 다이얼로그에 레이아웃 지정
        self.setLayout(layout)

    def test(self):
        logging.debug('damn, a bug')
        logging.info('something to remember')
        logging.warning('that\'s not right')
        logging.error('foobar')
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


# App
if (__name__ == '__main__'):
    app = None
    if (not QApplication.instance()):
        app = QApplication([])
    dlg = MyDialog()
    dlg.show()
    dlg.raise_()
    if (app):
        app.exec_()