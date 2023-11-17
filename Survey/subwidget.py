from PyQt5.QtWidgets import (QButtonGroup,QMessageBox,QGroupBox,QVBoxLayout,QWidget, 
                             QGridLayout, QLabel, QLineEdit, QTextEdit, QFormLayout, QHBoxLayout, 
                             QRadioButton, QCheckBox, QCalendarWidget)

class InformationWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)

        grid.addWidget(QLabel('회사명:'), 0, 0)
        grid.addWidget(QLabel('성명:'), 1, 0)
        grid.addWidget(QLabel('회사 내 직급:'), 2, 0)
        grid.addWidget(QLabel('회사의 주력 산업:'), 3, 0)

        company_name_edit = self.handlerLineEdit()
        your_name_edit = self.handlerLineEdit()
        your_position_edit = self.handlerLineEdit()

        grid.addWidget(company_name_edit, 0, 1)
        grid.addWidget(your_name_edit, 1, 1)
        grid.addWidget(your_position_edit, 2, 1)

        # 주력 산업 라디오 버튼 생성
        industries_group = QGroupBox()
        industries_layout = QVBoxLayout()

        industries = [
            "IT",
            "반도체/디스플레이",
            "자동차",
            "로봇",
            "금융권",
            "기타"
        ]

        group = QButtonGroup(self)
        for idx, industry in enumerate(industries):
            radio = QRadioButton(industry)
            group.addButton(radio, idx)
            industries_layout.addWidget(radio)

        industries_group.setLayout(industries_layout)
        grid.addWidget(industries_group, 3, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 600)
        self.show()
        

    def handlerLineEdit(self):
        return QLineEdit()


    def handlerLineEdit(self):
        return QLineEdit()


    def handlerLineEdit(self):
        return QLineEdit()

    def handlerLineEdit(self):
        self.line1 = QLineEdit()
        return self.line1

    def handlerTextEditor(self):
        self.edit1 = QTextEdit()
        return self.edit1
    def handlerLineEdit(self):
        self.line1 = QLineEdit()
        return self.line1

    def handlerTextEditor(self):
        self.edit1 = QTextEdit()
        return self.edit1


class LCAProcessWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()  # 수직 박스 레이아웃으로 변경
        self.setLayout(layout)

        # 설명을 위한 라벨 추가
        description_label = QLabel(
            "현재 회사에서 제품을 만드는데 해당되는 프로세스만 선택해주시면 됩니다. (다중선택 가능)"
        )
        font = description_label.font()
        font.setBold(True)  # 폰트를 굵게 설정
        description_label.setFont(font)
        layout.addWidget(description_label)

        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # 6개의 체크박스 추가
        checkboxes = [
            "제조 전 단계",
            "수송",
            "제조",
            "재활용",
            "폐기",
            "유통"
        ]
        for checkbox in checkboxes:
            form_layout.addRow(QCheckBox(checkbox))

        self.setWindowTitle('LCAProcess')
        self.setGeometry(300, 300, 300, 600)
        self.show()
        
        # 설명을 위한 라벨 추가
        description_label = QLabel(
            "현재 회사에서 원료 (제조 전 단계) 수송을 위한 운송 종류는 무엇인가요? (다중 선택 가능)"
        )
        font = description_label.font()
        font.setBold(True)  # 폰트를 굵게 설정
        description_label.setFont(font)
        layout.addWidget(description_label)

        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # 4개의 체크박스 추가
        checkboxes = [
            "육상",
            "해운",
            "항공",
            "기타"
        ]
        for checkbox in checkboxes:
            form_layout.addRow(QCheckBox(checkbox))

        self.setWindowTitle('LCAProcess')
        self.setGeometry(300, 300, 300, 600)
        self.show()
        
        # 설명을 위한 라벨 추가
        description_label = QLabel(
            "가장 자주 이동하는 지역과의 거리는 어떻게 되나요?"
        )
        font = description_label.font()
        font.setBold(True)  # 폰트를 굵게 설정
        description_label.setFont(font)
        layout.addWidget(description_label)

        form_layout = QVBoxLayout()  # 수직 박스 레이아웃으로 변경
        layout.addLayout(form_layout)

        # 5개의 라디오 버튼 추가
        radio_buttons = [
            "0~20km",
            "21~40km",
            "41~60km",
            "61~80km",
            "그 이상"
        ]
        group = QButtonGroup(self)
        for idx, radio_text in enumerate(radio_buttons):
            radio = QRadioButton(radio_text)
            group.addButton(radio, idx)
            form_layout.addWidget(radio)

        self.setWindowTitle('LCAProcess')
        self.setGeometry(300, 300, 300, 600)
        self.show()
        
        
        # 설명을 위한 라벨 추가
        description_label = QLabel(
            "가장 자주 많이 사용하는 원료의 종류는 어떻게 되나요?"
        )
        font = description_label.font()
        font.setBold(True)  # 폰트를 굵게 설정
        description_label.setFont(font)
        layout.addWidget(description_label)

        form_layout = QVBoxLayout()  # 수직 박스 레이아웃으로 변경
        layout.addLayout(form_layout)

        # 4개의 라디오 버튼 추가
        radio_buttons = [
            "화학 약품",
            "제조 부품",
            "농업 비료",
            "기타"
        ]
        group = QButtonGroup(self)
        for idx, radio_text in enumerate(radio_buttons):
            radio = QRadioButton(radio_text)
            group.addButton(radio, idx)
            form_layout.addWidget(radio)

        self.setWindowTitle('LCAProcess')
        self.setGeometry(300, 300, 300, 600)
        self.show()
        

class AnalysisWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.setSpacing(5)  # 간격을 5로.
        self.setLayout(vbox)

        method_label = QLabel("LCA 방법론 (다중선택 가능)")
        font = method_label.font()
        font.setBold(True)
        method_label.setFont(font)
        vbox.addWidget(method_label)

        cml_checkbox = QCheckBox("CML")
        ipcc_checkbox = QCheckBox("IPCC")
        traci_checkbox = QCheckBox("TRACI")
        epd_checkbox = QCheckBox("EPD(환경성적표지)")

        vbox.addWidget(cml_checkbox)
        vbox.addWidget(ipcc_checkbox)
        vbox.addWidget(traci_checkbox)
        vbox.addWidget(epd_checkbox)

        self.setWindowTitle('AnalysisWidget')
        self.setGeometry(300, 300, 300, 150)
        self.show()
        
        # 텍스트 입력 필드 추가
        material_labels = [
            "제조 공정에 사용되는 원료:",
            "재활용에 사용되는 원료:",
            "폐기에 사용되는 원료:",
            "제조에 사용되는 전력량:"
        ]
        for label in material_labels:
            material_label = QLabel(label)
            material_text = QLineEdit()
            vbox.addWidget(material_label)
            vbox.addWidget(material_text)

        self.setWindowTitle('AnalysisWidget')
        self.setGeometry(300, 300, 300, 250)
        self.show()
        
        # 라디오버튼 추가
        awareness_label = QLabel("평소에 ESG 혹은 LCA에 대해 알고 있었나요?")
        font = awareness_label.font()
        font.setBold(True)
        awareness_label.setFont(font)
        vbox.addWidget(awareness_label)

        radio_buttons = []
        options = [
            "1. 전혀 몰랐다.",
            "2. 이름만 들어봤다.",
            "3. 대략적으로 이해를 하고 있다.",
            "4. 실제로 자주 접하고 있으며 나름 익숙하다.",
            "5. 전문가다."
        ]
        for option in options:
            button = QRadioButton(option)
            radio_buttons.append(button)
            vbox.addWidget(button)

        self.setWindowTitle('AnalysisWidget')
        self.setGeometry(300, 300, 300, 400)
        self.show()

class ReviewContentWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        info_label = QLabel("그 외 의견을 자유롭게 기술해주세요. (글자 수 제한 없음)")
        layout.addWidget(info_label)

        review_text = QTextEdit()
        layout.addWidget(review_text)

        self.setWindowTitle('User Review')
        self.setGeometry(300, 300, 400, 300)
        self.show()
