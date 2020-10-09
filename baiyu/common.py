from baiyu.models import *
from django.db.models import Q,Sum,Count,Avg

'''
根据给定的年份和周度，输出该周度的开始日期和结束日期，返回值为元组
'''
def get_start_and_time_by_year_and_weeknum(year,week_num):
    try:
        time_res = WeekDateStandard.objects.values('startDate','endDate').filter(Year=year,WeekNum=week_num)[0]
        startDate = time_res['startDate']
        endDate = time_res['endDate']
    except Exception as e:
        print('The Error Reason is:',str(e))
        startDate = ''
        endDate = ''

    return startDate,endDate


def get_total_introduced_info(bird_type,nGen,save_type):
    result = []
    try:
        res = IntroducedInfo.objects.all().values().filter(nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type)
        for index in res:
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            result.append(index)
    except Exception as e:
        print('get_total_introduced_info:The Error Reason is:',str(e))
    return result


def get_zudai_statistic(bird_type,nGen):
    result = []
    try:
        res = WeeklyCoreTable.objects.all().values().filter(nBirdsType=bird_type,nGeneration=nGen)
        for index in res:
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            result.append(index)
    except Exception as e:
        print('get_zudai_statistic:The Error Reason is:',str(e))
    return result


def get_daici_statistic_count(bird_type,nGen):
    result = 0
    try:
        result = WeeklyCoreTable.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen).count()
    except Exception as e:
        print('The error reason is:',str(e))
    return result



def get_year_week_by_offset_function(list_res,year,week_num,offset):

    cur_year = '1000-01-01'
    cur_week = 0
    tmp = 0
    for index,elem in enumerate(list_res):
        if elem['Year'] == year and elem['WeekNum'] == week_num:
            tmp = index
            break
    cur_year = list_res[tmp + offset]['Year']
    cur_week = list_res[tmp + offset]['WeekNum']
    start_date = list_res[tmp + offset]['startDate']
    end_date = list_res[tmp + offset]['endDate']
    return cur_year,cur_week,start_date,end_date


'''
获取XX年XX周到YY年YY周中间的时间id列表
'''
def get_date_id_list(start_year,start_week,end_year,end_week,nGen):
    id_list = []
    id_list_all = []
    try:
        id_list_dict = WeekCorrectionFactor.objects.filter(nGeneration=nGen).values('id').distinct()
        for index in id_list_dict:
            id_list_all.append(index['id'])
        start_id = WeekCorrectionFactor.objects.values('id').filter(nGeneration=nGen).filter(Year=start_year,WeekNum=start_week)[0]['id']
        end_id = WeekCorrectionFactor.objects.values('id').filter(nGeneration=nGen).filter(Year=end_year, WeekNum=end_week)[0]['id']
        for index in range(start_id,end_id+1):
            if index in id_list_all:
                id_list.append(index)
    except Exception as e:
        print(str(e))

    return id_list


'''
获取死淘率调整信息
'''

def get_sitaorate_correct_info(nGen):
    sitaorate_correct_list = []
    try:
        res = WeekCorrectionFactor.objects.all().values('Year','WeekNum','startDate','endDate','SiTaoC','SiTaoCNote').filter(nGeneration=nGen).filter(Q(SiTaoC__gt=0) | Q(SiTaoC__lt=0))
        for key,index in enumerate(res):
            index['id'] = key+1
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            sitaorate_correct_list.append(index)
    except Exception as e:
        print(str(e))

    return sitaorate_correct_list


def get_chandanrate_correct_info(nGen):
    chandanrate_correct_list = []
    try:
        res = WeekCorrectionFactor.objects.all().values('Year','WeekNum','startDate','endDate','ChanDanC','ChanDanCNote').filter(nGeneration=nGen).filter(Q(ChanDanC__gt=0) | Q(ChanDanC__lt=0))
        for key,index in enumerate(res):
            index['id'] = key+1
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            chandanrate_correct_list.append(index)
    except Exception as e:
        print(str(e))

    return chandanrate_correct_list



def get_rufurate_correct_info(nGen):
    rufurate_correct_list = []
    try:
        res = WeekCorrectionFactor.objects.all().values('Year','WeekNum','startDate','endDate','RuFuZhongDanC','RuFuZhongDanCNote').filter(nGeneration=nGen).filter(Q(RuFuZhongDanC__gt=0) | Q(RuFuZhongDanC__lt=0))
        for key,index in enumerate(res):
            index['id'] = key+1
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            rufurate_correct_list.append(index)
    except Exception as e:
        print(str(e))

    return rufurate_correct_list

