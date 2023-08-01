import PyPDF2
from tools import rename_path, get_path, sort_file


def convert_function(pdf_paths, save_path):
    result_path = save_path+"/spawn.pdf"
    result_path = rename_path.rename_path_function(result_path)
    merger = PyPDF2.PdfMerger()
    for f in pdf_paths:
        merger.append(PyPDF2.PdfReader(f))
    merger.write(result_path)
    return


if __name__ == "__main__":
    convert_function(sort_file.get_sorted_file_path(get_path.get_pdf_file_path()), get_path.get_save_path())

'''
1.以pdf的图片为单位自定义排序
2.简化 50%✓
'''