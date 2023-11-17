# -*- coding: utf-8 -*-
import numpy as np
import networkx as nx
import pandas as pd

from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QSizePolicy)
from PyQt5.QtGui import (QImage, QPixmap, QPalette)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class CustomWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('File:'), 0, 0)
        grid.addWidget(QLabel('Status:'), 1, 0)
        grid.addWidget(QLabel('Diagram:'), 2, 0)

        grid.addWidget(self.handlerLineEdit(), 0, 1)
        grid.addWidget(self.handlerTextEditor(), 1, 1)
        grid.addWidget(self.handlerCanvasEditor(), 2, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 600)
        self.show()

    def handlerLineEdit(self):
        self.line1 = QLineEdit()
        return self.line1

    def handlerTextEditor(self):
        self.edit1 = QTextEdit()
        return self.edit1

    def handlerCanvasEditor(self):
        self.image1 = Canvas()
        # self.image1.ax.clear()
        # self.image1.ax.imshow(np.zeros((200, 300), dtype=np.uint8))
        return self.image1
    
    
class Canvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.parent = parent
        self.plot()

    def plot(self):
        df = pd.read_excel('filtered_data.xlsx')  # filtered_data.xlsx 파일 읽기, 파일명은 실제 파일명으로 변경해주세요

        unique_processes = df['LCA_Process'].unique()  # 'LCA_Process' 열에서 중복을 제거한 고유한 값들 얻기

        G = nx.Graph()

        # Add nodes
        G.add_nodes_from(unique_processes)

        # Add edges
        edges = df.groupby('LCA_Process')['Material'].apply(list).reset_index()  # 'Material'을 리스트로 그룹화
        for i, row in edges.iterrows():
            process = row['LCA_Process']
            materials = row['Material']
            for material in materials:
                if material in unique_processes and material != process:
                    G.add_edge(process, material)

        # Manually set node positions for a linear layout
        pos = {node: (0, -i) for i, node in enumerate(unique_processes)}  # 수동으로 좌표 설정

        # Draw nodes
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', ax=self.ax, font_weight='bold', node_size=1000, font_size=10)

        # Draw edges
        for edge in G.edges():
            start_node, end_node = edge
            x = [pos[start_node][0], pos[end_node][0]]
            y = [pos[start_node][1], pos[end_node][1]]
            self.ax.plot(x, y, color='black')  # 각 노드 사이에 선을 그립니다.

        self.draw()


