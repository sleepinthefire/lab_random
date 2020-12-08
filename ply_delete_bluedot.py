# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:49:08 2020

@author: mtl98
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('C:/Users/mtl98/Desktop/1.ply') as f:
    data = f.read()
    header = data.split('end_header')[0]
    cutted = data.split('end_header')[1].replace('\n', ' ')
    conma = cutted.split(' ')[1:-1]
    data_array = np.array(conma).reshape(int(len(conma)/9), 9)
    data_array = data_array.astype(float)
    a = data_array[~np.any(data_array >= 200, axis=1), :]
    kara = []
    karakara = []
    edit = a.astype(str).tolist()

    for n, li in enumerate(edit):
        if n != len(edit):
            li.append('\n')
        kara.append(li)
    for li in kara:
        count = 0
        for l in li:
            if count==0:
                karakara.append(l)
            elif count in [6,7,8]:
                karakara.append(' ' + str(int(float(l))))
            else:
                karakara.append(' ' + l)
            count += 1
    karakara = ''.join(karakara)
    edit_file = header + "end_header\n" + karakara

with open("C:/Users/mtl98/Desktop/1_edit.ply", mode='w') as f:
    f.write(edit_file)
