import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton

# 自定义窗口类
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # 设置界面的语句单独调一个函数，显得__init__方法不那么臃肿
    # 实现多个布局器并存 ————> 嵌套方法，最外面一个垂直布局，里面嵌套一个垂直布局和一个水平布局
    def init_ui(self):
        # 最外层的垂直布局，包含爱好和性别
        container = QVBoxLayout()

        # 创建第一个组，里面可以添加多个组件
        # hobby_box保证他们是同一个组
        hobby_box = QGroupBox('爱好')
        # v_layout保证三个爱好是垂直摆放
        v_layout = QVBoxLayout()
        # 创建按钮
        btn1 = QRadioButton('男同')
        btn2 = QRadioButton('男娘')
        btn3 = QRadioButton('原神')
        # 添加到v_layout中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 把v_layout添加到hobby_box中
        hobby_box.setLayout(v_layout)

        # 创建第二个组
        gender_box = QGroupBox('性别')
        # 性别容器
        h_layout = QHBoxLayout()
        # 添加组件
        btn4 = QRadioButton('男')
        btn5 = QRadioButton('女')
        # 添加到性别容器里
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # 添加到box里
        gender_box.setLayout(h_layout)

        # 把爱好和性别的内容添加到容器中
        container.addWidget(hobby_box)
        container.addWidget(gender_box)

        self.setLayout(container)

if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)

    # 创建窗口 ——> 自定义
    w = MyWindow()

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()