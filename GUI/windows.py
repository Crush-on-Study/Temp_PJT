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

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 720, 880)
        self.show()

    def initMenu(self):

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # create Menu
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        viewMenu = menubar.addMenu('&View')
        optionMenu = menubar.addMenu('&Option')
        toolMenu = menubar.addMenu('&Tool')

        # fileMenu Action
        fileMenu.addAction(self.action_open())
        fileMenu.addAction(self.action_run())
        fileMenu.addAction(self.action_quit())

    def set_filename(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.filename = fname[0]

        if fname[0]:
            self.form_widget.line1.setText(self.filename)

    def run_analysis(self):
        if self.filename == '':
            self.form_widget.line1.setText("먼저 파일을 설정해주세요!")
        else:
            if self.filename.endswith('.xlsx'):
                try:
                    df = pd.read_excel(self.filename)  # 엑셀 파일 읽기
                    tab_delimited = df.to_csv(sep='\t', index=False)  # 탭으로 구분된 형태로 변환
                    self.form_widget.edit1.setText(tab_delimited)  # 탭 형태의 문자열을 QTextEdit에 설정
                    self.statusBar().showMessage("엑셀 파일이 로드되었습니다.")
                except Exception as e:
                    self.statusBar().showMessage(f"파일 불러오기 오류: {e}")
            else:
                self.statusBar().showMessage("Excel 파일을 선택해주세요 (*.xlsx)")


    def action_open(self):
        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.set_filename)
        return openFile

    def action_run(self):
        runAction = QAction('Run', self)
        runAction.setShortcut('Ctrl+G')
        runAction.setStatusTip('Run Analysis')
        runAction.triggered.connect(self.run_analysis)
        return runAction

    def action_quit(self):
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        return exitAction


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
