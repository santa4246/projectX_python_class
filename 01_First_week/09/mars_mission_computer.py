import random, time, platform, psutil, multiprocessing, threading

class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature' : '',
            'mars_base_external_temperature' : '',
            'mars_base_internal_humidity' : '',
            'mars_base_external_illuminance' : '',
            'mars_base_internal_co2' : '',
            'mars_base_internal_oxygen' : '',
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 2)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    def get_env(self):
        return self.env_values


class MissionComputer:
    def __init__(self):
        self.env_values = {}
        self.ds = DummySensor()
    
    def get_sensor_data(self):
        while True:
            self.ds.set_env()
            self.env_values = self.ds.get_env()
            
            env_json = '{\n'
            for key, value in self.env_values.items():
                env_json += f'    "{key}": '
                if isinstance(value, str):
                    env_json += f'"{value}",\n'
                else:
                    env_json += f'{value},\n'
            env_json = env_json.rstrip(',\n') + '\n}'
            print(env_json)
            time.sleep(5)

    def get_mission_computer_info(self):
        while True:
            try:
                cpu = platform.system(),
                cpu_version = platform.version(),
                cpu_type = platform.processor(),
                cpu_core_count = multiprocessing.cpu_count(),
                mem_size = round(psutil.virtual_memory().total / (1024.0 ** 3), 2),
            except Exception as e:
                print(f"error : {str(e)}")

            sys__info_dict ={
                'cpu': cpu,
                'cpu_version': cpu_version,
                'cpu_type': cpu_type,
                'cpu_core_count': cpu_core_count,
                'mem_size': mem_size,
            }

            sys_info_json = '{\n'
            for key, value in sys__info_dict.items():
                sys_info_json += f'    "{key}": '
                if isinstance(value, str):
                    sys_info_json += f'"{value}",\n'
                else:
                    sys_info_json += f'{value},\n'
            sys_info_json = sys_info_json.rstrip(',\n') + '\n}'
            print(sys_info_json)

            time.sleep(20)
    
    def get_mission_computer_load(self):
        while True:
            try:
                cpu_usage = psutil.cpu_percent(interval=1),
                mem_usage = psutil.virtual_memory().percent,
            except Exception as e:
                print(f"error : {str(e)}")
                
            usage_dict = {
                'cpu_usage' : cpu_usage,
                'mem_usage' : mem_usage,
            }

            usage_json = '{\n'
            for key, value in usage_dict.items():
                usage_json += f'    "{key}": '
                if isinstance(value, str):
                    usage_json += f'"{value}",\n'
                else:
                    usage_json += f'{value},\n'
            usage_json = usage_json.rstrip(',\n') + '\n}'
            print(usage_json)

            time.sleep(20)


def main():
    try:
        runComputer = MissionComputer()

        sensor_thread = threading.Thread(target=runComputer.get_sensor_data)
        info_thread = threading.Thread(target=runComputer.get_mission_computer_info)
        load_thread = threading.Thread(target=runComputer.get_mission_computer_load)

        sensor_thread.start()
        info_thread.start()
        load_thread.start()

        sensor_thread.join()
        info_thread.join()
        load_thread.join()

        runComputer1 = MissionComputer()
        runComputer2 = MissionComputer()
        runComputer3 = MissionComputer()

        process1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info)
        process2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load)
        process3 = multiprocessing.Process(target=runComputer3.get_sensor_data)

        process1.start()
        process2.start()
        process3.start()
        
    except Exception as err :
        print("error: {0}".format(err))
    

if __name__ == "__main__":
    main()