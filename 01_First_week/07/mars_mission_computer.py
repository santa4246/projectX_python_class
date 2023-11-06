import random, time

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


def main():
    try:
        RunComputer = MissionComputer()
        RunComputer.get_sensor_data()
    except Exception as err :
        print("error: {0}".format(err))


if __name__ == "__main__":
    main()