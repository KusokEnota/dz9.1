import pandas as pd

data = pd.read_csv('sample_data/california_housing_train.csv')
average_house_price = data.loc[(data['population'] >= 0) & (data['population'] <= 500), 'median_house_value'].mean()

print("Средняя стоимость дома при количестве людей от 0 до 500:", average_house_price)
