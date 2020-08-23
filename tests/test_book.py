#！/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:wangmei
import pytest
from base.method import Requests
from utils.operationExcel import OperationExcel
from common.public import *
import json
class TestBook():
    excel=OperationExcel()
    obj=Requests()
    def result(self,r,row):
        """对响应码和响应内容的断言"""
        assert r.status_code == 200
        assert self.excel.get_expect(row=row) in json.dumps(r.json(),ensure_ascii=False)
    def test_book_001(self):
        """获取所有的书籍信息"""
        r=self.obj.get(url=self.excel.get_url(row=1))
        self.result(r=r,row=1)
    def test_book_002(self):
        """
        验证添加书籍，两点：
        1、需要校验用例是否执行成功，验证书籍添加成功
        2、从响应结果中获取bookid,并将bookid写入到一个文件中，这个写入到文件的方法在common
        下的public.py里面封装
        """
        r=self.obj.post(
            url=self.excel.get_url(row=2),
            json=self.excel.get_data())
        write_content(content=r.json()[0]['datas']['id'],filedir='data',filename='bookId')
        self.result(r=r,row=2)
    def test_book_003(self):
        """
        查看添加的书籍，URL中包含动态参数bookid，
        所以需要从文件中读取bookid的值，并修改获取url的函数（operationExcel.py中get_url（））
        同理在public下面添加读取的方法
        """
        r=self.obj.get(url=self.excel.get_url(row=3))
        self.result(r=r,row=2)
if __name__=='__main__':
    """下面的执行中::表示层级关系，如下表示只执行test_book_001用例"""
    pytest.main(['-v','test_book.py::TestBook::test_book_001'])