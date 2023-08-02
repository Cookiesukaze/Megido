import os
import tkinter as tk
from tkinter import ttk
import time


class FileListWindow(tk.Tk):
    def __init__(self, file_paths):
        super().__init__()

        # 设置窗口标题
        self.title("自定义排序")

        # 初始化变量
        self.sort_column = None
        self.sort_reverse = False
        self.file_paths = file_paths

        # 创建列表控件
        self.tree = ttk.Treeview(self, columns=("文件名", "大小", "修改时间", "路径"), show="headings")
        self.tree.column("文件名", width=300, anchor="w")
        self.tree.column("大小", width=100, anchor="e")
        self.tree.column("修改时间", width=150, anchor="e")
        self.tree.column("路径", width=0)  # 隐藏路径列
        self.tree.heading("文件名", text="文件名", command=lambda: self.sort_by_column("文件名"))
        self.tree.heading("大小", text="大小", command=lambda: self.sort_by_column("大小"))
        self.tree.heading("修改时间", text="修改时间", command=lambda: self.sort_by_column("修改时间"))
        self.tree.pack(fill="both", expand=True)

        # 加载文件列表
        self.load_files()

        # 注册拖放处理程序
        self.tree.bind("<Button-1>", self.on_button_press)
        self.tree.bind("<B1-Motion>", self.on_motion)
        self.tree.bind("<ButtonRelease-1>", self.on_button_release)

        # 创建按钮
        sort_by_name_button = ttk.Button(self, text="按名称排序", command=lambda: self.sort_files_by_column("文件名"))
        sort_by_size_button = ttk.Button(self, text="按大小排序", command=lambda: self.sort_files_by_column("大小"))
        sort_by_time_button = ttk.Button(self, text="按时间排序", command=lambda: self.sort_files_by_column("修改时间"))
        close_button = ttk.Button(self, text="确定", command=self.close_window)
        sort_by_name_button.pack(side="left", padx=5, pady=5)
        sort_by_size_button.pack(side="left", padx=5, pady=5)
        sort_by_time_button.pack(side="left", padx=5, pady=5)
        close_button.pack(side="right", padx=5, pady=5)

    def load_files(self):
        for file_path in self.file_paths:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_time = os.path.getmtime(file_path)
            file_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_time))
            self.tree.insert("", "end", values=(file_name, file_size, file_time, file_path))

    # ... 其他方法不变 ...

    def close_window(self):
        self.file_paths = [self.tree.set(child, "路径") for child in self.tree.get_children("")]
        self.quit()


def get_sorted_file_path(file_paths):
    app = FileListWindow(file_paths)
    app.mainloop()
    sorted_items = app.file_paths
    print("文件顺序：")
    for item in sorted_items:
        print(item)
    return sorted_items