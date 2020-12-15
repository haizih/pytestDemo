# -*- coding: UTF-8 -*-
# Author: duke
# Date: 2020/12/8

import pytest
class TestData:
    @pytest.mark.parametrize(['a','b'], [(10, 20), (110, 5), (31, 9)])
    def test_data(self, a, b):
        print(a + b)