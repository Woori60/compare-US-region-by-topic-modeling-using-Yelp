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

res = []
with open('C:\\Users\\CSE_125-2\\Desktop\\yelp_data\\bus_lasvegas.json', 'rt', encoding='UTF-8') as fp:
    for line in fp:
        lineobj = json.loads(line)
        res.append(lineobj['business_id'])

print(res)

# 파일에 추가해서 쓰는거니까 새로 돌릴 때 기존 파일 삭제해야함
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0



with open('C:\\Users\\CSE_125-2\\Desktop\\yelp_data\\review_lasvegas.json', 'a', -1, encoding='UTF-8') as mf:
    with open('C:\\Users\\CSE_125-2\\Desktop\\yelp_data\\review.json', 'rt', encoding='UTF-8') as f:
        for line in f:
            lineobj = json.loads(line)
            if lineobj['business_id'] == res[0]:
                if count1 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']

                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count1 = count1 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[1]:
                if count2 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']

                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count2 = count2 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[2]:
                if count3 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']

                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count3 = count3 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[3]:
                if count4 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']

                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count4 = count4 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[4]:
                if count5 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']
                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count5 = count5 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[5]:
                if count6 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']
                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count6 = count6 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[6]:
                if count7 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']

                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count7 = count7 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[7]:
                if count8 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']

                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count8 = count8 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[8]:
                if count9 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']

                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count9 = count9 + 1
                else:
                    continue
            elif lineobj['business_id'] == res[9]:
                if count10 < 200:
                    file_data['review_id'] = lineobj['review_id']
                    file_data['user_id'] = lineobj['user_id']
                    file_data['business_id'] = lineobj['business_id']
                    file_data['stars'] = lineobj['stars']
                    file_data['date'] = lineobj['date']
                    file_data['text'] = lineobj['text']

                    mf.write(dict_to_json(file_data, data_to_json))#, encoding='utf-8')
                    mf.write('\n')
                    count10 = count10 + 1
                else:
                    continue
            else:
                continue
                        
            
        '''
        for line in f:
            lineobj = json.loads(line)
            if lineobj["postal_code"]== '85226':
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

'''
