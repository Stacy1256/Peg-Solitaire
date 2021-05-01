#!/usr/bin/python3 
#-*- coding: utf-8 -*-

import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QSize
from LevelsWindow import LevelsWindow
from GameWindow import GameWindow, MyProxyStyle

import os

class MainWindow(QStackedWidget):
    def __init__(self):
        # self.start()
        super().__init__()
        self.initVariables()
        self.initUI()
    
    def initUI(self):
        self.initWindow()

    def initVariables(self):
        self.desktopWindowSize = (QDesktopWidget().availableGeometry().width(), QDesktopWidget().availableGeometry().height())
        self.desktopWindowSizeDefault = (1366, 728)
        self.desktopWindowSizeCoefficients = (self.desktopWindowSize[0]/self.desktopWindowSizeDefault[0], self.desktopWindowSize[1]/self.desktopWindowSizeDefault[1])

    def initWindow(self):
        self.resize(int(400*self.desktopWindowSizeCoefficients[0]), int(600*self.desktopWindowSizeCoefficients[1]))
        # self.center()
        self.setWindowTitle("Peg-Solitaire")

class MenuWindow(QWidget):
    
    def __init__(self, showLevelsWindow):
        # self.start()
        super().__init__()
        self.initVariables(showLevelsWindow)
        self.initUI()

    def initVariables(self, showLevelsWindow):

        # Виставляємо своєрідні константи, що стосуються здебільшого розміру програми
        self.showLevelsWindow = showLevelsWindow
        self.desktopWindowSize = (QDesktopWidget().availableGeometry().width(), QDesktopWidget().availableGeometry().height())
        self.desktopWindowSizeDefault = (1366, 728)
        self.desktopWindowSizeCoefficients = (self.desktopWindowSize[0]/self.desktopWindowSizeDefault[0], self.desktopWindowSize[1]/self.desktopWindowSizeDefault[1])

    # Ініціалізація інтерфейсу користувача
    def initUI(self):
        
        self.intiWindow()
        self.addWidgets()

    # Виставляємо параметри вікна
    def intiWindow(self):
        
        self.setFixedSize(QSize(int(400*self.desktopWindowSizeCoefficients[0]), int(600*self.desktopWindowSizeCoefficients[1])))
        self.center()
        self.setWindowTitle("Peg-Solitaire")

    # Додаємо розмітки і кнопку на вікно
    def addWidgets(self):
        
        self.createLayout()
        self.addLevelsButton()
        self.layoutV.addStretch(1)
        
        self.layoutV.addLayout(self.layoutH, 3)
        
        self.layoutV.addStretch(3)
        self.setLayout(self.layoutV)
    
    # Створюємо розмітки
    def createLayout(self):
        self.layoutV = QVBoxLayout()
        self.layoutH = QHBoxLayout()

    # Додаємо кнопку "рівні"
    def addLevelsButton(self):
        buttonLevels = QPushButton("Levels", self)
        buttonLevels.setMinimumHeight(60)
        buttonLevels.clicked.connect(self.showLevelsWindow)
        self.layoutH.addStretch(1)
        self.layoutH.addWidget(buttonLevels, 2)
        self.layoutH.addStretch(1)

    # Робимо вікно посередині екрану
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        # qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openLevelsLayout(self):
        pass

"""Контролюємо яке вікно показуємо"""
class Controller:
    
    def __init__(self):

        self.mainWindow = MainWindow()
        self.mainWindow.show()

        self.showMainWindow()
    
    def showMainWindow(self):
        
        self.removeAllWidgets()

        menuWindow = MenuWindow(self.showLevelsWindow)
        self.mainWindow.addWidget(menuWindow)
        # menuWindow.show()

        self.mainWindow.update()

        self.mainWindow.setCurrentWidget(menuWindow)

        
        

    def showLevelsWindow(self):
        self.removeAllWidgets()

        levelsWindow = LevelsWindow(self.showMainWindow, self.showGameWindow)
        self.mainWindow.addWidget(levelsWindow)
        # levelsWindow.show()

        self.mainWindow.update()

        self.mainWindow.setCurrentWidget(levelsWindow)
    
    def showGameWindow(self, gameNumber):
        self.removeAllWidgets()

        gameWindow = GameWindow(gameNumber, self.showLevelsWindow)

        self.mainWindow.addWidget(gameWindow)
        # gameWindow.show()

        self.mainWindow.update()

        self.mainWindow.setCurrentWidget(gameWindow)

    def removeAllWidgets(self):
        for widget_index in range(self.mainWindow.count()):
            widget = self.mainWindow.widget(widget_index)
            self.mainWindow.removeWidget(widget)
            widget.deleteLater()

if __name__== '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    # menuWindow = MenuWindow()
    app.exec_()
    
