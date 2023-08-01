from docx2pdf import convert
import os
from tools import rename_path, change_extension, get_path
from time import sleep


def convert_function(word_paths, save_path):
    for piece in word_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        # doc统一转换成docx
        if extension == '.doc':
            word_path = change_extension.doc_to_docx_function(piece, save_path)
        else:
            word_path = piece
        # docx统一转换成pdf
        result_path = save_path + "/" + result_name + '.pdf'
        result_path = rename_path.rename_path_function(result_path)
        f = open(result_path, 'w')
        f.close()
        convert(word_path, result_path)
        # sleep是必需的否则会报错
        sleep(3)
    return


if __name__ == "__main__":
    convert_function(get_path.get_word_file_path(), get_path.get_save_path())

'''
1.批量选择doc ✓
2.当前的doc是转换成docx后放到保存路径的
3.原名称命名生成文件 ✓
4.图片质量选择
5.简化 ✓
'''