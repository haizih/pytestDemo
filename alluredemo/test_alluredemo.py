# -*- coding: UTF-8 -*-
# Filename:test_alluredemo.py
# Author: duke
# Date: 202012-09 00:48

import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False

def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')
