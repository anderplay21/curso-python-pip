from pathlib import Path

import utils
import read_csv
import charts

BASE_DIR = Path(__file__).resolve().parent


def run():

  data = read_csv.read_csv(BASE_DIR / 'data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = [float(x['World Population Percentage']) for x in data]

  charts.generate_pie_chart(countries, percentages)
  charts.generate_bar_chart(countries, percentages)

  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country_data = result[0]
    print(country_data)
    labels, values = utils.get_population(country_data)
    charts.generate_pie_chart(list(labels), list(values))

if __name__ == '__main__':
  run()