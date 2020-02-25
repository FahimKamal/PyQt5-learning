from PyQt5 import QtWidgets, uic


def convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text()) * 1.23))


app = QtWidgets.QApplication([])
dlg = uic.loadUi('test.ui')

# At the start program will focus on Euro field
dlg.lineEdit.setFocus()
# Set Place holder in text field
dlg.lineEdit.setPlaceholderText('Euro')
dlg.lineEdit_2.setPlaceholderText('Dollar')

# Set the lineEdit_2 as read only
dlg.lineEdit_2.setReadOnly(True)

dlg.Push_me.clicked.connect(convert)

# Will push the calculate button when pressed enter key
dlg.lineEdit.returnPressed.connect(convert)

dlg.show()
app.exec()