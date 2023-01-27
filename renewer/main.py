import pandas as pd
import yaml
from device import DeviceInfo


# 클래스 생성(상속)
class FirstDevice(DeviceInfo):
    pass


class SecondDevice(DeviceInfo):
    pass


data = pd.read_csv('src/test.csv')

for item in data.values:
    if item[0] == '10.10.249.20':
        FirstDevice.set_host(item[1])
        FirstDevice.set_port(item[2])
        FirstDevice.set_id(item[3])
        FirstDevice.set_pwd(item[4])
        FirstDevice.set_enable(item[5])

    if item[0] == '10.10.250.22':
        SecondDevice.set_port(item[1])
        SecondDevice.set_host(item[2])
        SecondDevice.set_id(item[3])
        SecondDevice.set_pwd(item[4])
        SecondDevice.set_enable(item[5])

    else:
        pass

    print(item)

with open('src/dev.yaml_template') as f:
    list_doc = yaml.safe_load(f)
    device_list = list_doc['devices']

print("---")
print(list_doc)

print(type(list_doc))
print(type(device_list))

print(list_doc['devices']['OL_L3_48T']['type'])

for device in device_list:
    print(type(device))
    if device == "OL_L3_48T":
        pass
    # device['type'] = "router"

with open('src/dev.yaml_template', "w") as f:
    yaml.dump(list_doc, f)
