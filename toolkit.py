import datetime
import time

import xlrd as xlrd
from chinese_calendar import is_workday


def replace_all(filter_: list, string: str) -> str:
    """
    过滤所有字符
    :param filter_:要过滤的字符列表
    :param string:
    :return:
    """
    for filter_word in filter_:
        string = string.replace(filter_word, '')
    return string


class Timer(object):
    """
    计时器，对于需要计时的代码进行with操作：
    with Timer() as timer:
        ...
        ...
    print(timer.cost)
    ...
    """

    def __init__(self, start=None):
        self.start = start if start is not None else time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        self.cost = self.stop - self.start
        return exc_type is None


def change_to_sec(_time):
    """
    时分秒转换为秒数
    :param _time:
    :return:
    """
    hour, min_, seconds = _time.strip().split(":")
    return int(hour) * 3600 + int(min_) * 60 + int(seconds)


def check_is_workday(date):
    """
    判断是否为工作日
    """
    y = date.year
    m = date.month
    d = date.day
    april_last = datetime.date(y, m, d)
    return is_workday(april_last)


def get_excel_data(path, sheet_name):
    """
    获取excel文档数据
    :param path:
    :param sheet_name:
    :return: data_list
    """
    bk = xlrd.open_workbook(path)
    sh = bk.sheet_by_name(sheet_name)
    row_num = sh.nrows
    data_list = []
    for i in range(1, row_num):
        row_data = sh.row_values(i)
        data = {}
        for index, key in enumerate(sh.row_values(0)):
            data[key] = row_data[index]
        data_list.append(data)
    return data_list
