# -*- coding: UTF-8 -*-
# Author: duke
# Date: 2020/12/4

import yaml
#
# print(yaml.load("""
# - Hesperiidae
# - Papilionidae
# - Apatelodidae
# - Epiplemidae
# """, Loader=yaml.FullLoader))
#
# print(yaml.load("""a:1
# """, Loader=yaml.FullLoader))

print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))

# print(yaml.load(open('demo.yml'), loader=yaml.FullLoader))
print(yaml.dump({'a': [1, 2]}))

with open("demo3.yml","w") as f:
    yaml.dump(data={'a':[1,2]}, stream=f)