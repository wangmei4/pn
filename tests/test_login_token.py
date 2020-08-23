#!/usr/bin/pathon3
#-*- coding:UTF-8 -*-
# @author: cc <wangmei@lanysec.com>
from base.method import Requests
from utils.operationExcelall import *
import pytest
import json
excel=OperationExcel()
obj1=Requests()

@pytest.mark.parametrize('datas',excel.runs())
def test_login_book(datas):
    """对请求参数做反序列化处理,因为这里直接返回的请求参数是字符串类型的，在requests中需要传递字典格式"""
    data=datas[ExcelVarles.data]
    if len(str(data).strip()) == 0:pass
    elif len(str(data).strip()) >0:
        data = json.loads(data,encoding='utf-8')
    #同理，对请求头做反序列化的处理
    hearders=datas[ExcelVarles.headers]
    if len(str(hearders).strip()) == 0:
        pass
    elif len(str(hearders).strip()) >= 0:
        hearders = json.loads(hearders,encoding='utf-8')
    #执行前置条件关联的测试用例
    r = obj1.post(
        url=excel.case_prev(datas[ExcelVarles.precondition])[ExcelVarles.url],
        json=json.loads(excel.case_prev(datas[ExcelVarles.precondition])[ExcelVarles.params],encoding='utf-8')
    )
    #获取响应中的token
    prev_result=r.json()['acces_token']
    #替换被关联的测试点的请求头中的信息的变量
    header=excel.prev_hearder(prev_result)
    status_code=int(datas[ExcelVarles.statuscode])
    def case_assert(r):
        assert r.status_code==status_code
        assert datas[ExcelVarles.expect] in json.dumps(r.json(), ensure_ascii=False)
    if datas[ExcelVarles.method] =='get':
        r=obj.get(url=datas[ExcelVarles.url])
        case_assert(r=r)
    elif datas[ExcelVarles.method] == 'post':
        r = obj(url=datas[ExcelVarles.url],
                json=data,
                hearders=header
                )
        #将bookId写入到一个文件中
        write_content(content=str(r.json()[0]['datas']['id']),filedir='config',filename='book.yaml')
        case_assert(r=r)
    elif datas[ExcelVarles.method] == 'delete':
        url=str(datas[ExcelVarles.url]).replace('{bookID}',read_content(filedir='config',filename='book.yaml'))
        r=obj.delete(url=url)
        case_assert(r=r)


if __name__=='__main__':
    pytest.main(["-s","-v","test_login_token.py","--alluredir","./report/result"])
    import subprocess
    #生成报告
    subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)
    #使用默认浏览器打开报告
    subprocess.call('allure open -h 127.0.0.1 -p 8088 ./report/html', shell=True)
