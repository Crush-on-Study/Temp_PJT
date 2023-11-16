from PyQt5.QtWidgets import (QWidget, QListWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QStackedWidget, QHBoxLayout)
from PyQt5.QtGui import (QImage, QPixmap, QPalette)

import subwidget as sw

class CustomWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.leftList = QListWidget()
        self.leftList.insertItem(0, 'Information')
        self.leftList.insertItem(1, 'LCA Process')
        self.leftList.insertItem(2, 'LCA Method')
        self.leftList.insertItem(3, 'Review Content')
        self.leftList.setFixedSize(200, 640)

        self.stack1 = sw.InformationWidget(self)
        self.stack2 = sw.LCAProcessWidget(self)
        self.stack3 = sw.AnalysisWidget(self)
        self.stack4 = sw.ReviewContentWidget(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftList)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftList.currentRowChanged.connect(self.display)
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('StackedWidget demo')
        self.show()

    def display(self, i):
        self.Stack.setCurrentIndex(i)





def main():
    pass


# app = QApplication(sys.argv)
# ex = stackedExample()
# sys.exit(app.exec_())

if __name__ == "__main__":
    main()
