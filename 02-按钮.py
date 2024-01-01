import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()

    # 在窗口里添加控件
    btn = QPushButton('按钮')

    # 设置按钮的父对象是当前窗口，等于是将当前控件添加到窗口中显示
    # 新控件想放在哪个窗口中，就将父对象设为哪个窗口（窗口嵌套时选最里面的）
    btn.setParent(w)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()
