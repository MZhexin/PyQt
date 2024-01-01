'''
    1. QWidget
        控件和窗口的父类，自由度高（什么都没有），没有划分菜单栏、工具栏、状态栏、主窗口等区域
    2. QMainWindow
        QWidget的子类，包含菜单、工具栏、状态栏、标题栏等，中间部分则为主窗口区域
    3. QDialog
        对话框窗口的基类，一般不应该作为主窗口，而是通过点击操作弹出，起到提示作用
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QLabel, QPushButton

class Window1_QWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel('这是文字')
        label.setStyleSheet('font-size:30px;color:red')
        label.setParent(self)

class Window2_QMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel('这是文字')
        label.setStyleSheet('font-size:30px;color:red')

        # 调用父类中的menuBar，从而对菜单栏进行操作
        menu = self.menuBar()

        file_menu = menu.addMenu("文件")
        file_menu.addAction("新建")
        file_menu.addAction("打开")
        file_menu.addAction("保存")

        edit_menu = menu.addMenu("编辑")
        edit_menu.addAction("复制")
        edit_menu.addAction("粘贴")
        edit_menu.addAction("剪切")

        # 设置中心内容显示
        self.setCentralWidget(label)

class Window3_QDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        ok_btn = QPushButton("确定", self)
        ok_btn.setGeometry(50, 50, 100, 30)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w1 = Window1_QWidget()
    w2 = Window2_QMainWindow()
    w3 = Window3_QDialog()

    w1.setWindowTitle("这是标题")
    w2.setWindowTitle("这是标题")
    w3.setWindowTitle("对话框")

    w1.show()
    w2.show()
    w3.show()

    app.exec_()