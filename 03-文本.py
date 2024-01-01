import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()

    # 创建纯文本，在创建时指定了父对象，不用单独设置
    label = QLabel('账号', w)

    # 位置与大小：x、y、w、h ————> x和y取像素坐标，从左上角开始
    label.setGeometry(20, 20, 40, 40)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()