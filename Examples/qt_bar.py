"""
Author       : Hanqing Qi
Date         : 2023-11-07 14:26:49
LastEditors  : Hanqing Qi
LastEditTime : 2023-11-07 14:29:47
FilePath     : /GUI/Examples/qt_test.py
Description  : A simple example of a progress bar in PyQt5
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar
from PyQt5.QtCore import Qt, QTimer

class BarDemo(QWidget):
    def __init__(self):
        super(BarDemo, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Qt Progress Bar Example')
        
        self.progressBar = QProgressBar(self)
        self.progressBar.setOrientation(Qt.Vertical)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.progressBar)
        self.setLayout(self.layout)

        # Timer setup
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateBar)
        self.timer.start(100)

        self.show()

    def updateBar(self):
        value = self.progressBar.value()

        # Increase the value until 100 and then reset to 0
        if value < 100:
            value += 1
        else:
            value = 0
        self.progressBar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = BarDemo()
    sys.exit(app.exec_())
