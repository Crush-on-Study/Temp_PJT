import sys
import pandas as pd
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QTextEdit, QAction, QFileDialog, qApp, QPushButton)
from customwidget import CustomWidget

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.filename = ''

    def initUI(self):
        self.initMenu()
        self.statusBar()
        self.form_widget = CustomWidget(self)
        self.setCentralWidget(self.form_widget)

        self.setWindowTitle('LCA Survey')
        self.setGeometry(300, 300, 600, 320)  # 사이즈를 반으로 컷
        self.show()

    def initMenu(self):

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # create Menu
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')
        

        # fileMenu Action
        fileMenu.addAction(self.action_open())
        fileMenu.addAction(self.action_run())
        fileMenu.addAction(self.action_quit())

    def action_open(self):
        openFile = QAction('New', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Make New File')
        openFile.triggered.connect(self.make_document)
        return openFile

    def action_run(self):
        runAction = QAction('Save', self)
        runAction.setShortcut('Ctrl+G')
        runAction.setStatusTip('Save Document')
        runAction.triggered.connect(self.save_document)
        return runAction

    def action_quit(self):
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        return exitAction

    def make_document(self):
        print('make_document')

    def save_document(self):
        print('save_doc')
    #     # CustomWidget에서 데이터 가져오기
    #     data = self.form_widget.get_survey_data()  # 이 함수는 CustomWidget에 있는 데이터를 가져오는 함수일 겁니다.

    #     if data:
    #         # DataFrame 생성
    #         df = pd.DataFrame(data, columns=['Company Name', 'Your Name', 'Your Position', 'Industry', 'Review'])

    #         # 파일 다이얼로그 열기
    #         options = QFileDialog.Options()
    #         file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)

    #         if file_name:
    #             # 엑셀 파일로 저장
    #             df.to_excel(file_name, index=False)
    #             print(f"File saved to: {file_name}")
    #     else:
    #         print("No data to save.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
