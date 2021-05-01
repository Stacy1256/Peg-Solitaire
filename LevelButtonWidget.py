import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor, QIcon, QPixmap, QColorConstants

class LevelMenuButton(QAction):

    def __init__(self, levelID, levelProperties: dict, clickAction):
        super().__init__(
            QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + levelProperties["imageName"]),
            levelProperties["name"]
        )
        self.levelID = levelID

        image = QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "Images" + os.path.sep + levelProperties["imageName"])

        self.setIcon(image)
        self.setText(levelProperties["name"])

        # self.activate.connect(lambda: clickAction(levelID))
