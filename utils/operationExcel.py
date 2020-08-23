#！/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:wangmei
import xlrd
from utils.operationYaml import OperationYaml
from common.public import *
class ExcelVarles(object):
    """excel中的列号是固定的，所以定义一个类获取列的索引和列名称对应"""
    caseId = 0
    descript = 1
    url = 2
    method = 3
    data = 4
    expect = 5
    def getcaseId(self):
        return self.caseId
    def getdescript(self):
        return self.descript
    def geturl(self):
        return self.url
    def getmethod(self):
        return self.method
    def getdata(self):
        return self.data
    def getexpect(self):
        return self.expect
class OperationExcel:
    def get_sheet(self):
        wk=xlrd.open_workbook(file_path('data','books.xlsx'))
        return wk.sheet_by_index(0)
    @property
    def get_rows(self):
        """获取总行数"""
        return self.get_sheet().nrows
    @property
    def get_cols(self):
        """获取总列数"""
        return self.get_sheet().ncols
    def get_value(self,row,col):
        return self.get_sheet().cell_value(row,col)
    def get_caseID(self,row):
        return self.get_value(row=row,col=ExcelVarles().getcaseId())
    def get_url(self,row):
        url=self.get_value(row=row, col=ExcelVarles().geturl())
        if '{bookID}' in url:
            return str(url).replace('{bookID}',read_content(filedir='data',filename='bookId'))
        else:
            return url
    def get_method(self,row):
        return self.get_value(row=row, col=ExcelVarles().getmethod())
    def get_data(self,row):
        caseId=self.get_value(row=row, col=ExcelVarles().getdata())
        return OperationYaml.dict_yaml(caseId)
    def get_expect(self,row):
        return self.get_value(row=row, col=ExcelVarles().getexpect())
    def get_excel_datas(self):
        """实现获取excel文件中的所有内容，以列表的形式返回，列表中包含多个字典，
        每个字典为一行数据，键为表头，值为对应的该行的值"""
        datas=list()
        title=self.get_sheet().row_values(0)
        for row in range(1,self.get_sheet().nrows):
            row_values=self.get_sheet().row_values(row)
            datas.append(dict(zip(title,row_values)))
        return datas
# if __name__ == "__main__":
#     obj=OperationExcel()
#     print(obj.get_data(row=2))
#     print(type(obj.get_data(row=2)))
