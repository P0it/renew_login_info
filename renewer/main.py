import pandas as pd
import yaml
import sys
from device import DeviceInfo


# class( inherit )
class FirstDevice(DeviceInfo):
    pass


class SecondDevice(DeviceInfo):
    pass


def renew_login():
    # csv 파일 읽기
    data = pd.read_csv(file_path)
    print(data)

    # 클래스 생성자 초기화
    fd = FirstDevice()
    sd = SecondDevice()
    # 갱신 정보 객체에 저장
    for item in data.values:
        if item[0] == '10.10.249.20':
            fd.set_host(item[1])
            fd.set_port(item[2])
            fd.set_id(item[3])
            fd.set_pwd(item[4])
            fd.set_enable(item[5])

        if item[0] == '10.10.250.22':
            sd.set_host(item[1])
            sd.set_port(item[2])
            sd.set_id(item[3])
            sd.set_pwd(item[4])
            sd.set_enable(item[5])

        else:
            pass

    with open('src/dev.yaml') as f:
        list_doc = yaml.safe_load(f)
        device_list = list_doc['devices']
        print(list_doc)
        print(list_doc['devices']['OL_L3_48T']['type'])

        # list_doc['devices']['OL_L3_48T']['type'] = 'router'

    with open("src/dev.yaml", "w") as f:
        yaml.dump(list_doc, f)
        print("수정완료")


# 메인 실행 함수
if len(sys.argv) < 2:
    print("--- Downloading ---")
    # TODO file_path 테스트 후에 삭제
    file_path = 'src/test.csv'
    renew_login()
    # method: yaml -> csv


elif len(sys.argv) == 2:
    print("--- Renewing ---")
    # method: csv -> yaml
    # TODO file_path 테스트 후에 원복
    # file_path = sys.argv[1]
    file_path = 'src/test.csv'
    renew_login()

else:
    print("Only single csv file is required.")
