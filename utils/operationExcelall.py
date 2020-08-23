#!/usr/bin/pathon3
#-*- coding:UTF-8 -*-
# @author: cc <wangmei@lanysec.com>
import xlrd
#from utils.operationYaml import OperationYaml
import json
from common.public import *
class ExcelVarles(object):
    """excel中的列号是固定的，所以定义一个类获取列的索引和列名称对应"""
    caseId = 'caseID'
    descript = '描述'
    url = '请求地址'
    precondition = '前置条件'
    paramstype = '请求参数类型'
    method = '请求方法'
    data = '请求参数'
    expect = '期望结果'
    isrun = '是否运行'
    headers = '请求头'
    statuscode = '状态码'

class OperationExcel:
    def get_sheet(self):
        wk=xlrd.open_workbook(file_path('data','books.xlsx'))
        return wk.sheet_by_index(0)
    @property
    def get_excel_datas(self):
        """实现获取excel文件中的所有内容，以列表的形式返回，列表中包含多个字典，
        每个字典为一行数据，键为表头，值为对应的该行的值"""
        datas=list()
        title=self.get_sheet().row_values(0)
        for row in range(1,self.get_sheet().nrows):
            row_values=self.get_sheet().row_values(row)
            datas.append(dict(zip(title,row_values)))
        return datas
    def runs(self):
        """获取到可执行的测试用例"""
        run_list=[]
        for item in self.get_excel_datas:
            isrun=item[ExcelVarles.isrun]
            if isrun == 'y':
                run_list.append(item)
            else:
                pass
        return run_list
    def case_list(self):
        """获取所有的测试用例"""
        allcase=[]
        for item in self.get_excel_datas:
            allcase.append(item)
        return allcase
    def case_prev(self,caseprev):
        """
        根据前置测试条件找到关联的测试用例
        :param caseprev:前置测试条件
        :return:
        """
        for item in self.case_list():
            if caseprev in item.values():
                return item
    def prev_hearder(self,prev_result):
        """
        将传入的参数值与hearder部分的{token}进行替换实现关联
        :param prev_result: 替换{token}的参数
        :return:
        """
        for item in self.runs():
            header=(item[ExcelVarles.headers])
            if '{token}' in header:
                header=str(header).replace('{token}',prev_result)
                return json.loads(header,encoding='utf-8')

if __name__=='__main__':
    obj=OperationExcel()
    print(obj.case_list())