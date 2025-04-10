import matplotlib.pyplot as plt
import pandas as pd
from sklearn import LinearRegression

def convert_wheels(english_number):
    match english_number:
        case 'eight':
            return 8
        case 'five':
            return 5
        case 'four':
            return 4
        case 'six':
            return 6
        case 'three':
            return 3
        case 'twelve':
            return 12
        case 'two':
            return 2
        case _:
            raise Exception(f"Unexpected value for wheels: {english_number}")

car_data = pd.read_csv('automobile.csv', usecols=[
    'symboling', 'fuel-type', 'aspiration', 'body-style',
    'num-of-cylinders', 'horsepower', 'price'
]).dropna()

car_data['num-of-cylinders'] = car_data['num-of-cylinders'].apply(convert_wheels)

car_data = pd.get_dummies(car_data, columns=['fuel-type', 'aspiration', 'body-style'], drop_first=True)

fig_graph = plt.figure(figsize=(14, 6))
chart_0 = fig_graph.add_subplot(121)
chart_1 = fig_graph.add_subplot(122)

chart_0.scatter(car_data['num-of-cylinders'], car_data['price'])
chart_0.set_xlabel('Number of Cylinders')
chart_0.set_ylabel('Price')
chart_0.set_title('Number of Cylinders vs Price')

chart_1.scatter(car_data['horsepower'], car_data['price'])
chart_1.set_xlabel('Horsepower')
chart_1.set_ylabel('Price')
chart_1.set_title('Horsepower vs Price')

plt.savefig('car_price_comparison.png')
plt.show()

features_matrix = car_data[['symboling', 'fuel-type_gas', 'aspiration_turbo', 'body-style_hardtop',
        'body-style_hatchback', 'body-style_sedan', 'body-style_wagon',
        'num-of-cylinders', 'horsepower']]
target_variable = car_data['price']

regression_model = LinearRegression()
regression_model.fit(features_matrix, target_variable)

for feature, coefficient in zip(regression_model.feature_names_in_, regression_model.coef_):
    print(f'{feature}: {coefficient:.2f}')
