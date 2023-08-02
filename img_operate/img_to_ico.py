from PIL import Image
import os
from tools import rename_path, get_path


def convert_function(img_paths, save_path):
    for piece in img_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        result_path = save_path + "/" + result_name + '.ico'
        result_path = rename_path.rename_path_function(result_path)
        ico_size = [(128, 128)]
        img = Image.open(piece)
        img.save(result_path, sizes=ico_size)
    return


if __name__ == "__main__":
    convert_function(get_path.get_img_file_path(), get_path.get_save_path())

'''
1.可选的ico大小
2.生成ico似乎宽高异常，等待检查
3.简化 ✓
'''