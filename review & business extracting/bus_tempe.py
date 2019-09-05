import json
from collections import OrderedDict

file_data = OrderedDict()

def data_to_json(data) :
    if type(data) is str : # 타입이 문자열이라면
        return '"' + data + '"' # 문자열을 "로 묶어주고
    elif type(data) is list : # 타입이 리스트라면
        return list_to_json(data, data_to_json) # 함수 호출
    elif type(data) is int or type(data) is float : # 타입이 숫자라면
        return data.__str__() # 그대로 반환
    elif type(data) is dict : # 타입이 dict라면
        return dict_to_json(data, data_to_json) # 함수 호출
    else :
        print("type은 {}".format(type(data)))
        return '""'
    
def list_to_json(list, func):
    out_str = "[" # [(대괄호)를 연다
    for val in list:
        out_str += func(val)
        out_str += ", " # ,(쉼표)로 데이터를 구분

    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "]" # ](대괄호)를 닫는다
    return out_str

def dict_to_json(dict, func) :
    out_str = "{" # {(중괄호)를 연다
    for key in dict.keys() :
        out_str += ('"' + key.__str__() + '"') # 키 값에 "(큰 따옴표)를 씌운다
        out_str += ": " # :(콜론)으로 Key와 Value를 분리
        out_str += func(dict[key])
        out_str += ", " # ,(쉼표)로 쌍과 쌍을 분리
    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "}" # }(중괄호)를 닫는다
    return out_str

# retaurant list - 각자 쓰기
res_list = ['Four Peaks Brewing', 'Cornish Pasty',
       'Culinary Dropout', 'Green New American Vegetarian', 'House of Tricks',
       'Snooze, An A.M. Eatery', 'Haji-Baba', 'Casey Moore\'s Oyster House',
       'Lucille\'s Smokehouse Bar-B-Que','La Bocca Urban Pizzeria + Wine Bar']

# 파일에 추가해서 쓰는거니까 새로 돌릴 때 기존 파일 삭제해야함
with open('C:\\Users\\CSE_125-2\\Desktop\\yelp_data\\bus_tempe.json', 'a', -1, encoding='UTF-8') as mf:
    with open('C:\\Users\\CSE_125-2\\Desktop\\yelp_data\\business.json', 'rt', encoding='UTF-8') as f:
        for line in f:
            lineobj = json.loads(line)
            if lineobj["postal_code"]== '85281':
                for name in res_list:
                    if lineobj['name'] == name:
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

