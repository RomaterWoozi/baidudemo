# -*- coding: utf-8 -*-

"""
字符串格式化
"""


def test_fun():
    base_url = 'http://image.so.com/zj?ch=art&sn=%d&listtype=new&temp=1'
    start_index = 631
    offset=0;
    print(str(offset))
    print((base_url % start_index))

    url = 'http://top.baidu.com/buzz?b=%d&fr=%d'
    b = 1
    fr = 20811
    print(url % (b, fr))


if __name__ == '__main__':
    test_fun()
