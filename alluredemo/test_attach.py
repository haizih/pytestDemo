# -*- coding: UTF-8 -*-
# Filename:test_attach.py
# Author: duke
# Date: 2020-12-09 18:45
import pytest
import allure
def test_attach_txt():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段htmlbody块</body>","",attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("/Users/duke/PycharmProjects/pytestDemo/alluredemo/website-top-join.jpg",
                       name="这是一个图片",attachment_type=allure.attachment_type.JPG)