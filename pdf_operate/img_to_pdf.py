import img2pdf
from PyQt5.QtWidgets import QApplication, QFileDialog
import os
from tools import rename_path


def convert_function(img_paths, save_path):
    result_path = save_path[0]+"/spawn.pdf"
    result_path = rename_path.rename_path_function(result_path)
    with open(result_path, "wb") as f:
        f.write(img2pdf.convert(img_paths))
        f.close()
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
        # file_paths = file_paths[::-1]
        # for file_path in file_paths:
        #     print(file_path)
        # print("多选文件列表：")
        # print("%s" % file_paths)
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
1.起始路径确定 ✓
2.文件类型筛选 ✓
3.保存路径选择 ✓
4.文件名选择 不想写，感觉没太大必要了
5.图片质量选择
'''