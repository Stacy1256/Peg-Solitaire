import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QSize, pyqtSignal, Qt
from PyQt5.QtGui import QColor, QIcon, QPixmap

class ClickableLabelWidget(QLabel):
    clicked = pyqtSignal()
 
    def __init__(self, imagePath, gameNumber, clickAction, maxSizeWH, isPeg = False, pegIndex = -1):
        super().__init__()
        image = QPixmap(imagePath)
        self.setPixmap(image)
        self.setScaledContents(True)
        self.setMaximumHeight(maxSizeWH)
        self.setMaximumWidth(maxSizeWH)
        
        self.imagePath = imagePath
        self.clickAction = clickAction
        self.gameNumber = gameNumber
        self.isPeg = isPeg
        self.pegIndex = pegIndex

    def mouseReleaseEvent(self, QMouseEvent):
        # self.clicked.emit()
        # print("lol")
        if self.isPeg:
            self.clickAction(self.pegIndex)
        else:
            self.clickAction(self.gameNumber)

class ClickableLabelWidget2(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent, clickAction, width, height, text):
        super().__init__(parent)
        self.clickAction = clickAction
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        self.setText(text)
        self.setParent(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickAction()
