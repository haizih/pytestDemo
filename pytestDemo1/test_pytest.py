import pytest
def test_one():
    print("开始执行 test_one 方法")
    x = 'this'
    assert 'h' in x


def test_two():
    print("开始执行 test_two 方法")
    x = 'hello'
    assert 'e' in x


def test_three():
    print("开始执行 test_three 方法")
    a = 'hello'
    b = 'hello world'
    assert a not in b



if __name__ == '__main__':
    pytest.main()
