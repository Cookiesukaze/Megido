from pdf2docx import Converter
import os
from tools import rename_path, get_path


def convert_function(pdf_paths, save_path):
    for piece in pdf_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        # 生成文件名为原文件名
        result_path = save_path + "/" + result_name + '.docx'
        result_path = rename_path.rename_path_function(result_path)
        result = Converter(piece)
        result.convert(result_path, start=0, end=None)
        result.close()
    return


if __name__ == "__main__":
    convert_function(get_path.get_pdf_file_path(), get_path.get_save_path())

'''
1.批量选择pdf ✓
2.原名称命名生成文件 ✓
3.文件名选择 不想写，感觉没太大必要了
4.图片质量选择
5.效果欠佳：公式转换的效果很差，识别不了粗体等
6.简化 ✓
'''