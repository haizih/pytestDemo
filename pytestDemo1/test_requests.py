# -*- coding: UTF-8 -*-
# Author: duke
# Date: 2020/12/2

import requests

# r = requests.post('http://httpbin.org/post', data={'key': 'value'})
# r = requests.post('http://httpbin.org/post',data={'key':'value'})
#
# print(r.status_code)

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url)

# payload = {'key1':'value1','key2':['value2','value3']}
# r = requests.get('http://httpbin.org/get',params=payload)
# print(r.url)
# print(r.text)

# r = requests.get('http://www.baidu.com')
# print(r.encoding)
# r.encoding = 'utf-8'
# print(r.encoding)
# print(r.text)

# r = requests.get('https://api.github.com/events')
# print(r.json())

# r = requests.get('https://api.github.com/events')
# print(r.raw)
# print(r.raw.read(5))
url = 'http://httpbin.org/get'
# headers = {'user-agent': 'my-app/0.0.111'}
#
# r = requests.get(url, headers=headers)
#
# print(r.text)

# r = requests.get(url)
# print(r.cookies)
# print(r.text)


# payload = {'key1':'value1', 'key2':'value2'}
# r = requests.post('http://httpbin.org/post',data=payload)
#
# print(r.text)
#
# payload = (('key1', 'value1'), ('key1', 'value2'))
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)

# response1 = requests.get("http://httpbin.org/get?key1=value1")
# print(response1.url)

# parameter = {
#             "key1":"value1",
#             "key2":"value2"
#             }
# response2 = requests.get("http://httpbin.org/get",params = parameter)
# print(response2.url)
# http://httpbin.org/get?key1=value1&key2=value2


import requests

new_headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
}

response = requests.get("https://www.zhihu.com",headers = new_headers)
print(response.text)        #正常输出

