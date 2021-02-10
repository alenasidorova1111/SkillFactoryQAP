import os
import json

with open(os.path.join(input(
        "Enter filename: \n")), encoding="utf8") as user_file:
    all_dicts = json.load(user_file)

# First attempt (the result returns Pass or wrong dictionary)
temp_list = [int, str,str,str,str,str,str, str, str,int, str, str, bool, bool, bool, str]
cnt = 0
for dict_ry in all_dicts:
    dict_val = [type(i) for i in list(dict_ry.values())]
    if dict_val == temp_list:
        print(str(cnt), 'Pass')
    else:
        print(dict_val)
    cnt += 1

# Second attempt (the result returns Pass or Error info for every dictionary
# (could be used for any .json file - after changing lists of types))
import os
import json

with open(os.path.join(input(
        "Enter filename: \n")), encoding="utf8") as user_file:
    all_dicts = json.load(user_file)

list_of_keys = ['timestamp', 'referer', 'location', 'remoteHost', 'partyId',
                'sessionId', 'pageViewId', 'eventType', 'item_id', 'item_price',
                'item_url', 'basket_price', 'detectedDuplicate',
                'detectedCorruption', 'firstInSession', 'userAgentName']
list_of_str = ['remoteHost', 'partyId', 'sessionId', 'pageViewId', 'item_id',
               'basket_price', 'userAgentName']
list_of_url = ['referer', 'location', 'item_url']
list_of_bool = ['detectedDuplicate', 'detectedCorruption', 'firstInSession']
list_of_event = ['eventType']
list_of_int = ['timestamp', 'item_price']

def check_value(dict_ry):
    temp_list = []
    if list(dict_ry) == list_of_keys:
        if list(dict_ry) == list_of_keys:
            for key, value in dict_ry.items():
                if key in list_of_int:
                    if type(value) == int:
                        temp_list.append('Pass')
                    else:
                        temp_list.append(f'{key} value has another type')
                if key in list_of_str:
                    if type(value) == str:
                        temp_list.append('Pass')
                    else:
                        temp_list.append(f'{key} value has another type')
                if key in list_of_bool:
                    if type(value) == bool:
                        temp_list.append('Pass')
                    else:
                        temp_list.append(f'{key} value has another type')
                if key in list_of_event:
                    if value == 'itemBuyEvent' or value == 'itemViewEvent':
                        temp_list.append('Pass')
                    else:
                        temp_list.append(f'{key} has wrong value')
                if key in list_of_url:
                    if value.startswith(r'http:') or value.startswith(r'https:'):
                        temp_list.append('Pass')
                    else:
                        temp_list.append(f'{key} value is not URL')
    return temp_list

cnt = 0
for i in all_dicts:
    if list(i) == list_of_keys:
        if check_value(i) == ['Pass'] * len(list_of_keys):
            print(f'In dictionary {cnt} - all values have status - Pass')
        else:
            print(f'In dictionary {cnt} - ', [i for i in check_value(i) if i != 'Pass'])
    else:
        print(f'In dictionary {cnt} - missed or extra values')
    cnt += 1


# Third attempt (the result returns Pass or Error info for every dictionary)
import os
import json

with open(os.path.join(input(
        "Enter filename: \n")), encoding="utf8") as user_file:
    all_dicts = json.load(user_file)

list_of_keys = ['timestamp', 'referer', 'location', 'remoteHost', 'partyId',
                'sessionId', 'pageViewId', 'eventType', 'item_id', 'item_price',
                'item_url', 'basket_price', 'detectedDuplicate',
                'detectedCorruption', 'firstInSession', 'userAgentName']


def check_value(dict_ry):
    temp_list = []
    if type(dict_ry['timestamp']) == int:
        temp_list.append('Pass')
    else:
        temp_list.append('timestamp value has another type')
    if type(dict_ry['referer']) == str:
        if dict_ry['referer'].startswith(r'http:') or dict_ry['referer'].startswith(r'https:'):
            temp_list.append('Pass')
        else:
            temp_list.append('referer value is not a URL')
    else:
        temp_list.append('referer value has another type')
    if type(dict_ry['location']) == str:
        if dict_ry['location'].startswith(r'http:') or dict_ry['location'].startswith(r'https:'):
            temp_list.append('Pass')
        else:
            temp_list.append('location value is not a URL')
    else:
        temp_list.append('location value has another type')
    if type(dict_ry['remoteHost']) == str:
        temp_list.append('Pass')
    else:
        temp_list.append('remoteHost value has another type')
    if type(dict_ry['partyId']) == str:
        temp_list.append('Pass')
    else:
        temp_list.append('partyId value has another type')
    if type(dict_ry['sessionId']) == str:
        temp_list.append('Pass')
    else:
        temp_list.append('sessionId value has another type')
    if type(dict_ry['pageViewId']) == str:
        temp_list.append('Pass')
    else:
        temp_list.append('pageViewId value has another type')
    if type(dict_ry['eventType']) == str:
        if dict_ry['eventType'] == 'itemBuyEvent' or dict_ry['eventType'] == 'itemViewEvent':
            temp_list.append('Pass')
        else:
            temp_list.append('eventType value is wrong')
    else:
        temp_list.append('eventType value has another type')
    if type(dict_ry['item_id']) == str:
        temp_list.append('Pass')
    else:
        temp_list.append('item_id value has another type')
    if type(dict_ry['item_price']) == int:
        temp_list.append('Pass')
    else:
        temp_list.append('item_price value has another type')
    if type(dict_ry['item_url']) == str:
        if dict_ry['item_url'].startswith(r'http:') or dict_ry['item_url'].startswith(r'https:'):
            temp_list.append('Pass')
        else:
            temp_list.append('item_url value is not a URL')
    else:
        temp_list.append('item_url value has another type')
    if type(dict_ry['basket_price']) == str:
        temp_list.append('Pass')
    else:
        temp_list.append('basket_price value has another type')
    if type(dict_ry['detectedDuplicate']) == bool:
        temp_list.append('Pass')
    else:
        temp_list.append('detectedDuplicate value has another type')
    if type(dict_ry['detectedCorruption']) == bool:
        temp_list.append('Pass')
    else:
        temp_list.append('detectedCorruption value has another type')
    if type(dict_ry['firstInSession']) == bool:
        temp_list.append('Pass')
    else:
        temp_list.append('firstInSession value has another type')
    if type(dict_ry['userAgentName']) == str:
        temp_list.append('Pass')
    else:
        temp_list.append('userAgentName value has another type')
    return temp_list


cnt = 0
for i in all_dicts:
    if list(i) == list_of_keys:
        if check_value(i) == ['Pass'] * len(list_of_keys):
            print(f'In dictionary {cnt} - all values have status - Pass')
        else:
            print(f'In dictionary {cnt} - ', [i for i in check_value(i) if i != 'Pass'])
    else:
        print(f'In dictionary {cnt} - missed or extra values')
    cnt += 1