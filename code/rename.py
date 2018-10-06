import os
import numpy as np
import pydicom as dc

# 读original第n个文件个数n
for j in range(20):
    path = "./data/thin/original/" + str(j+1)
    filenum = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))]) - 1
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    for f in files:
        try:
            print(int(f[4:8]))
            src = path + "/" + f
            dst = path + "/" + str(f[4:8]) + ".dcm"
            print(src)
            print(dst)
            os.rename(src, dst)
        except:
            pass
