import tkinter as tk
from tkinter import filedialog
import os
from PyQt5.QtWidgets import QApplication, QFileDialog


def get_desktop_path():
    return os.path.join(os.path.expanduser('~'), "Desktop")


def get_save_path():
    desktop_path = get_desktop_path()
    save_dialog = tk.Tk()
    save_dialog.withdraw()
    save_dialog.title = '选择保存路径'
    save_dialog.iconbitmap('')
    save_path = filedialog.askdirectory(initialdir=(os.path.expanduser(desktop_path)))
    return save_path


def get_img_file_path():
    desktop_path = get_desktop_path()
    file_filter = (("Img files", "*.jpeg"), ("Img files", "*.jpg"), ("Img files", "*.png"))
    file_dialog = tk.Tk()
    file_dialog.withdraw()
    file_dialog.title = '选择一张或多张图片'
    file_dialog.iconbitmap('')
    file_paths = filedialog.askopenfilenames(initialdir=(os.path.expanduser(desktop_path)), filetypes=file_filter)
    print(file_paths)
    return file_paths


def get_word_file_path():
    desktop_path = get_desktop_path()
    file_filter = (("文档文件", "*.doc"), ("文档文件", "*.docx"))
    file_dialog = tk.Tk()
    file_dialog.withdraw()
    file_dialog.title = '选择一个或多个文档文件'
    file_dialog.iconbitmap('')
    file_paths = filedialog.askopenfilenames(initialdir=(os.path.expanduser(desktop_path)), filetypes=file_filter)
    print(file_paths)
    return file_paths


def get_pdf_file_path():
    desktop_path = get_desktop_path()
    file_filter = (("PDF文件", "*.pdf"),)
    file_dialog = tk.Tk()
    file_dialog.withdraw()
    file_dialog.title = '选择一个或多个PDF文件'
    file_dialog.iconbitmap('')
    file_paths = filedialog.askopenfilenames(initialdir=(os.path.expanduser(desktop_path)), filetypes=file_filter)
    print(file_paths)
    return file_paths


def get_ppt_file_path():
    desktop_path = get_desktop_path()
    file_filter = (("PPT文件", "*.pptx"),)
    file_dialog = tk.Tk()
    file_dialog.withdraw()
    file_dialog.title = '选择一个或多个PPT文件'
    file_dialog.iconbitmap('')
    file_paths = filedialog.askopenfilenames(initialdir=(os.path.expanduser(desktop_path)), filetypes=file_filter)
    print(file_paths)
    return file_paths
