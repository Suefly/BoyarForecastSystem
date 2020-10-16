from baiyu.models import *

with open('D:\项目文件\家禽计量系统\database\WeekStandardTable.txt', mode='r', encoding='utf-8') as f:
    res = f.readlines()
    print(res)
    ret_list = []
    for line in res:
        ret = line.replace('\n','').split(' ')
        while '' in ret:
            ret.remove('')
        print(ret)
        ret_list.append(ret)


print(ret_list[1:])

def insert_weekly_param_data(ret_list):
    items_list = []
    for index in ret_list:
        item = WeekStandardTable(
            WeekNum = index[1],
            siTaoRate = index[2],
            ChanDanRate = index[3],
            RuFuZhongDanRate = index[4],
            ShouJingRate = index[5],
            FuHuaRate = index[6],
            JianChuRate = index[7],
            SaleRate = index[8],
            nGeneration = index[10],
            nBirdsType = index[11],
            Remark = ''
        )
        items_list.append(item)
    WeekStandardTable.objects.bulk_create(items_list)

insert_weekly_param_data(ret_list[1:])