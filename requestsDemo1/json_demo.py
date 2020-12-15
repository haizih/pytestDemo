# -*- coding: UTF-8 -*-
# Author: duke
# Date: 2020/12/6
# import json
#
# info = [{
#     "name": "Tom",
#     "gender": "male",
#     "other": None
# }, {
#     "name": "Jack",
#     "gender": "male",
#     "other": None
# }]
# # dumps:将python中的 字典 转换为 字符串
# data = json.dumps(info, sort_keys=True, indent=4)
# print(data)
# print(type(data))

import json
# loads:将字符串转换为 json
str = '''
[{
    "name": "Tom",
    "gender": "male"
}, {
    "name": "Jack",
    "gender": "male"
}]
'''

print(type(str))
data = json.loads(str)
print(type(data))
print(data)


