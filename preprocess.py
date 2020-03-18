import re
import os

def rm_tags(text):
    re_tag = re.compile(r'<[^>]+>')
    return re_tag.sub('', text)

def read_files(filetype):
    path = "D:/pythonWork/IMDb/aclImdb/"
    file_list = []

    positive_path = path + filetype + "/pos/"

    for f in os.listdir(positive_path):
        file_list += [positive_path + f]

    negative_path = path + filetype + "/neg/"

    for f in os.listdir(negative_path):
        file_list += [negative_path + f]
    
    print('read', filetype, 'files:', len(file_list))

    all_labels = ([1] * 12500 + [0] * 12500)
    all_texts = []

    for fi in file_list:
         with open(fi, encoding = 'utf8') as file_input:
             all_texts += [rm_tags(" ".join(file_input.readlines()))]

    return all_labels, all_texts