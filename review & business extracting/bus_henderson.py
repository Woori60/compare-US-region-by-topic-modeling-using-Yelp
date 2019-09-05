import json
from collections import OrderedDict

file_data = OrderedDict()

def data_to_json(data) :
    if type(data) is str : # Ÿ���� ���ڿ��̶��
        return '"' + data + '"' # ���ڿ��� "�� �����ְ�
    elif type(data) is list : # Ÿ���� ����Ʈ���
        return list_to_json(data, data_to_json) # �Լ� ȣ��
    elif type(data) is int or type(data) is float : # Ÿ���� ���ڶ��
        return data.__str__() # �״�� ��ȯ
    elif type(data) is dict : # Ÿ���� dict���
        return dict_to_json(data, data_to_json) # �Լ� ȣ��
    else :
        print("type�� {}".format(type(data)))
        return '""'
    
def list_to_json(list, func):
    out_str = "[" # [(���ȣ)�� ����
    for val in list:
        out_str += func(val)
        out_str += ", " # ,(��ǥ)�� �����͸� ����

    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "]" # ](���ȣ)�� �ݴ´�
    return out_str

def dict_to_json(dict, func) :
    out_str = "{" # {(�߰�ȣ)�� ����
    for key in dict.keys() :
        out_str += ('"' + key.__str__() + '"') # Ű ���� "(ū ����ǥ)�� �����
        out_str += ": " # :(�ݷ�)���� Key�� Value�� �и�
        out_str += func(dict[key])
        out_str += ", " # ,(��ǥ)�� �ְ� ���� �и�
    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "}" # }(�߰�ȣ)�� �ݴ´�
    return out_str

# retaurant list - ���� ����
res_list = ['The Cracked Egg', 'Sammy\'s Restaurant & Bar', 'Sushi Cafe', 'Metro Diner', 'Claim Jumper Restaurant & Saloon', 'The Steamie Weenie', 'Ohjah Japanese Steakhouse', 'Henry\'s American Grill', 'China Tango', 'Sushi Bay']

# ���Ͽ� �߰��ؼ� ���°Ŵϱ� ���� ���� �� ���� ���� �����ؾ���

with open('bus_henderson.json', 'a', -1, encoding='UTF-8') as mf:
    with open('business.json', 'rt', encoding='UTF-8') as f:
        for line in f:
            lineobj = json.loads(line)
            
            if lineobj["postal_code"]== '89074':
              
              for name in res_list:
                if lineobj["name"]==name:
                  file_data["business_id"] = lineobj["business_id"]
                  file_data["name"] = lineobj["name"]
                  file_data["city"] = lineobj["city"]
                  file_data["state"] = lineobj["state"]
                  file_data["postal_code"] = lineobj["postal_code"]
                  file_data["stars"] = lineobj["stars"]
                  file_data["review_count"] = lineobj["review_count"]
                  file_data["categories"] = lineobj["categories"]
               
                  print(file_data)
                  mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                  mf.write('\n')