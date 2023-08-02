import sys
import tkinter as tk


def exit_program():
    sys.exit(0)


class IconSizeChooser(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('选择图标大小')

        # 图标大小的选项
        self.icon_sizes = [16, 32, 64, 128]
        self.selected_size = tk.IntVar()

        # 创建单选按钮
        for i, size in enumerate(self.icon_sizes):
            radiobutton = tk.Radiobutton(self, text=f"{size} × {size}", variable=self.selected_size, value=size)
            radiobutton.grid(row=0, column=i, padx=10, pady=5)

        self.selected_size.set(128)

        # 创建确定按钮
        self.ok_button = tk.Button(self, text='确定', command=self.destroy)
        self.ok_button.grid(row=1, column=0, columnspan=len(self.icon_sizes), padx=10, pady=0)

        self.protocol("WM_DELETE_WINDOW", exit_program)

    def get_selected_size(self):
        # 获取用户选择的图标大小
        return self.selected_size.get()
