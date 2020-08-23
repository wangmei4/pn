#！/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:wangmei
import pytest
import json
from base.method import Requests
from utils.operationYaml import OperationYaml
obj=Requests()
objyaml=OperationYaml()


@pytest.mark.parametrize('datas',objyaml.read_yaml('data','login.yaml'))

def test_login(datas):
    #发送请求
    r=obj.post(url=datas['url'],json=datas['data'])
    #断言：判断yaml文件中的except是否在响应中
    assert datas['except'] in json.dumps(r.json(),ensure_ascii='utf-8')

if __name__=='__main__':
    pytest.main(["-s","-v","test_login.py"])