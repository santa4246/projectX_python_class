import numpy as np

def main():
    try:
        arr1 = get_csv('mars_base_main_parts/mars_base_main_parts-001.csv')
        arr2 = get_csv('mars_base_main_parts/mars_base_main_parts-002.csv')
        arr3 = get_csv('mars_base_main_parts/mars_base_main_parts-003.csv')
        parts = merge_csv(arr1, arr2, arr3)
        
        valid_values = get_parts_average(parts)
        save_csv_under_fifty(valid_values)
        
    except Exception as err :
        print("error: {0}".format(err))

def get_csv(file_path):
    return np.genfromtxt(file_path, delimiter=',', skip_header=1)

def merge_csv(arr1, arr2, arr3):
    return np.concatenate((arr1, arr2, arr3), axis=0)

def get_parts_average(parts):
    valid_values = parts[~np.isnan(parts)]
    print(np.mean(valid_values)) # 평균값

    return valid_values

def save_csv_under_fifty(valid_values):
    filtered_values = valid_values[valid_values < 50]
    np.savetxt('parts_to_work_on.csv', filtered_values, delimiter=',', fmt='%.2f')

if __name__ == "__main__":
    main()