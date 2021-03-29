import binarization as bi
import csv_dealer as csv

def main():
  #データの取得
  data1 = csv.import_csv("../csv/output.csv")
  data2 = csv.import_csv("../csv/meiji_data.csv")

  #データの統合
  data = pd.concat([data1,data2])
  print(data)

  #データ出力
  #bi.export_csv(, data):



if __name__ == '__main__':
    main()