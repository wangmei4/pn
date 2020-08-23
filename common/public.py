#！/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:wangmei
import os
def file_path(filedir,filename):
    """
    获取文件路径
    :param filedir: 文件所在的文件夹名称
    :param filename: 文件名称
    :return: 文件的绝对路径
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),filedir,filename)
def write_content(content,filedir,filename):
    with open(file_path(filedir=filedir,filename=filename),'w') as f:
        f.write(str(content))
def read_content(filedir,filename):
    with open(file_path(filedir=filedir,filename=filename),'r') as f:
        return f.read()
