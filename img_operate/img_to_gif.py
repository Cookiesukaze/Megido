from tools import rename_path, get_path, sort_file
from PIL import Image


def convert_function(img_paths, save_path):
    result_path = save_path + "/spawn.gif"
    result_path = rename_path.rename_path_function(result_path)
    duration = 800
    loop = 0
    spawn_gif = [Image.open(img_path) for img_path in img_paths]
    spawn_gif[0].save(result_path, format='GIF', append_images=spawn_gif[1:], save_all=True, duration=duration, loop=loop)
    return


if __name__ == "__main__":
    convert_function(sort_file.get_sorted_file_path(get_path.get_img_file_path()), get_path.get_save_path())

'''
1.自定义间断、自定义是否循环
2.处理大小不一的图片
'''