def get_shoujingrate_correct_info(nGen):
    shoujingrate_correct_list = []
    try:
        res = WeekCorrectionFactor.objects.all().values('Year','WeekNum','startDate','endDate','ShouJingC','ShouJingCNote').filter(nGeneration=nGen).filter(Q(ShouJingC__gt=0) | Q(ShouJingC__lt=0))
        for key,index in enumerate(res):
            index['id'] = key+1
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            shoujingrate_correct_list.append(index)
    except Exception as e:
        print(str(e))

    return shoujingrate_correct_list


def get_fuhuarate_correct_info(nGen):
    fuhuarate_correct_list = []
    try:
        res = WeekCorrectionFactor.objects.all().values('Year','WeekNum','startDate','endDate','FuHuaC','FuHuaCNote').filter(nGeneration=nGen).filter(Q(FuHuaC__gt=0) | Q(FuHuaC__lt=0))
        for key,index in enumerate(res):
            index['id'] = key+1
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            fuhuarate_correct_list.append(index)
    except Exception as e:
        print(str(e))

    return fuhuarate_correct_list



def get_jianchurate_correct_info(nGen):
    jianchurate_correct_list = []
    try:
        res = WeekCorrectionFactor.objects.all().values('Year','WeekNum','startDate','endDate','JianChuC','JianChuCNote').filter(nGeneration=nGen).filter(Q(JianChuC__gt=0) | Q(JianChuC__lt=0))
        for key,index in enumerate(res):
            index['id'] = key+1
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            jianchurate_correct_list.append(index)
    except Exception as e:
        print(str(e))

    return jianchurate_correct_list


def get_salerate_correct_info(nGen):
    salerate_correct_list = []
    try:
        res = WeekCorrectionFactor.objects.all().values('Year','WeekNum','startDate','endDate','SaleRateC','SaleRateCNote').filter(nGeneration=nGen).filter(Q(SaleRateC__gt=0) | Q(SaleRateC__lt=0))
        for key,index in enumerate(res):
            index['id'] = key+1
            index['startDate'] = index['startDate'].strftime('%Y-%m-%d')
            index['endDate'] = index['endDate'].strftime('%Y-%m-%d')
            salerate_correct_list.append(index)
    except Exception as e:
        print(str(e))

    return salerate_correct_list




def get_tongji_data_by_company_and_species(year,week,nGen,company_id,species_id):
    '''
    统计固定年份下的某个公司饲养的某个品种的数量
    :param year:
    :param week:
    :param nGen:
    :param company_id:
    :param species_id:
    :return:
    '''
    result = 0
    try:
        res = IntroducedInfoDetail.objects.all().filter(Year=year, WeekNum=week, nGeneration=nGen).filter(CompanyId=company_id,SpeciesId=species_id).aggregate(RuSheNum=Sum('RuSheNum'))
        if not res['RuSheNum']:
            result = 0
        else:
            result = res['RuSheNum']
    except Exception as e:
        print(str(e))
    return result

def list_add(a):
    '''
    给定一个列表，求该列表的元素的和
    :param a: 
    :return: 
    '''
    c = 0
    for i in range(len(a)):
        c = c + a[i]
    return c


def get_tongji_data_by_species(year,week,nGen,species_id):
    '''
    根据养殖品种统计入舍数量
    :return:
    '''
    result = 0
    try:
        res = IntroducedInfoDetail.objects.all().filter(Year=year, WeekNum=week, nGeneration=nGen).filter(SpeciesId=species_id).aggregate(RuSheNum=Sum('RuSheNum'))
        if not res['RuSheNum']:
            result = 0
        else:
            result = res['RuSheNum']
    except Exception as e:
        print(str(e))
    return result


def get_yearly_tongji_data_by_company_and_species(year,nGen,company_id,species_id):
    '''
    统计固定年份下的某个公司饲养的某个品种的数量
    :param year:
    :param week:
    :param nGen:
    :param company_id:
    :param species_id:
    :return:
    '''
    result = 0
    try:
        res = IntroducedInfoDetail.objects.all().filter(Year=year,nGeneration=nGen).filter(CompanyId=company_id,SpeciesId=species_id).aggregate(RuSheNum=Sum('RuSheNum'))
        if not res['RuSheNum']:
            result = 0
        else:
            result = res['RuSheNum']
    except Exception as e:
        print(str(e))
    return result

def get_yearly_tongji_data_by_species(year,nGen,species_id):
    '''
    根据养殖品种统计入舍数量
    :return:
    '''
    result = 0
    try:
        res = IntroducedInfoDetail.objects.all().filter(Year=year,nGeneration=nGen).filter(SpeciesId=species_id).aggregate(RuSheNum=Sum('RuSheNum'))
        if not res['RuSheNum']:
            result = 0
        else:
            result = res['RuSheNum']
    except Exception as e:
        print(str(e))
    return result