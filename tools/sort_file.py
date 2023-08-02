import os
import sys
import tkinter as tk
from tkinter import ttk
import time


def exit_program():
    sys.exit()


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
        self.tree = ttk.Treeview(self, columns=("路径", "大小", "修改时间"), show="headings")
        self.tree.column("路径", width=300, anchor="w")
        self.tree.column("大小", width=100, anchor="e")
        self.tree.column("修改时间", width=150, anchor="e")
        self.tree.heading("路径", text="路径", command=lambda: self.sort_by_column("路径"))
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
        sort_by_path_button = ttk.Button(self, text="按路径排序", command=lambda: self.sort_files_by_column("路径"))
        sort_by_size_button = ttk.Button(self, text="按大小排序", command=lambda: self.sort_files_by_column("大小"))
        sort_by_time_button = ttk.Button(self, text="按时间排序", command=lambda: self.sort_files_by_column("修改时间"))
        close_button = ttk.Button(self, text="确定", command=self.close_window)
        sort_by_path_button.pack(side="left", padx=5, pady=5)
        sort_by_size_button.pack(side="left", padx=5, pady=5)
        sort_by_time_button.pack(side="left", padx=5, pady=5)
        close_button.pack(side="right", padx=5, pady=5)

        self.protocol("WM_DELETE_WINDOW", exit_program)

    def load_files(self):
        for file_path in self.file_paths:
            file_size = os.path.getsize(file_path)
            file_time = os.path.getmtime(file_path)
            file_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_time))
            self.tree.insert("", "end", values=(file_path, file_size, file_time))

    def sort_by_column(self, column):
        if self.sort_column == column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = column
            self.sort_reverse = False
        self.sort_files_by_column(column)

    def sort_files_by_column(self, column):
        items = [(self.tree.set(child, column), child) for child in self.tree.get_children("")]
        items.sort(reverse=self.sort_reverse)
        for index, (value, child) in enumerate(items):
            self.tree.move(child, "", index)

        # 重置所有列标题
        for col in ("路径", "大小", "修改时间"):
            if col == column:
                self.tree.heading(col, text=col + (" ▼" if self.sort_reverse else " ▲"))
            else:
                self.tree.heading(col, text=col)

    def close_window(self):
        self.file_paths = [self.tree.set(child, "路径") for child in self.tree.get_children("")]
        self.quit()

    # 拖放处理程序
    def on_button_press(self, event):
        self._dragged_item = self.tree.identify_row(event.y)
        if self._dragged_item == "":
            return
        self.tree.selection_set(self._dragged_item)

    def on_motion(self, event):
        if hasattr(self, '_dragged_item'):
            self.tree.selection_remove(self._dragged_item)
            self.tree.move(self._dragged_item, "", event.y // 60)
            self.tree.selection_set(self._dragged_item)

    def on_button_release(self, event):
        if hasattr(self, '_dragged_item'):
            del self._dragged_item


def get_sorted_file_path(file_paths):
    app = FileListWindow(file_paths)
    app.mainloop()
    sorted_paths = app.file_paths
    print("文件顺序：")
    for path in sorted_paths:
        print(path)
    return sorted_paths
