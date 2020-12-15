# -*- coding: UTF-8 -*-
# Filename:test_demo.py
# Author: duke
# Date: 202012-09 00:13
import pytest
import yaml
class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if 'test' in env:
            print('this is test env')
            print(r"test env's is :",env['test'])
        elif 'dev' in env:
            print('This is dev env')


