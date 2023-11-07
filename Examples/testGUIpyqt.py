"""
Author       : Hanqing Qi
Date         : 2023-11-07 14:36:51
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-07 14:42:19
FilePath     : /GUI/testGUIpyqt.py
Description  : A test file for GUI in PyQt5
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPen, QBrush
import numpy as np

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('PyQt5 GUI')

        self.cur_yaw = 0
        self.des_yaw = 0
        self.cur_height = 0
        self.des_height = 0
        self.delay = 10  # milliseconds

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_values)
        self.timer.start(self.delay)
        
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.des_height += 0.1
        elif event.key() == Qt.Key_Down:
            self.des_height -= 0.1
        elif event.key() == Qt.Key_Left:
            self.des_yaw += 0.07
        elif event.key() == Qt.Key_Right:
            self.des_yaw -= 0.07
        elif event.key() == Qt.Key_Escape:
            self.close()

    def angle_to_coordinates(self, radians, radius=50):
        x = radius * np.cos(radians) + self.width()/2
        y = radius * np.sin(radians) + self.height()/2
        return x, y

    def update_values(self):
        self.cur_yaw += 0.03 * (self.des_yaw - self.cur_yaw)
        self.cur_height += 0.02 * (self.des_height - self.cur_height)
        self.update()

    def drawYawCircle(self, painter):
        painter.setPen(QPen(Qt.white, 3))
        painter.drawEllipse(int(self.width()/2 - 50), int(self.height()/2 - 50), 100, 100)

    def drawArrow(self, painter, color, radians):
        x, y = self.angle_to_coordinates(radians)
        painter.setBrush(QBrush(color))
        painter.drawLine(int(self.width()/2), int(self.height()/2), int(x), int(y))

    def drawHeightBar(self, painter, x, height, color):
        painter.setBrush(QBrush(color))
        painter.drawRect(x, int(self.height() - 100), 20, int(-height))

    def drawText(self, painter, text, x, y, color):
        painter.setPen(QPen(color))
        painter.drawText(x, y, text)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        self.drawYawCircle(painter)
        self.drawArrow(painter, Qt.red, self.cur_yaw)
        self.drawArrow(painter, Qt.green, self.des_yaw)
        self.drawHeightBar(painter, self.width() - 100, self.cur_height, Qt.red)
        self.drawHeightBar(painter, self.width() - 70, self.des_height, Qt.green)
        self.drawText(painter, f"Current yaw: {self.cur_yaw:.2f}", 20, 20, Qt.red)
        self.drawText(painter, f"Desired yaw: {self.des_yaw:.2f}", 20, 40, Qt.green)
        self.drawText(painter, f"Cur Height: {self.cur_height:.2f}", self.width() - 100, self.height() - 110, Qt.red)
        self.drawText(painter, f"Des Height: {self.des_height:.2f}", self.width() - 70, self.height() - 110, Qt.green)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())
