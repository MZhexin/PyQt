'''
    布局 ————> 即界面的一种排列方式
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

# 自定义窗口类
class MyWindow(QWidget):
    def __init__(self):
        # 切记一定要调用父类的init方法，里面包含很多UI空间的初始化语句
        super().__init__()

        # 设置大小
        self.resize(400, 400)

        # 设置标题
        self.setWindowTitle('垂直布局')

        # 创建一个垂直布局的布局器 ————> 布局器是一种约束，在界面上看不到的
        # 一个Widget只能有一个布局器，但通过布局器的嵌套，实现一个窗口有多个布局器的情况
        # V是垂直Vertical的首字母
        layout = QVBoxLayout()

        # 添加一个伸缩器（理解为弹簧），按比例关系来压缩、分配布局器的空间
        layout.addStretch(1)

        # 创建按钮1
        btn1 = QPushButton('按钮1')
        # 把刚刚创建的按钮添加到刚刚创建的布局器中
        layout.addWidget(btn1)

        # 伸缩器比例关系1:2
        layout.addStretch(2)

        # 同理，再创建两个按钮
        # 按钮2
        btn2 = QPushButton('按钮2')
        layout.addWidget(btn2)
        # 按钮3
        btn3 = QPushButton('按钮3')
        layout.addWidget(btn3)

        # 前面写比例，这里不写比例，就是等于比例为0，即仨伸缩器比例关系是1:2:0
        layout.addStretch()

        # 让当前的窗口使用布局器layout的排列规则
        self.setLayout(layout)

if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)

    # 创建窗口 ——> 自定义
    w = MyWindow()

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()