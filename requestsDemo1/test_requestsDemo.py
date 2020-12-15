import requests
from jsonpath import jsonpath
from hamcrest import *


class TestDemo:
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "duke"
        }
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "duke"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "duke"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_hogwarts_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        # print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "header demo"})
        print(r.status_code)
        # print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "header demo"

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        # print(r.json()['category_list']['categories'][0]['name'])
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('霍格沃兹测试学院公众号'))

    # header cookie处理
    def test_header_demo(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {'User-Agent': 'test-User-Agent'}
        cookie_data = {
            'hogwarts': 'school',
            'teacher': 'AD'
        }
        r = requests.get(url=url, headers=header, cookies = cookie_data)
        print(r.request.headers)
