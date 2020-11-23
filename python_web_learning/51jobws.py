def get_city_code():
    from selenium import webdriver
    import requests
    r = webdriver.Chrome()
  

    url = 'https://js.51jobcdn.com/in/js/h5/dd/d_jobarea.js?20191212'
    r = requests.get(url)
    begin = r.text.find('var hotcity')
    if begin == -1:
        print('Not find var hotcity')
    # print(begin)
    end = r.text.find(';',begin)
    if end == -1:
        print('Not find ; ')
    # print(end)
    result_text = r.text[begin : end-1]
    #print(result_text)
    begin = result_text.find('{')
    city_dict_str = result_text[begin:]
    # print(city_dict_str)
    key,value = "",""
    key_list,value_list = [],[]
    count = 1
    i = 0
    while i < len(city_dict_str):
        if city_dict_str[i] == '"' and count == 1:
            count = 2
            i += 1
            while city_dict_str[i] != '"':
                key += city_dict_str[i]
                i += 1
            key_list.append(key)
            key = ""
            i += 1
        if city_dict_str[i] == '"' and count == 2:
            count = 1
            i += 1
            while city_dict_str[i] != '"':
                value += city_dict_str[i]
                i += 1
            value_list.append(value)
            value = ""
            i += 1
        i += 1
    city_dict = {}
    i = 0
    while i < len(key_list):
        city_dict[value_list[i]] = key_list[i]
        i += 1
    # print(city_dict)
    return city_dict

print(get_city_code())