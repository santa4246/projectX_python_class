import csv

def main():
    file_name = 'Mars_Base_Inventory_List.csv'

    # 수행과제
    read_csv(file_name)
    
    # 보너스과제


def read_csv(file_name):
    columns = {}

    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        
        for header in headers:
            columns[header] = []

        for row in csv_reader:
            for header, value in zip(headers, row):
                columns[header].append(value)

    for header, values in columns.items():
        # print(f'{header}: {values}')
        pass
    
    print(sorted(list(map(float, columns['Flammability'])), reverse = True))

if __name__ == "__main__":
    main()