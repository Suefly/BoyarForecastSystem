from baiyu.models import *

with open('D:\项目文件\家禽计量系统\database\WeekInputTable.txt', mode='r', encoding='utf-8') as f:
    res = f.readlines()
    print(res)
    ret_list = []
    for line in res:
        ret = line.replace('\n','').replace('00:00:00.000','').split(' ')
        while '' in ret:
            ret.remove('')
        print(ret)
        ret_list.append(ret)


print(ret_list[1:])

def insert_input_data(ret_list):
    items_list = []
    for index in ret_list:
        item = IntroducedInfo(
            Year = index[1],
            WeekNum = index[2],
            startDate = index[3],
            endDate = index[4],
            RuSheNum = index[5],
            LivePeriod = index[6],
            nGeneration = index[8],
            nDraftOrOriginal = index[9],
            nBirdsType = index[10],
            flag = 0,
            Remark = ''
        )
        items_list.append(item)
    IntroducedInfo.objects.bulk_create(items_list)

insert_input_data(ret_list[1:])