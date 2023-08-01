import img2pdf
from tools import rename_path, get_path, sort_file


def convert_function(img_paths, save_path):
    result_path = save_path + "/spawn.pdf"
    result_path = rename_path.rename_path_function(result_path)
    with open(result_path, "wb") as f:
        f.write(img2pdf.convert(img_paths))
        f.close()
        return


if __name__ == "__main__":
    convert_function(sort_file.get_sorted_file_path(get_path.get_img_file_path()), get_path.get_save_path())

'''
1.起始路径确定 ✓
2.文件类型筛选 ✓
3.保存路径选择 ✓
4.文件名选择 不想写，感觉没太大必要了
5.图片质量选择
6.简化 50%✓
'''
