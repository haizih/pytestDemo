# -*- coding: UTF-8 -*-
# Filename:test_order.py
# Author: duke
# Date: 2020-12-09 11:55

import pytest
class TestPytest():

    @pytest.mark.run(order=-1)
    def test_two(self):
        print('test_two is -1')

    @pytest.mark.run(order=-7)
    def test_one(self):
        print('test_one is -7')

    @pytest.mark.run(order=-66)
    def test_three(self):
        print('test_three is -6')

