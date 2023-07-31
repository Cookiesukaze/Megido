from PIL import Image
from PyQt5.QtWidgets import QApplication, QFileDialog
import os
from tools import rename_path, change_extension


def convert_function(img_paths, save_path):
    for piece in img_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        result_path = save_path[0] + "/" + result_name + '.ico'
        result_path = rename_path.rename_path_function(result_path)
        ico_size = [(128, 128)]
        img = Image.open(piece)
        img.save(result_path, sizes=ico_size)
    return


def get_file_path():
    desktop_path = get_desktop_path()
    file_filter = "*jpeg *.jpg *.png"
    app = QApplication([])
    file_dialog = QFileDialog()
    # 设置可选文件类型为存在的多个文件
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    # 设置打开窗口名
    file_dialog.setWindowTitle("选择一张或多张图片")
    # 设置打开目录
    file_dialog.setDirectory(desktop_path)
    # 设置过滤器
    file_dialog.setNameFilter(file_filter)
    if file_dialog.exec_():
        file_paths = file_dialog.selectedFiles()
        return file_paths


def get_desktop_path():
    return os.path.join(os.path.expanduser('~'), "Desktop")


def get_save_path():
    desktop_path = get_desktop_path()
    app = QApplication([])
    save_dialog = QFileDialog()
    # 设置可选文件类型为目录
    save_dialog.setFileMode(QFileDialog.Directory)
    # 设置打开窗口名
    save_dialog.setWindowTitle("选择保存路径")
    # 设置打开目录
    save_dialog.setDirectory(desktop_path)
    if save_dialog.exec_():
        save_path = save_dialog.selectedFiles()
        # print(save_path)
        return save_path


if __name__ == "__main__":
    convert_function(get_file_path(), get_save_path())

'''
1.可选的ico大小
2.生成ico似乎宽高异常，等待检查
2.尝试手动删除不必要文件并打包，否则不再采用pyqt5，甚至不再采用桌面应用
3.尝试简化所有代码
'''