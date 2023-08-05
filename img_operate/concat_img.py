import tkinter as tk
from PIL import Image, ImageTk
from tools import get_path, sort_file, rename_path


class ImageStitcher:
    def __init__(self, master):
        self.master = master
        self.master.title("自定义拼接图片")
        self.tk_image = None
        self.master = master
        self.image_paths = sort_file.get_sorted_file_path(get_path.get_img_file_path())
        self.stitched_image = None

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.row_label = tk.Label(self.frame, text="Rows")
        self.row_label.pack()
        self.row_entry = tk.Entry(self.frame)
        self.row_entry.pack()

        self.col_label = tk.Label(self.frame, text="Columns")
        self.col_label.pack()
        self.col_entry = tk.Entry(self.frame)
        self.col_entry.pack()

        self.stitch_button = tk.Button(self.frame, text="预览图片", command=self.stitch_images)
        self.stitch_button.pack()

        self.save_button = tk.Button(self.frame, text="保存图片", command=self.save_image)
        self.save_button.pack()

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

    def stitch_images(self):
        rows = int(self.row_entry.get())
        cols = int(self.col_entry.get())

        # 定义一个透明的图片作为填充
        TRANSPARENT_IMAGE = Image.new('RGBA', (1, 1), (0, 0, 0, 0))

        # 获取所有图片的尺寸，找出最大的宽度和高度
        max_width = max_height = 0
        print(self.image_paths)
        images = []
        for path in self.image_paths:
            img = Image.open(path)
            width, height = img.size
            max_width = max(max_width, width)
            max_height = max(max_height, height)
            images.append(img)

        # 调整所有图片的尺寸，使其与最大的宽度和高度一致
        images = [img.resize((max_width, max_height)) if img.size != (max_width, max_height) else img for img in images]

        # 创建一个新的图片，用于存放所有的图片
        self.stitched_image = Image.new('RGBA', (max_width * cols, max_height * rows))

        # 使用Pillow库的ImageGrid方法，将所有的图片拼接在一起
        for i in range(rows):
            for j in range(cols):
                if i * cols + j < len(images):
                    self.stitched_image.paste(images[i * cols + j], (j * max_width, i * max_height))
                else:
                    self.stitched_image.paste(TRANSPARENT_IMAGE.resize((max_width, max_height)),
                                              (j * max_width, i * max_height))

        # 在窗口中预览图片
        self.stitched_image.thumbnail((500, 500))
        self.tk_image = ImageTk.PhotoImage(self.stitched_image)
        self.image_label.config(image=self.tk_image)

    def save_image(self):
        if self.stitched_image is None:
            return
        save_path = get_path.get_save_path() + "/spawn.png"
        save_path = rename_path.rename_path_function(save_path)
        if save_path:
            self.stitched_image.save(save_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageStitcher(root)
    root.mainloop()

'''
!important
1.窗口弹出美化 
2.图片质量检查
3.简化 
'''
