import csv
import pandas as pd
import yaml
import sys


def renew_data():
    # import csv file
    data = pd.read_csv(file_path)
    print(data)

    with open('dev.yaml', 'r') as read_file:
        # convert yaml into dic
        contents = yaml.safe_load(read_file)
        device_list = contents['devices']
        # convert dic into 'list' to access by index
        index_list = list(device_list)
        # print(index_list)
        for index in index_list:
            for datum in data.values:
                # check device
                if pd.isna(datum[1]):
                    pass
                else:
                    if datum[1] == index:
                        if pd.isna(datum[0]):
                            pass
                        else:
                            contents['devices'][index]['alias'] = datum[0]
                            contents['devices'][index]['connections']['cli']['ip'] = datum[0]
                        if pd.isna(datum[2]):
                            pass
                        else:
                            contents['devices'][index]['connections']['cli']['port'] = datum[2]
                        if pd.isna(datum[3]):
                            pass
                        else:
                            contents['devices'][index]['credentials']['default']['username'] = datum[3]
                        if pd.isna(datum[4]):
                            pass
                        else:
                            contents['devices'][index]['credentials']['default']['password'] = datum[4]
                        if pd.isna(datum[5]):
                            pass
                        else:
                            contents['devices'][index]['credentials']['enable']['password'] = datum[5]

        with open('dev.yaml', 'w') as dump_file:
            # print(contents)
            yaml.dump(contents, dump_file)


def extract_csv():
    with open('dev.yaml', 'r') as read_file:
        # convert yaml into dic
        contents = yaml.safe_load(read_file)
        print(contents)
        device_list = contents['devices']
        # convert dic into 'list' to access by index
        index_list = list(device_list)
        data = []
        for index in index_list:
            row_data = [contents['devices'][index]['alias'],
                        index,
                        contents['devices'][index]['connections']['cli']['port'],
                        contents['devices'][index]['credentials']['default']['username'],
                        contents['devices'][index]['credentials']['default']['password'],
                        contents['devices'][index]['credentials']['enable']['password']
                        ]
            data.append(row_data)

    header = ['ip', 'hostname', 'ssh_port', 'ssh_id', 'ssh_pwd', 'enable']

    with open('login_info.csv', 'w', encoding='UTF-8', newline='') as write_csv:
        writer = csv.writer(write_csv)

        writer.writerow(header)
        writer.writerows(data)


# 메인 실행 함수
if len(sys.argv) < 2:
    extract_csv()
    print('--- Downloaded! ---')

elif len(sys.argv) == 2:
    file_path = sys.argv[1]
    renew_data()
    print("--- Renewed! ---")

else:
    print("Only single csv file is required.")
