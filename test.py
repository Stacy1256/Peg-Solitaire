import sys
from PyQt5 import QtWidgets


class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        colorButton = QtWidgets.QPushButton("Colors")
        exitAct = QtWidgets.QAction('Exit', self)

        toolbar = self.addToolBar("Exit")

        toolbar.addWidget(colorButton)
        toolbar.addAction(exitAct)

        menu = QtWidgets.QMenu()
        menu.addAction("red")
        menu.addAction("green")
        menu.addAction("blue")
        colorButton.setMenu(menu)

        menu.triggered.connect(lambda action: print(action.text()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())