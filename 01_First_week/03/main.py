import csv

def main():
    file_name = 'Mars_Base_Inventory_List.csv'
    try:
        read_csv(file_name)

    except Exception as err :
        print("error: {0}".format(err))

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
        print(f'{header}: {values}')

    sorted_indices = sorted(range(len(columns['Flammability'])), key=lambda k: columns['Flammability'][k], reverse = True)
    
    sorted_Substance = [columns['Substance'][i] for i in sorted_indices]
    sorted_Weight = [columns['Weight (g/cm쨀)'][i] for i in sorted_indices]
    sorted_Specific = [columns['Specific Gravity'][i] for i in sorted_indices]
    sorted_Strength = [columns['Strength'][i] for i in sorted_indices]
    sorted_Flammability = [columns['Flammability'][i] for i in sorted_indices]

    print(sorted_Substance)
    print(sorted_Weight)
    print(sorted_Specific)
    print(sorted_Strength)
    print(sorted_Flammability)

def print_specific_value(float_list):
    for index, value in enumerate(float_list):
        if value >= 0.7:
            print(f"인덱스: {index}, 값: {value}")

if __name__ == "__main__":
    main()