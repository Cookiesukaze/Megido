import comtypes.client
from PyQt5.QtWidgets import QApplication, QFileDialog
import os
from tools import rename_path


def convert_function(ppt_paths, save_path):
    for piece in ppt_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        # 生成文件名为原文件名
        result_path = save_path[0]+"/"+result_name+'.pdf'
        result_path = rename_path.rename_path_function(result_path)
        # 把正斜杠替换成反斜杠
        result_path = result_path.replace('/', '\\')
        ppt = comtypes.client.CreateObject("Powerpoint.Application", dynamic=True)
        ppt.Visible = 1
        result = ppt.Presentations.Open(piece)
        result.SaveAs(result_path, 32)
        result.close()
    return


def get_file_path():
    desktop_path = get_desktop_path()
    file_filter = "*pptx"
    app = QApplication([])
    file_dialog = QFileDialog()
    # 设置可选文件类型为存在的多个文件
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    # 设置打开窗口名
    file_dialog.setWindowTitle("选择一个或多个ppt文件")
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
2.如果可以的话希望ppt不要显示在前台
3.原名称命名生成文件 ✓
2.文件名选择 不想写，感觉没太大必要了
3.图片质量选择
'''