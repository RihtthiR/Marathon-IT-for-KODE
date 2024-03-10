import json
import time
from call_function_with_timeout import SetTimeout

def read_json_func():
    with open("List_of_data.json") as json_file:
        json_data = json.load(json_file)
        # print(json_data)
        sum = 0
        for i in range(len(json_data)):
            time.sleep(2)
            try:
                sum += json_data[i]['temperatureC']
                print(json_data[i]['temperatureC'])
            except TypeError:
                print('Error in variable')
        print('Average:',sum / len(json_data))

def read_with_timeout():
    read_json_with_timeout = SetTimeout(read_json_func,timeout=10)

    is_done, is_timeout, err_msg, results = read_json_with_timeout()
    print('Done:',is_done,'Timeout:',is_timeout,'Error:',err_msg,'Results:',results)

