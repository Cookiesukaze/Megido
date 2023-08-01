import comtypes.client
import os
from tools import rename_path, get_path


def convert_function(ppt_paths, save_path):
    for piece in ppt_paths:
        result_name, extension = os.path.splitext(piece)
        result_name = result_name.split("/")[-1]
        # 生成文件名为原文件名
        result_path = save_path + "/" + result_name + '.pdf'
        result_path = rename_path.rename_path_function(result_path)
        # 把正斜杠替换成反斜杠
        result_path = result_path.replace('/', '\\')
        ppt = comtypes.client.CreateObject("Powerpoint.Application", dynamic=True)
        ppt.Visible = 1
        result = ppt.Presentations.Open(piece)
        result.SaveAs(result_path, 32)
        result.close()
    return


if __name__ == "__main__":
    convert_function(get_path.get_ppt_file_path(), get_path.get_save_path())

'''
1.批量选择ppt ✓
2.如果可以的话希望ppt不要显示在前台
3.原名称命名生成文件 ✓
4.文件名选择 不想写，感觉没太大必要了
5.图片质量选择
6.简化 ✓
'''