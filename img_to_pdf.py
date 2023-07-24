import img2pdf
from PyQt5.QtWidgets import QApplication,QFileDialog


def convert_function(img_paths):
    result = "spawn.pdf"
    with open(result, "wb") as f:
        f.write(img2pdf.convert(img_paths))
        return result


def file_choose():
    app = QApplication([])
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFiles)
    if file_dialog.exec_():
        file_paths = file_dialog.selectedFiles()
        # file_paths = file_paths[::-1]
        # for file_path in file_paths:
        #     print(file_path)
        print("多选文件列表：")
        print("%s" % file_paths)
        convert_function(file_paths)


if __name__ == "__main__":
    file_choose()
