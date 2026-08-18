import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def read_csv(path):
  csv_path = Path(path)
  if not csv_path.is_absolute():
    csv_path = BASE_DIR / csv_path
  with csv_path.open('r', encoding='utf-8', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])