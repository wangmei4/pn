#！/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:wangmei
import yaml
from common.public import file_path

class OperationYaml:
    def read_yaml(self,filedir,filename):
        """读取标准格式的yaml文件，如data下面的login.yaml"""
        with open(file_path(filedir,filename),'r',encoding='utf-8') as f:
            return list(yaml.safe_load_all(f))
    def dict_yaml(self,fileDir='config',fileName='book.yaml'):
        """读取字典格式的yaml文件，读取内容与excel中的data映射起来"""
        with open(file_path(filedir=fileDir,filename=fileName), 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
if __name__=='__main__':
    obj=OperationYaml()
    print(obj.dict_yaml()['book_002'])
