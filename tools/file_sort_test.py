import os
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QListWidget, \
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QListWidgetItem
from PyQt5.QtCore import Qt


class DragDropListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(QListWidget.InternalMove)
        self.setSelectionMode(QListWidget.ExtendedSelection)
        self.setDragEnabled(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            super().dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            for url in event.mimeData().urls():
                file_path = str(url.toLocalFile())
                item = QListWidgetItem(file_path)
                self.addItem(item)
        else:
            super().dropEvent(event)


class FileListWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化界面元素
        self.file_list_widget = DragDropListWidget()
        self.file_list_widget.setSelectionMode(QListWidget.ExtendedSelection)
        self.sort_by_name_button = QPushButton("按名称排序")
        self.sort_by_size_button = QPushButton("按大小排序")
        self.sort_by_time_button = QPushButton("按时间排序")
        self.sort_label = QLabel("")
        self.close_button = QPushButton("确定")

        # 设置界面布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.sort_by_name_button)
        hbox.addWidget(self.sort_by_size_button)
        hbox.addWidget(self.sort_by_time_button)
        vbox = QVBoxLayout()
        vbox.addWidget(self.file_list_widget)
        vbox.addWidget(self.sort_label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.close_button)
        self.setLayout(vbox)

        # 绑定界面元素的事件处理函数
        self.sort_by_name_button.clicked.connect(self.sort_files_by_name)
        self.sort_by_size_button.clicked.connect(self.sort_files_by_size)
        self.sort_by_time_button.clicked.connect(self.sort_files_by_time)
        self.close_button.clicked.connect(self.close_window)

        # 设置窗口标题
        self.setWindowTitle("自定义排序")

    def sort_files_by_name(self):
        items = [(self.file_list_widget.item(i).text(), i) for i in range(self.file_list_widget.count())]
        items.sort()
        self.file_list_widget.clear()
        for item, _ in items:
            self.file_list_widget.addItem(item)
        self.sort_label.setText("已按名称排序")

    def sort_files_by_size(self):
        items = [(os.path.getsize(self.file_list_widget.item(i).text()), self.file_list_widget.item(i).text(), i)
                 for i in range(self.file_list_widget.count())]
        items.sort(reverse=True)
        self.file_list_widget.clear()
        for _, item, _ in items:
            self.file_list_widget.addItem(item)
        self.sort_label.setText("已按大小排序")

    def sort_files_by_time(self):
        items = [(os.path.getmtime(self.file_list_widget.item(i).text()), self.file_list_widget.item(i).text(), i)
                 for i in range(self.file_list_widget.count())]
        items.sort(reverse=True)
        self.file_list_widget.clear()
        for _, item, _ in items:
            self.file_list_widget.addItem(item)
        self.sort_label.setText("已按时间排序")

    def close_window(self):
        self.close()


def get_sorted_file_path(file_paths):
    app = QApplication([])
    # 创建文件列表窗口并显示文件列表
    file_list_window = FileListWindow()
    for file_path in file_paths:
        item = QListWidgetItem(file_path)
        file_list_window.file_list_widget.addItem(item)
    file_list_window.show()
    app.exec_()
    # 打印文件排序后的顺序
    sorted_items = [file_list_window.file_list_widget.item(i).text()
                    for i in range(file_list_window.file_list_widget.count())]
    print("文件顺序：")
    for item in sorted_items:
        print(item)

    # 返回选择的文件路径列表
    return sorted_items


'''
需要自定义排序的工具有：merge_pdf、img_to_pdf
'''
