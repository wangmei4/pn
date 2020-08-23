#!/usr/bin/pathon3
#-*- coding:UTF-8 -*-
# @author: cc <wangmei@lanysec.com>
import pytest
datalist=[
    {'caseID': 'login', '描述': '登录', '请求地址': 'http://127.0.0.1:5000/v1/auth', '前置条件': '', '请求方法': 'post', '请求参数类型': '', '请求参数': '', '期望结果': '', '是否运行': 'y', '请求头': '', '状态码': ''},
    {'caseID': 'book_001', '描述': '获取书籍信息', '请求地址': 'http://127.0.0.1:5000/v1/api/books', '前置条件': 'login', '请求方法': 'get', '请求参数类型': '', '请求参数': '', '期望结果': 'python自动化测试实战', '是否运行': 'y', '请求头': '', '状态码': 200},
    {'caseID': 'book_002', '描述': '添加书籍', '请求地址': 'http://127.0.0.1:5000/v1/api/books', '前置条件': 'login', '请求方法': 'post', '请求参数类型': '', '请求参数': 'book_002', '期望结果': '添加成功', '是否运行': 'y', '请求头': '{"Authorization":"JWT {token}"}', '状态码': 200},
    {'caseID': 'book_003', '描述': '查看书籍', '请求地址': 'http://127.0.0.1:5000/v1/api/books/{bookID}', '前置条件': 'login', '请求方法': 'get', '请求参数类型': '', '请求参数': '', '期望结果': '', '是否运行': 'y', '请求头': '{"Authorization":"JWT {token}"}', '状态码': 200},
    {'caseID': 'book_004', '描述': '编辑书籍信息', '请求地址': 'http://127.0.0.1:5000/v1/api/books/{bookID}', '前置条件': 'login', '请求方法': 'put', '请求参数类型': '', '请求参数': '', '期望结果': '', '是否运行': 'y', '请求头': '{"Authorization":"JWT {token}"}', '状态码': 200},
    {'caseID': 'book_005', '描述': '删除书籍信息', '请求地址': 'http://127.0.0.1:5000/v1/api/books/{bookID}', '前置条件': 'login', '请求方法': 'delete', '请求参数类型': '', '请求参数': 'book_005', '期望结果': '删除书籍成功', '是否运行': 'y', '请求头': '{"Authorization":"JWT {token}"}', '状态码': 200}
]

@pytest.mark.parametrize('data',datalist)
def test_01(data):
    print(data)
    assert 1==1
if __name__=='__main__':
    pytest.main(['-s','-v','test_001.py'])

