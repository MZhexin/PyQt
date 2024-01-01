import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()

    # 输入框对象
    edit = QLineEdit(w)

    # 设置文本
    edit.setPlaceholderText('请输入账号')

    # 设置几何形状（x、y、w、h）
    edit.setGeometry(55, 20, 300, 40)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()