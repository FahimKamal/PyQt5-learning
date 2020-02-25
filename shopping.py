from PyQt5 import QtWidgets, uic


def add():
    # if the input_field is not empty then add new item
    if not UI.input_field.text() == '':
        UI.listWidget.addItem(UI.input_field.text())
        UI.input_field.setText('')


app = QtWidgets.QApplication([])
UI = uic.loadUi('shopping_list.ui')

UI.input_field.setPlaceholderText('Add new Item')
UI.input_field.returnPressed.connect(add)

UI.add_button.clicked.connect(add)

UI.show()
app.exec()