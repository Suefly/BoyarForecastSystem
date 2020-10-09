from baiyu.db import *
from baiyu.common import *

'''
获取祖代引种的总数(不分公司，不分品种，不分饲养方式，只是按时间求入舍的总数)
'''

def insertDB_introduced_info(**kwargs):
    if not kwargs:
        print('no valid kwargs')
        return
    else:
        # print('database would be updated')
        init_param ={
            'Year':0,
            'WeekNum':0,
            'startDate':'0000-0-0',
            'endDate':'0000-0-0',
            'RuSheNum':0,
            'nGeneration':0,
            'nDraftOrOriginal':0,
            'nBirdsType':0,
            'Remark':''
        }
        for key in kwargs:
            if key in init_param.keys():
                init_param[key] = kwargs[key]
            else:
                print('Keep the origin key and value!')

        IntroducedInfo.objects.create(
            Year=init_param['Year'],
            WeekNum=init_param['WeekNum'],
            startDate=init_param['startDate'],
            endDate=init_param['endDate'],
            RuSheNum=init_param['RuSheNum'],
            nGeneration=init_param['nGeneration'],
            nDraftOrOriginal=init_param['nDraftOrOriginal'],
            nBirdsType=init_param['nBirdsType'],
            Remark=init_param['Remark']
        )



'''
根据年份和月度，把分公司和分品种的入舍量，汇总到整体的入舍表中
'''
def get_rushe_num(year,week_num):
    RuSheNum = 0
    try:
        res = IntroducedInfoDetail.objects.values().filter(Year=year,WeekNum=week_num)
        for index in res:
            RuSheNum += index['RuSheNum']
    except Exception as e:
        print('get_rushe_num:The Error Reason is :',e)

    return RuSheNum




'''
将IntroducedInfoDetail中的分公司和分品种的数据汇总到IntroducedInfo中
'''
def gen_total_introdeced_data(nGeneration=1,nDraftOrOriginal=1,nBirdsType=1,Remark=''):
    ##  step0: 清除表中所有数据
    clean_introducd_info(nGeneration)
    ##  step1: 获取引种时间列表
    time_res = IntroducedInfoDetail.objects.values('Year','WeekNum').distinct()
    print(Remark,type(Remark))
    ## step2: 按时间列表插入数据
    for index in time_res:
        startDate,endDate = get_start_and_time_by_year_and_weeknum(index['Year'], index['WeekNum'])
        insertDB_introduced_info(
            Year=index['Year'],
            WeekNum = index['WeekNum'],
            startDate = startDate,
            endDate = endDate,
            RuSheNum = get_rushe_num(index['Year'], index['WeekNum']),
            nGeneration = nGeneration,
            nDraftOrOriginal = nDraftOrOriginal,
            nBirdsType = nBirdsType,
            Remark = Remark,

        )



