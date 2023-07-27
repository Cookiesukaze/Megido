import os
from win32com import client as wc


def doc_to_docx_function(source_file_path, destination_file_path):
    result_name, extension = os.path.splitext(source_file_path)
    result_name = result_name.split("/")[-1]
    word = wc.Dispatch("Word.Application")
    doc = word.Documents.Open(source_file_path)
    new_file_path = destination_file_path + "/" + result_name + '.docx'
    # 12为docx
    doc.SaveAs(new_file_path, 12)
    doc.Close()
    word.Quit()
    return new_file_path
