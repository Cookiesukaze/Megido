from PIL import Image
import os
from tools import rename_path, get_path, type_chooser


def convert_function(img_paths, save_path, ico_size_input):
    for piece in img_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        result_path = save_path + "/" + result_name + '.ico'
        result_path = rename_path.rename_path_function(result_path)
        img = Image.open(piece)
        img = img.resize((ico_size_input, ico_size_input))  # 调整图像大小
        img.save(result_path, sizes=[(ico_size_input, ico_size_input)])
    return


if __name__ == "__main__":
    ico_size_chooser = type_chooser.IconSizeChooser()
    ico_size_chooser.mainloop()
    ico_size = ico_size_chooser.get_selected_size()

    convert_function(get_path.get_img_file_path(), get_path.get_save_path(), ico_size)

'''
1.可选的ico大小 ✓
2.生成ico似乎宽高异常，等待检查 ✓
3.简化 ✓
'''
