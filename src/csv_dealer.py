import csv
import pandas as pd

def import_csv(path):
  data = pd.read_csv(path, encoding='Shift-JIS')
  return data

def export_csv(path, data):
  with open(path, 'w', encoding='Shift-JIS') as f:
    for i in range(len(data)):
      writer = csv.writer(f, lineterminator='\n')
      writer.writerow(data[i])

