import pandas as pd
import yaml

data = pd.read_csv('D:/PycharmWorkspace/renewer/src/test.csv')
print(data.head())


with open('src/dev.yaml_template') as f:
    film = yaml.load(f, Loader=yaml.FullLoader)
    pd.options.dis


