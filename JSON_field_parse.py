#coding:utf-8
import os
import json

"""
func:该函数主要用于打印json文件中指定名称的指定字段
Args:file:文件名 name:名称 filed:字段名

"""
def json_parse(file,name,filed):
    if not os.path.exists(file):
        print("json file not exist!")
    with open (file,'r') as f:
        json_data = json.loads(f.read())
    box_list = json_data["boxes"]
    for box in box_list:
        if box["name"] == name:
            print(box[filed])
            return box[filed]


if __name__ == "__main__":
    json_file="./boxes.json"
    json_parse(json_file,"box_b","rectangle")