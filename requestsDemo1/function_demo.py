# -*- coding: UTF-8 -*-
# Author: duke
# Date: 2020/12/5

# def method(*,a):
#     print(a)
#
# method(a=1)

print(list(range(3,6)))  # [3, 4, 5]
list_a = (3,6)
print(list_a)  # (3, 6)
print(list(range(*list_a))) # [3, 4, 5]

