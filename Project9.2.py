import pandas as pd

data = pd.read_csv('sample_data/california_housing_train.csv')
max_households = data[data['population'] == data['population'].min()]['households'].max()

print('Максимальное количество домохозяйств в зоне минимального значения population:', max_households)
