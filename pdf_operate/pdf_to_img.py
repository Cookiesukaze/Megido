import fitz
import os
from tools import rename_path, get_path


def convert_function(pdf_paths, save_path):
    for piece in pdf_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        # 生成文件夹名为原文件名
        result_path = save_path + "/" + result_name
        result_path = rename_path.rename_path_function(result_path)
        if not os.path.exists(result_path):
            os.mkdir(result_path)
        # 打开pdf
        pdf = fitz.open(piece)
        for page_num in range(pdf.pageCount):
            img_name = "img({}).png".format(page_num+1)
            print(img_name)
            page = pdf[page_num]
            rotate = int(0)
            zoom_x, zoom_y = 5, 5  # 缩放5倍
            matrix = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            result = page.get_pixmap(matrix=matrix, alpha=False)
            result.save(os.path.join(result_path, img_name))
    return


if __name__ == "__main__":
    convert_function(get_path.get_pdf_file_path(), get_path.get_save_path())

'''
1.自定义的图片缩放
2.自定义的图片格式
'''