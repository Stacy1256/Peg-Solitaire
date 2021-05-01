from LevelButtonWidget import LevelMenuButton
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QIcon, QPixmap, QColorConstants
import os
import Levels
import sys
from ClickableLabelWidget import ClickableLabelWidget, ClickableLabelWidget2
from copy import deepcopy

LevelMenuStyle = """
QMenu {{
    font-size: 18px;
    left: 20px;
    color: black;
    width: {}px;
}}

QMenu::item {{
    spacing: 20px;
    height: 60px;
    width: {}px;
    padding: 2px 20px 2px 30px;
            }}
QMenu::item:selected {{
    background-color: blue;
            }}
QMenu::icon {{
    padding-left: 10px;
}}"""
class MyProxyStyle(QProxyStyle):
    pass
    def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None):

        if QStyle_PixelMetric == QStyle.PM_SmallIconSize:
            return 50
        else:
            return QProxyStyle.pixelMetric(self, QStyle_PixelMetric, option, widget)

class GameWindow(QWidget):

    # Min width, height of button on ToolBar
    minWHBackBtn = 50 
    selectedPegIndex = -1

    def __init__(self, gameNumber, showLevelWindow):
        # self.start()
        super().__init__()
        self.initVariables(showLevelWindow, gameNumber)
        self.initUI()

    def initVariables(self, showLevelWindow, gameNumber):
        self.gameNumber = gameNumber
        self.showLevelWindow = showLevelWindow
        self.desktopWindowSize = (QDesktopWidget().availableGeometry().width(), QDesktopWidget().availableGeometry().height())
        self.desktopWindowSizeDefault = (1366, 728)
        self.windowSizeDefault = (400, 600)
        self.desktopWindowSizeCoefficients = (self.desktopWindowSize[0]/self.desktopWindowSizeDefault[0], self.desktopWindowSize[1]/self.desktopWindowSizeDefault[1])
        # print(self.desktopWindowSize)

    def initUI(self):
        # self.initWindow()
        self.addWidgetss()
        self.loadGame()
        self.setLayout(self.layoutMain)

    # Додаємо віджети до вікна
    def addWidgetss(self):
        self.layoutMain = QVBoxLayout()
        self.layoutMain.setContentsMargins(0, 0, 0, 0)

        self.addToolBarWidget()

        self.layoutMain.setMenuBar(self.toolBar)
    
    # Додаємо тулбар
    def addToolBarWidget(self):
        self.toolBar = QToolBar()
        self.toolBar.setMinimumHeight(self.minWHBackBtn)
        size = QSize(self.minWHBackBtn, self.minWHBackBtn)
        self.toolBar.setIconSize(size)

        self.addBackButtonToToolBar()
        self.addMenuToToolBar()
        self.addSpacerWidgetToToolBar()
        self.addRestartButtonToToolBar()
        self.addUndoButtonToToolBar()
    
    # Додали меню до тулбару
    def addMenuToToolBar(self):
        self.menuGameLevelsButton = QPushButton("Levels")
        self.menuGameLevelsButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.menuGameLevels = QMenu()
        self.menuGameLevels.setAutoFillBackground(True)
        
        for i in range(len(Levels.levels)):
            level = deepcopy(Levels.levels[i])
            q = self.menuGameLevels.addAction(
                QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + level["imageName"]),
                level["name"]
            )
        
        self.menuGameLevels.triggered.connect(lambda action: self.gameLevelChanged(action.text()))

        self.menuGameLevelsButton.setMenu(self.menuGameLevels)

        self.toolBar.addWidget(self.menuGameLevelsButton)

        self.menuGameLevelsButton.show()

        style = (LevelMenuStyle.format(200, 200))

        self.menuGameLevels.setStyle(MyProxyStyle("Windows"))

        self.menuGameLevels.setStyleSheet(style)

    # Обрали інший рівень з меню (випадаючий список)
    def gameLevelChanged(self, levelName):

        for levelID in range(len(Levels.levels)):
            if Levels.levels[levelID]["name"] == levelName:
                break

        self.gameNumber = levelID
        self.loadGame()

    def addBackButtonToToolBar(self):
        self.buttonBack = QToolButton()
        self.buttonBack.setMinimumWidth(self.minWHBackBtn)
        self.buttonBack.setMinimumHeight(self.minWHBackBtn)
        icon = QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + "back.png")
        self.buttonBack.setIcon(icon)
        size = QSize(self.minWHBackBtn, self.minWHBackBtn)
        self.buttonBack.setIconSize(size)
        self.buttonBack.clicked.connect(self.showLevelWindow)
        self.toolBar.addWidget(self.buttonBack)
    
    def addRestartButtonToToolBar(self):
        self.restartButton = QToolButton()
        self.restartButton.setMinimumWidth(self.minWHBackBtn)
        self.restartButton.setMinimumHeight(self.minWHBackBtn)
        icon = QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + "restart.png")
        self.restartButton.setIcon(icon)
        size = QSize(self.minWHBackBtn, self.minWHBackBtn)
        self.restartButton.setIconSize(size)
        self.restartButton.clicked.connect(self.restartGame)
        self.toolBar.addWidget(self.restartButton)

    def addSpacerWidgetToToolBar(self):
        self.spacerWidget = QWidget()
        self.spacerWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        # self.spacerWidget.setVisible(True)
        self.toolBar.addWidget(self.spacerWidget)
    
    def addUndoButtonToToolBar(self):
        self.undoButton = QToolButton()
        self.undoButton.setMinimumWidth(self.minWHBackBtn)
        self.undoButton.setMinimumHeight(self.minWHBackBtn)
        icon = QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + "undo.png")
        size = QSize(self.minWHBackBtn, self.minWHBackBtn)
        self.undoButton.setIconSize(size)
        self.undoButton.clicked.connect(self.undoMove)
        self.undoButton.setIcon(icon)
        self.toolBar.addWidget(self.undoButton)

    # Завантажуємо гру
    def loadGame(self):
        # self.gameGridLayout = QGridLayout()
        self.gameParam = deepcopy((Levels.levels[self.gameNumber]))
        self.gameGrid = self.gameParam["map"]
        self.gameGridHistory = [deepcopy(self.gameGrid)]

        self.calculateSizes()

        self.loadGameGrid(self.gameGrid)

    # Завнтажуємо поле
    def loadGameGrid(self, grid):
        try:
            self.gridWidget.deleteLater()
        except:
            pass
        finally:
            pass

        self.setGridWidget()

        self.gameGridLayout = QGridLayout(self.gridWidget)
        self.gameGridLayout.setContentsMargins(0, 0, 0, 0)

        index = 0

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if Levels.config[grid[row][column]] != None:
                    label = ClickableLabelWidget(
                        os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + Levels.config[grid[row][column]],
                        0,
                        self.btnClicked,
                        self.pegSize[0],
                        isPeg = True,
                        pegIndex = index
                        )
                    index += 1
                    # print(label)
                    self.gameGridLayout.addWidget(label, row, column)
                    # print(self.gameGridLayout.indexOf(label))
        
        self.gameGridLayout.setSpacing(0)
        # self.gameGridLayout.SetMaximumSize

        # self.layoutMain.addLayout(self.gameGridLayout)
        self.layoutMain.addWidget(self.gridWidget)
        self.update()
    
    # Розраховуємо розмір одного квадратика на полі
    def calculateSizes(self):
        self.pegSize = (int(self.windowSizeDefault[0]/self.gameParam["size"][0]*self.desktopWindowSizeCoefficients[0]),) * 2
        self.gridWidgetSize = (self.pegSize[0]*self.gameParam["size"][0], self.pegSize[1]*self.gameParam["size"][1])

    # Створюємо ігрове поле
    def setGridWidget(self):
        self.gridWidget = QWidget()
        self.gridWidget.setMaximumSize(QSize(*self.gridWidgetSize))

    def restartGame(self):
        # self.deleteLater()
        # self.__init__(self.gameNumber, self.showLevelWindow)
        self.loadGame()
        self.update()
    
    def btnClicked(self, indexSenderPeg):
        locationSenderPeg = self.gameGridLayout.getItemPosition(indexSenderPeg)

        if self.selectedPegIndex != -1:
            
            locationSelectedPeg = self.gameGridLayout.getItemPosition(self.selectedPegIndex)     

            if self.tryEatPeg(locationSelectedPeg, locationSenderPeg):
                pass    
            else:
                if self.gameGrid[locationSelectedPeg[0]][locationSelectedPeg[1]] == "+":
                    self.gameGrid[locationSelectedPeg[0]][locationSelectedPeg[1]] = "."
                elif self.gameGrid[locationSelectedPeg[0]][locationSelectedPeg[1]] == "a":
                    self.gameGrid[locationSelectedPeg[0]][locationSelectedPeg[1]] = "i"

        if self.gameGrid[locationSenderPeg[0]][locationSenderPeg[1]] == ".":
            self.gameGrid[locationSenderPeg[0]][locationSenderPeg[1]] = "+"
            self.selectedPegIndex = indexSenderPeg
            
        elif self.gameGrid[locationSenderPeg[0]][locationSenderPeg[1]] == "i":
            self.gameGrid[locationSenderPeg[0]][locationSenderPeg[1]] = "a"
            self.selectedPegIndex = indexSenderPeg
        
        if self.checkIfWon():
            self.showCongratulations()

        self.loadGameGrid(self.gameGrid)
    
    # Спроба з'їсти фішку. Вдається - ок, невається, то нехай і невдається
    def tryEatPeg(self, loc1, loc2):
        # loc1 - selected peg location
        # loc2 - pressed peg location
        # loc3 - location pf peg between loc1 and loc2
        a = loc1[0] - loc2[0]
        b = loc1[1] - loc2[1]
        loc3 = (int((loc1[0] + loc2[0])/2), int((loc1[1] + loc2[1])/2))

        if ((abs(a) == 2 and loc1[1] == loc2[1] \
            or abs(b) == 2 and loc1[0] == loc2[0]) \
            and (self.gameGrid[loc2[0]][loc2[1]] == "O" or self.gameGrid[loc2[0]][loc2[1]] == "o") \
            and (self.gameGrid[loc3[0]][loc3[1]] == "." or self.gameGrid[loc3[0]][loc3[1]] == "i")) == False:
            return False    

        # save last move
        self.gameGridHistory.insert(0, deepcopy(self.gameGrid))

        if self.gameGrid[loc3[0]][loc3[1]] == ".":
            self.gameGrid[loc3[0]][loc3[1]] = "O"
        elif self.gameGrid[loc3[0]][loc3[1]] == "i":
            self.gameGrid[loc3[0]][loc3[1]] = "o"

        if self.gameGrid[loc2[0]][loc2[1]] == "O":
            self.gameGrid[loc2[0]][loc2[1]] = "."
        elif self.gameGrid[loc2[0]][loc2[1]] == "o":
            self.gameGrid[loc2[0]][loc2[1]] = "i"

        if self.gameGrid[loc1[0]][loc1[1]] == "+":
            self.gameGrid[loc1[0]][loc1[1]] = "O"
        if self.gameGrid[loc1[0]][loc1[1]] == "a":
            self.gameGrid[loc1[0]][loc1[1]] = "o"

        
        self.selectedPegIndex = -1

        return True     

    # def undoMove(self):
    #     if len(self.gameGridHistory) <= 1:
    #         return
    #     index = 0
    #     for row in self.gameGridHistory[0]:
    #         for row_element in row:
    #             if row_element == "+" or row_element == "a":
    #                 self.selectedPegIndex = index
    #                 break
    #             if row_element != "":
    #                 index += 1
    #     self.selectedPegIndex 
    #     self.loadGameGrid(self.gameGridHistory[0])
    #     self.gameGrid = deepcopy(self.gameGridHistory[0])
    #     self.gameGridHistory.pop()
    def undoMove(self):
        if len(self.gameGridHistory) <= 1:
            return
        index = 0
        for row in self.gameGridHistory[0]:
            for row_element in row:
                if row_element == "+" or row_element == "a":
                    self.selectedPegIndex = index
                    break
                if row_element != "":
                    index += 1
        self.loadGameGrid(self.gameGridHistory[0])
        self.gameGrid = deepcopy(self.gameGridHistory[0])
        self.gameGridHistory.pop(0)

    # Перевірка виграшу
    def checkIfWon(self):
        for row in self.gameGrid:
            for row_element in row:
                if row_element == "a" or row_element == "i":
                    pass
                else:
                    return False
        
        return True

    def showCongratulations(self):
        textCongratulations = "You have completed this game!\nHurray!"
        self.widgetCongrats = ClickableLabelWidget2(self, self.closeCongratulations, self.windowSizeDefault[0], self.windowSizeDefault[1], textCongratulations)
        self.layoutMain.addWidget(self.widgetCongrats)

    def closeCongratulations(self):
        self.widgetCongrats.deleteLater()

    def getLayout(self):
        return self.layoutMain