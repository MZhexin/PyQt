import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QVBoxLayout, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 固定窗口大小
        self.setFixedSize(400, 250)

        # 外层容器
        container = QVBoxLayout()

        # 表单容器
        form_layout = QFormLayout()

        # 创建第一个输入框
        edit1 = QLineEdit()
        edit1.setPlaceholderText('请输入账号')
        form_layout.addRow('账号：', edit1)

        # 创建另一个输入框
        edit2 = QLineEdit()
        edit2.setPlaceholderText('请输入密码')
        form_layout.addRow('密码：', edit2)

        # 将lay_out添加到垂直布局器中
        container.addLayout(form_layout)

        # 按钮
        login_btn = QPushButton('登录')
        login_btn.setFixedSize(100, 30)

        # 把按钮添加到容器中，并且指定对齐方式
        container.addWidget(login_btn, alignment=Qt.AlignRight)

        self.setLayout(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()

    w.show()

    app.exec_()