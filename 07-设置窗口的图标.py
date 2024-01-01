import sys
import os.path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()

    # 获取图像的绝对路径
    path = os.path.abspath('Genshin Impact.png')

    # 设置图标 ——————> QIcon需要绝对路径才能显示图标
    w.setWindowIcon(QIcon(path))

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()