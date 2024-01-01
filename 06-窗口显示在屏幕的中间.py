import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

if __name__ == '__main__':
    # 创建QApplication对象
    app = QApplication(sys.argv)

    # 创建窗口
    w = QWidget()

    # 将窗口设置在屏幕左上角（所有位置都采用像素坐标）
    w.move(0, 0)

    # 调整窗口在屏幕中央显示
    '''
        （1）QDesktopWidget() ——————> 获取当前屏幕的组件
        （2）availableGeometry() ———> 所有可用的坐标范围
        （3）center() ——————————————> 可用坐标范围的中央
    '''
    center_pointer = QDesktopWidget().availableGeometry().center()

    # 获取中央位置的横纵坐标
    x = center_pointer.x()
    y = center_pointer.y()

    # 窗口移动到中央 ——————> 发现当前窗口的左上角是屏幕中央，即窗口位于屏幕中心的右下处
    # 解决方法：x和y分别减去当前窗口宽和高的一半
    w.move(x, y)

    # 获取窗口的数据
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - width / 2, y - height / 2)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec_()