import tkinter as tk
from PIL import Image, ImageTk
from tools import get_path, rename_path
import os
import sys


class Pixelator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.pixelated_image = None
        self.title("像素化你的图片")
        self.file_path = get_path.get_single_img_file_path()
        self.original_image = Image.open(self.file_path)
        self.max_image_size = (800, 800)
        self.original_image.thumbnail(self.max_image_size)
        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.scale = tk.Scale(self, from_=1, to=100, orient="horizontal", command=self.update_image)
        self.scale.pack()

        self.save_button = tk.Button(self, text="保存", command=self.save_image)
        self.save_button.pack()

        self.update_image()

    def pixelate(self, pixel_size):
        image = self.original_image.resize(
            (self.original_image.size[0] // pixel_size, self.original_image.size[1] // pixel_size),
            Image.NEAREST
        )
        image = image.resize(
            self.original_image.size,
            Image.NEAREST
        )
        return image

    def update_image(self):
        pixel_size = max(1, self.scale.get())
        self.pixelated_image = self.pixelate(pixel_size)
        photo_image = ImageTk.PhotoImage(self.pixelated_image)
        self.image_label.configure(image=photo_image)
        self.image_label.image = photo_image

    def save_image(self):
        save_path = get_path.get_save_path()
        if save_path:
            self.save_image_to_path(save_path)
            sys.exit(0)  # 退出程序

    def save_image_to_path(self, path):
        result_name, extension = os.path.splitext(self.file_path)
        result_name = result_name.split("/")[-1]
        result_path = path + "/" + result_name + '.png'  # 默认保存为png
        result_path = rename_path.rename_path_function(result_path)
        self.pixelated_image.save(result_path)


if __name__ == "__main__":
    app = Pixelator()
    app.mainloop()

'''
1.批量选择
'''
