from docx2pdf import convert
from PyQt5.QtWidgets import QApplication, QFileDialog
import os
from tools import rename_path, change_extension
from time import sleep


def convert_function(word_paths, save_path):
    for piece in word_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        # doc统一转换成docx
        if extension == '.doc':
            word_path = change_extension.doc_to_docx_function(piece, save_path[0])
        else:
            word_path = piece
        # docx统一转换成pdf
        result_path = save_path[0] + "/" + result_name + '.pdf'
        result_path = rename_path.rename_path_function(result_path)
        f = open(result_path, 'w')
        f.close()
        convert(word_path, result_path)
        # sleep是必需的否则会报错
        sleep(3)
    return


def get_file_path():
    desktop_path = get_desktop_path()
    file_filter = "*doc *docx"
    app = QApplication([])
    file_dialog = QFileDialog()
    # 设置可选文件类型为存在的多个文件
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    # 设置打开窗口名
    file_dialog.setWindowTitle("选择一个或多个word文档文件")
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
1.批量选择ppt ✓
2.当前的doc是转换成docx后放到保存路径的
3.原名称命名生成文件 ✓
4.图片质量选择
'''