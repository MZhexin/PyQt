import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt程序")

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()
