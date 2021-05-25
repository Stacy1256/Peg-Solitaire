#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
from RenderCube import cubeMesh
from constants import (
    ANGLE_INCREMENTOR,
    FRAMES_PER_SECOND,
    MAX_COLOR_VALUE,
    MIN_COLOR_VALUE,
)
import sys
import os
from random import randint
from threading import Timer

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtOpenGL
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtOpenGL import *
from LevelsWindow import LevelsWindow
from OpenGL.GL import *
from OpenGL.GLU import *


from GameWindow import GameWindow


class MainWindow(QStackedWidget):
    def __init__(self):
        # self.start()
        super().__init__()
        self.initVariables()
        self.initUI()

    def initUI(self):
        self.initWindow()
        p = self.palette()
        p.setColor(QPalette.Window, QColor(245, 227, 77))
        self.setPalette(p)

    def initVariables(self):
        self.desktopWindowSize = (
            QDesktopWidget().availableGeometry().width(),
            QDesktopWidget().availableGeometry().height(),
        )
        self.desktopWindowSizeDefault = (1366, 728)
        self.desktopWindowSizeCoefficients = (
            self.desktopWindowSize[0] / self.desktopWindowSizeDefault[0],
            self.desktopWindowSize[1] / self.desktopWindowSizeDefault[1],
        )

    def initWindow(self):
        self.resize(
            int(400 * self.desktopWindowSizeCoefficients[0]),
            int(600 * self.desktopWindowSizeCoefficients[1]),
        )
        # self.center()
        self.setWindowTitle("Peg-Solitaire")


class MenuWindow(QWidget):
    def __init__(self, showLevelsWindow):
        # self.start()
        super().__init__()
        self.initVariables(showLevelsWindow)
        self.widgetq = glWidget(self)

        # timer = QTimer(self)
        # timer.setInterval(1000 / FRAMES_PER_SECOND)  # period, in milliseconds
        # timer.timeout.connect(self.widgetq.renderFigure)
        # timer.start(1000)

        self.initUI()
        # self.widgetq.setLayout(self.layoutV)
        # self.l = QVBoxLayout(self)
        # self.l.addWidget(self.widgetq)
        # self.setLayout(self.l)

    def initVariables(self, showLevelsWindow):

        # Виставляємо своєрідні константи, що стосуються здебільшого розміру програми
        self.showLevelsWindow = showLevelsWindow
        self.desktopWindowSize = (
            QDesktopWidget().availableGeometry().width(),
            QDesktopWidget().availableGeometry().height(),
        )
        self.desktopWindowSizeDefault = (1366, 728)
        self.desktopWindowSizeCoefficients = (
            self.desktopWindowSize[0] / self.desktopWindowSizeDefault[0],
            self.desktopWindowSize[1] / self.desktopWindowSizeDefault[1],
        )

    # Ініціалізація інтерфейсу користувача
    def initUI(self):

        self.initWindow()
        self.addWidgets()

    # Виставляємо параметри вікна
    def initWindow(self):

        self.setFixedSize(
            QSize(
                int(400 * self.desktopWindowSizeCoefficients[0]),
                int(600 * self.desktopWindowSizeCoefficients[1]),
            )
        )
        self.center()
        self.setWindowTitle("Peg-Solitaire")

    # Додаємо розмітки і кнопку на вікно
    def addWidgets(self):

        self.createLayout()
        self.addLevelsButton()
        self.layoutV.addStretch(1)
      
        self.layoutV.addLayout(self.layoutH, 3)

        self.layoutV.addWidget(glWidget(self), 5)

        # self.layoutV.addStretch(3)
        self.setLayout(self.layoutV)

    # Створюємо розмітки
    def createLayout(self):
        self.layoutV = QVBoxLayout()
        self.layoutH = QHBoxLayout()

    # Додаємо кнопку "рівні"
    def addLevelsButton(self):
        buttonLevels = QPushButton("PLAY", self)
        buttonLevels.setMinimumHeight(80)
        buttonLevels.clicked.connect(self.showLevelsWindow)
        self.layoutH.addStretch(1)
        self.layoutH.addWidget(buttonLevels, 2)
        self.layoutH.addStretch(1)
    
    # #timer
    # def timer(self):
    #     self.curr_time = QtCore.QTime(00,00,00)
    #     self.timer = QtCore.QTimer()
    #     self.timer.timeout.connect(self.time)
    #     self.timer.start(1000)

    # def time(self):
    #     self.curr_time = self.curr_time.addSecs(self, 1)
    #     self.upTime.setTime(self.curr_time)


    # Робимо вікно посередині екрану
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        
        # qr.moveCenter(cp)
        self.move(qr.topLeft())

    def openLevelsLayout(self):
        pass


class glWidget(QGLWidget):

    angle = 4.0
    colorList = []

    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(400, 480)
        self.setMaximumSize(550, 550)
        p = self.palette()
        p.setColor(QPalette.Window, QColor(245, 227, 77))
        self.setPalette(p)
        self.startTimer(1000/FRAMES_PER_SECOND)

        #color
        # p = self.palette()
        # p.setColor(QPalette.Window, QColor(240, 216, 240))
        # self.setPalette(p)

    def renderFigure(self):
        
        print(self.angle)
        self.angle = (self.angle + ANGLE_INCREMENTOR) % 360
        self.updateGL()
        # Timer(1000 / FRAMES_PER_SECOND, self.renderFigure).start()

    def timerEvent(self, event):
        self.update()

    def paintGL(self):
        

        # print("paintGL: " + str(self.angle))
        # self.angle = (self.angle + ANGLE_INCREMENTOR) % 720
        # self.angle += ANGLE_INCREMENTOR
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glLoadIdentity()
        # glTranslatef(0.0, 0, -20.0)
        # glBegin(glType)
        # glTranslatef(-2.5, 0.5, -6.0)
        glRotatef(ANGLE_INCREMENTOR, 200.0, 21.0, 1.0)
        # glRotatef(self.angle, 0.0, 0.0, 0.0)
        cubeMesh()


        

        
        # glEnd()
        glFlush()

    def initializeGL(self):
        # glClearDepth(1.0)
        
        glDepthFunc(GL_LESS)
        # print (float(self.width()), float(self.height()), (float(self.width()) / float(self.height())))
        gluPerspective(45.0, (float(self.width()) / float(self.height())), 0.1, 50.0)
        glTranslatef(-3.1, -2.0, -16.0)
        glRotatef(-90.0, 2.0, 3.0, 0.0)
        glColor3f(255.0, 255.0, 255.0)

        # Timer(1 / FRAMES_PER_SECOND, self.renderFigure).start()

        # glClearDepth(1.0)
        # glDepthFunc(GL_LESS)
        # glEnable(GL_DEPTH_TEST)
        # glShadeModel(GL_SMOOTH)
        # glMatrixMode(GL_PROJECTION)
        # glLoadIdentity()
        # gluPerspective(45.0,1.33,0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def randomColorGenerator():
        
        r = randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE) / 255
        g = randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE) / 255
        b = randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE) / 255
        color = (r, g, b)
        return color


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


if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    app = QApplication(sys.argv)
    controller = Controller()
    # menuWindow = MenuWindow()
    app.exec_()
