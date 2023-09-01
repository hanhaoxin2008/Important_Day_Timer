"""
json模块
"""

import json
def read_json():
    """
    读取json文件
    """
    with open("data.json", "r") as f:
        json_data=json.load(f)
    return json_data
def read_countdown():
    """
    读取json文件中的countdown
    """
    return  read_json()['list']
def write_json(json_data):
    """
    写入json文件
    """
    json_str = json.dumps(json_data)
    with open("data.json", "w") as f:
        f.write(json_str)


def write_countdown(countdown):
    """
    向json写入countdown
    """
    json_data=read_json()
    json_data['list'].append(countdown.__dict__)
    write_json(json_data)