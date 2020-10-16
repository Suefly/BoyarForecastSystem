from baiyu.models import *

with open('D:\项目文件\家禽计量系统\database\WholeParameter.txt', mode='r', encoding='utf-8') as f:
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

def insert_whole_param_data(ret_list):
    items_list = []
    for index in ret_list:
        item = WholeParameter(
            YuChengPeriod = index[1],
            MaxLivePeriod = index[2],
            XuanYongRate = index[3],
            nGeneration = index[5],
            nBirdsType = index[6],
            Remark = ''
        )
        items_list.append(item)
    WholeParameter.objects.bulk_create(items_list)

insert_whole_param_data(ret_list[1:])