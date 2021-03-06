import pandas as pd
import numpy as np
import re
import csv_dealer as csv

def main():
  #原材料データの取得
  f = csv.import_csv("../csv/ingredient3.csv").values.tolist()
  f_list = [f[i][1] for i in range(len(f))]

  #()とその内部の情報の除去
  elements = brackets_eraser(f_list)

  #バイナリデータに変換
  matrix = []
  matrix.append(elements.tolist())
  matrix[1:] = Binarization(elements,f_list)

  #csvに出力
  csv.export_csv("../csv/output.csv",matrix)

def brackets_eraser(list):
  elements = []
  for index in range(len(list)):
    for k in re.split('[(（]', list[index])[0].split('、'):
      if k.split('／')[0] != '':
        elements.append(k.split('／')[0])
    for i in re.split('[(（]', list[index])[1:]:
      if len(re.split('[)）]', i)) > 1:
        for m in (re.split('[)）]', i)[1]).split('、'):
          if m.split('／')[0] != '':
            elements.append(m.split('／')[0])
  return np.unique(elements)

def Binarization(elements,f_list):
  binary = np.zeros((len(f_list),len(elements)),dtype = int )
  for i in range(len(f_list)):
    for j in range(len(elements)):
      if elements[j] in f_list[i]:
        binary[i][j] = 1
  return binary.tolist()

if __name__ == '__main__':
    main()
