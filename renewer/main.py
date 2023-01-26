import pandas as pd
import yaml

data = pd.read_csv('D:/PycharmWorkspace/renewer/test.csv')
print(data.head())


with open('dev.yaml_template') as f:
    film = yaml.load(f, Loader=yaml.FullLoader)
    pd.options.dis


