import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('计算器')

        # 准备数据
        data = {
            0: ['7', '8', '9', '+', '('],
            1: ['4', '5', '6', '-', ')'],
            2: ['3', '2', '1', '*', '<-'],
            3: ['0', '.', '=', '/', 'C']
        }

        # 整体垂直布局
        layout = QVBoxLayout()

        # 输入框
        edit = QLineEdit()
        edit.setPlaceholderText('请输入内容')
        # 把输入框添加到容器
        layout.addWidget(edit)

        # 网格布局（也可以算作九宫格布局）
        grid = QGridLayout()

        # 循环创建追加进去
        # line_number表示第几行，line_data表示当前行的数据
        for line_number, line_data in data.items():
            # 此时col_number表示第几列，number表示要显示的符号
            for col_number, number in enumerate(line_data):
                btn = QPushButton(number)
                grid.addWidget(btn, line_number, col_number)

        layout.addLayout(grid)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()

    app.exec_()