#!/usr/bin/python3 
#-*- coding: utf-8 -*-

import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QColor
from array import *

import os

class App(QWidget):
    def __init__(self):
        self.start()
        self.set()
        
    


    def start(self):
        self.ui = uic.loadUi("Peg_Gui.ui")
        self.ui.show();
        

    def set(self):
        #buttons= [self.ui.btn_1, self.ui.btn_2]
        self.ui.btn_1.clicked.connect(lambda: self.click())
        self.ui.btn_2.clicked.connect(lambda: self.click())
        self.ui.btn_3.clicked.connect(lambda: self.click())
        self.ui.btn_4.clicked.connect(lambda: self.click())
        self.ui.btn_5.clicked.connect(lambda: self.click())
        self.ui.btn_6.clicked.connect(lambda: self.click())
        self.ui.btn_7.clicked.connect(lambda: self.click())
        self.ui.btn_8.clicked.connect(lambda: self.click())
        self.ui.btn_9.clicked.connect(lambda: self.click())
        self.ui.btn_10.clicked.connect(lambda: self.click())
        self.ui.btn_11.clicked.connect(lambda: self.click())
        self.ui.btn_12.clicked.connect(lambda: self.click())
        self.ui.btn_13.clicked.connect(lambda: self.click())
        self.ui.btn_14.clicked.connect(lambda: self.click())
        self.ui.btn_15.clicked.connect(lambda: self.click())
        self.ui.btn_16.clicked.connect(lambda: self.click())
        self.ui.btn_17.clicked.connect(lambda: self.click())
        self.ui.btn_18.clicked.connect(lambda: self.click())
        self.ui.btn_19.clicked.connect(lambda: self.click())
        self.ui.btn_20.clicked.connect(lambda: self.click())
        self.ui.btn_21.clicked.connect(lambda: self.click())
        self.ui.btn_22.clicked.connect(lambda: self.click())
        self.ui.btn_23.clicked.connect(lambda: self.click())
        self.ui.btn_24.clicked.connect(lambda: self.click())
        self.ui.btn_25.clicked.connect(lambda: self.click())
        self.ui.btn_26.clicked.connect(lambda: self.click())
        self.ui.btn_27.clicked.connect(lambda: self.click())
        self.ui.btn_28.clicked.connect(lambda: self.click())
        self.ui.btn_29.clicked.connect(lambda: self.click())
        self.ui.btn_30.clicked.connect(lambda: self.click())
        self.ui.btn_31.clicked.connect(lambda: self.click())
        self.ui.btn_32.clicked.connect(lambda: self.click())
        self.ui.btn_33.clicked.connect(lambda: self.click())
        self.ui.btn_34.clicked.connect(lambda: self.click())
        self.ui.btn_35.clicked.connect(lambda: self.click())
        self.ui.btn_36.clicked.connect(lambda: self.click())
        self.ui.btn_37.clicked.connect(lambda: self.click())
        self.ui.btn_38.clicked.connect(lambda: self.click())
        self.ui.btn_39.clicked.connect(lambda: self.click())
        self.ui.btn_40.clicked.connect(lambda: self.click())
        self.ui.btn_41.clicked.connect(lambda: self.click())
        self.ui.btn_42.clicked.connect(lambda: self.click())
        self.ui.btn_43.clicked.connect(lambda: self.click())
        self.ui.btn_44.clicked.connect(lambda: self.click())
        self.ui.btn_45.clicked.connect(lambda: self.click())
        self.ui.btn_46.clicked.connect(lambda: self.click())
        self.ui.btn_47.clicked.connect(lambda: self.click())
        self.ui.btn_48.clicked.connect(lambda: self.click())
        self.ui.btn_49.clicked.connect(lambda: self.click())
        self.ui.btn_50.clicked.connect(lambda: self.click())
        self.ui.btn_51.clicked.connect(lambda: self.click())
        self.ui.btn_52.clicked.connect(lambda: self.click())
        self.ui.btn_53.clicked.connect(lambda: self.click())
        self.ui.btn_54.clicked.connect(lambda: self.click())
        self.ui.btn_55.clicked.connect(lambda: self.click())
        self.ui.btn_56.clicked.connect(lambda: self.click())
        self.ui.btn_57.clicked.connect(lambda: self.click())
        self.ui.btn_58.clicked.connect(lambda: self.click())
        self.ui.btn_59.clicked.connect(lambda: self.click())
        self.ui.btn_60.clicked.connect(lambda: self.click())
        self.ui.btn_61.clicked.connect(lambda: self.click())
        self.ui.btn_62.clicked.connect(lambda: self.click())
        self.ui.btn_63.clicked.connect(lambda: self.click())
        self.ui.btn_64.clicked.connect(lambda: self.click())
        self.ui.btn_65.clicked.connect(lambda: self.click())
        self.ui.btn_66.clicked.connect(lambda: self.click())
        self.ui.btn_67.clicked.connect(lambda: self.click())
        self.ui.btn_68.clicked.connect(lambda: self.click())
        self.ui.btn_69.clicked.connect(lambda: self.click())
        self.ui.btn_70.clicked.connect(lambda: self.click())
        self.ui.btn_71.clicked.connect(lambda: self.click())
        self.ui.btn_72.clicked.connect(lambda: self.click())
        self.ui.btn_73.clicked.connect(lambda: self.click())
        self.ui.btn_74.clicked.connect(lambda: self.click())
        self.ui.btn_75.clicked.connect(lambda: self.click())
        self.ui.btn_76.clicked.connect(lambda: self.click())
        self.ui.btn_77.clicked.connect(lambda: self.click())
        self.ui.btn_78.clicked.connect(lambda: self.click())
        self.ui.btn_79.clicked.connect(lambda: self.click())
        self.ui.btn_70.clicked.connect(lambda: self.click())
        self.ui.btn_81.clicked.connect(lambda: self.click())
        self.ui.btn_back.clicked.connect(lambda: self.click())
        self.ui.btn_menu.clicked.connect(lambda: self.click())
        self.ui.btn_restart.clicked.connect(lambda: self.click())
        
        #додати комбобокс

    def click(self, num=1):
        print(num)
        col = QColor(1, 80, 0)
        self.ui.btn_restart.setStyleSheet("QWidget { background-color: %s }" %col.name())
        self.ui.buttons_grid[1,1].setStyleSheet("QWidget { background-color: %s }" %col.name())

if __name__== '__main__':
    app = QApplication(sys.argv)
    #app = QApplication(sys.arqv)
    ex = App()
    app.exec_()