import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QIcon, QPixmap
import os
import sys
import Levels
from ClickableLabelWidget import ClickableLabelWidget as LevelWidget

class LevelsWindow(QWidget):
    
    minWHBackBtn = 50

    def __init__(self, showMainWindow, showGameWindow):
        super().__init__()
        self.initVariables(showMainWindow, showGameWindow)
        self.initUI()

    def initVariables(self, showMainWindow, showGameWindow):
        self.showGameWindow = showGameWindow
        self.showMainWindow = showMainWindow

    def initUI(self):
        # self.initWindow()
        self.addWidgetss()
        # self.show()

    def addWidgetss(self):
        self.layoutMain = QVBoxLayout()
        self.layoutMain.setContentsMargins(0, 0, 0, 0)

        self.addToolBarWidget()
        self.addLevels()

        self.layoutMain.setMenuBar(self.toolBar)
        self.setLayout(self.layoutMain)
    
    def addToolBarWidget(self):
        self.toolBar = QToolBar()
        self.toolBar.setMinimumHeight(self.minWHBackBtn)
        size = QSize(self.minWHBackBtn, self.minWHBackBtn)
        self.toolBar.setIconSize(size)

        self.addBackButtonToToolBar()
    
    def addBackButtonToToolBar(self):
        self.buttonBack = QToolButton()
        self.buttonBack.setMinimumWidth(self.minWHBackBtn)
        self.buttonBack.setMinimumHeight(self.minWHBackBtn)
        icon = QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + "back.png")
        self.buttonBack.setIcon(icon)
        size = QSize(self.minWHBackBtn, self.minWHBackBtn)
        self.buttonBack.setIconSize(size)
        self.buttonBack.clicked.connect(self.showMainWindow)
        self.toolBar.addWidget(self.buttonBack)
    
    def addLevels(self):
        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        for row in range(int((len(Levels.levels) + 1) / 2)):
            for column in range(2):
                if (len(Levels.levels) > row*2 + column):
                    levelButton = LevelWidget(
                        os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + Levels.levels[row*2 + column]["imageName"],
                        row*2 + column,
                        self.launchGame,
                        200 # maxSizeWH
                        ) # Levels.levels[row*2 + column]["name"]
                    
                    self.gridLayout.addWidget(levelButton, row, column)
        
        self.gridLayout.setRowStretch(1, 1)
        self.layoutMain.addLayout(self.gridLayout)
        
    def launchGame(self, gameNumber):
        self.showGameWindow(gameNumber)

    def getLayout(self):
        return self.layoutMain

# print(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + "back.png")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = LevelsWindow(None)
    app.exec_()