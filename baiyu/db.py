import pymysql
from pymysql import connect

# from baiyu.function.zudai_to_fumudai import *
from baiyu.models import *
import datetime

class OpenDB(object):
    def __init__(self):
        # 初始化
        self.conn = connect(host='localhost', port=3306, user='root', password='123456', database='forecastsystem', charset='utf8')
        self.cursor = self.conn.cursor()

    def __enter__(self):
        # 返回游标进行执行操作
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 结束提交数据并关闭数据库
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


'''
#获取祖代鸡引种周度总量，返回类型：list
#by sujie 2019/05/27
'''
def get_introduced_detail_all():
    res = []
    try:
        db_res = IntroducedInfoDetail.objects.all()
        for index in db_res:
            res.append(index)
    except Exception as e:
        res = []
        print(e)
    return res



def get_introduced_detail_info(bird_type,nGen):
    introduce_res = []
    with OpenDB() as cursor:
        sql = '''
            SELECT
                bi.id,
                bi.YEAR,
                bi.WeekNum,
                bi.startDate,
                bi.endDate,
                bc.companyName,
                bs.SpeciesName,
                bf.feedWayName,
                bi.RuSheNum,
                bi.LivePeriod,
                bi.nGeneration,
                bi.qzhyFlag,
                bi.Remark
            FROM
                baiyu_introducedinfodetail bi,
                baiyu_companyinfo bc,
                baiyu_feedway bf,
                baiyu_speciesinfo bs
            WHERE
                bi.CompanyId = bc.id
            AND bi.feedWayId = bf.id
            AND bi.SpeciesId = bs.id
            AND bi.nBirdsType = %d
            AND bi.nGeneration = %d
        ''' % (bird_type,nGen)
        try:
            cursor.execute(sql)
            db_res = cursor.fetchall()
            for i in db_res:
                introduce_res.append(i)
        except Exception as e:
            print('Error Reason is :',e)
        print('standard_res',introduce_res)
        return introduce_res


'''
#获取祖代鸡引种周度总表记录条数，返回类型：int
#by sujie 2019/05/27
'''
def get_count_ProgenitorIntroduced(bird_type,nGen):
    try:
        count = IntroducedInfo.objects.filter(nBirdsType=bird_type,nGeneration=nGen).count()
    except Exception as e:
        count = 0
        print('Error Reason is :',e)
    return count


'''
#获取商品代周度统计，返回类型：list
#by sujie 2019/05/27
'''
def get_sWeekly_statistic():
    res = []
    try:
        db_res = WeeklyStatisticTable.objects.all()
        for index in db_res:
            res.append(index)
    except Exception as e:
        print('Error Reason is :',e)
    return res


'''
#获取祖代鸡和父母代机周度标准参数，传入参数为代次，祖代鸡代次为1，父母代为2，商品代为3，返回类型：list
#by sujie 2019/05/30
'''
def get_weekly_standard(nBirdsType,nGeneration):
    standard_res = []
    with OpenDB() as cursor:
        sql = '''
            SELECT
                bws.WeekNum,
                bws.siTaoRate,
                bws.ChanDanRate,
                bws.RuFuZhongDanRate,
                bws.ShouJingRate,
                bws.FuHuaRate,
                bws.JianChuRate,
                bws.SaleRate,
                bws.nGeneration,
                bs.SpeciesName,
                bf.feedWayName,
                bws.Remark
            FROM
                baiyu_weekstandardtable bws
            JOIN baiyu_speciesinfo bs
            JOIN baiyu_feedway bf
            WHERE
                bws.SpeciesId = bs.id
            AND bws.feedWayId = bf.id
            AND bws.nBirdsType = %d
            AND bws.nGeneration = %d
            
        ''' % (nBirdsType,nGeneration)
        try:
            cursor.execute(sql)
            db_res = cursor.fetchall()
            print('****',db_res)
            for i in db_res:
                standard_res.append(i)
        except Exception as e:
            print('Error Reason is :',e)
        return standard_res




'''
#获取父母代鸡周度标准参数，返回类型：list
#by sujie 2019/05/30
'''
# def get_fumudai_weekly_standard():
#     res = []
#     try:
#         db_res = WeekStandardTable.objects.all()
#         for index in db_res:
#             res.append(index)
#     except Exception as e:
#         print('Error Reason is :',e)
#     return res

'''
#获取商品代鸡日度标准参数，返回类型：list
#by sujie 2019/05/30
'''
def get_shangpindai_daily_standard(bird_type):
    res = []
    try:
        db_res = DailyStandardTable.objects.all().values().filter(nBirdsType=bird_type)
        for index in db_res:
            res.append(index)
    except Exception as e:
        print('Error Reason is :',e)
    return res



'''
#获取商品代鸡年度标准参数，返回类型：list
#by sujie 2019/05/30
'''
def get_shangpindai_yearly_param():
    res = []
    try:
        db_res = YearParameter.objects.all()
        for index in db_res:
            res.append(index)
    except Exception as e:
        print('Error Reason is :',e)
    return res


'''
#获取祖代鸡/父母代鸡的总参数，返回类型：list
#by sujie 2019/05/30
'''
def get_all_param(bird_type,nGeneration):
    res = []
    try:
        db_res = WholeParameter.objects.all().values().filter(nBirdsType=bird_type,nGeneration = nGeneration)
        for index in db_res:
            res.append(index)
    except Exception as e:
        print('Error Reason is :',e)
    return res


'''
#获取年度淘汰鸡肉参数（祖代淘汰鸡、父母代淘汰鸡）
#by sujie 2019/05/30
'''
def get_tcjirou_param(bird_type,nGeneration):
    res = []
    try:
        db_res = YearTaotaiJirouParam.objects.all().filter(nBirdsType=bird_type,nGeneration = nGeneration)
        for index in db_res:
            res.append(index)
    except Exception as e:
        print('Error Reason is :',e)
    return res


'''
#获取周度的标注日期
#by sujie 2019/06/04
'''
def get_weeklydate_standard():
    res = []
    try:
        db_res = WeekDateStandard.objects.all()
        for index in db_res:
            res.append(index)
    except Exception as e:
        print('Error Reason is :',e)
    return res

###################################################################
'''
#此部分为计算各项数据 2019-06-28   sujie@boyar.cn
'''
###################################################################

'''
获取引种和入舍的时间列表，入参为代次和家禽种类，返回为list
get_Rushe_timeList（1,4） 为获取祖代白羽肉鸭的引种时间列表
flag为1的不参与计算，为0的参与计算
'''
def get_Sum_Rushe_timeList(nGen,nBirdType,save_type):
    time_list = []
    try:
        res = IntroducedInfo.objects.all().values('Year','WeekNum','LivePeriod','RuSheNum','flag').filter(nGeneration=nGen,nBirdsType=nBirdType,nDraftOrOriginal=save_type,flag=0)
        for index in res:
            time_list.append(index)
    except Exception as e:
        print('The Error Reason is :',e)

    return time_list



def get_Rushe_timeList(nGen,nBirdType,year):
    time_list = []
    try:
        res = IntroducedInfoDetail.objects.all().values('Year','WeekNum','LivePeriod','RuSheNum').filter(nGeneration=nGen,nBirdsType=nBirdType,Year=year)
        for index in res:
            time_list.append(index)
    except Exception as e:
        print('The Error Reason is :',e)

    return time_list

'''
该接口的功能是给出一个星期（年份、第几周）和生存周期，可以得到生存周期之后的周（年份、第几周），
传入的参数是年份、周度、生存周期，返回值类型list，生存周期内的所有星期的年份和周度
'''
def get_period_week(year,weekNum,livePeriod=1):
    # 2006年以前的数据不参与计算，所以从2006年第一周开始参与计算
    _year = 2006
    time_list = []
    try:
        index = WeekDateStandard.objects.all().values('id').filter(Year=year,WeekNum=weekNum)[0]['id']
        # print('index',index)
    except Exception as e:
        print('The Error Reason is :',e)
        index = 1

    limit_start = index - 2
    limit_end = limit_start + livePeriod
    # print(limit_start,limit_end,'qujian')
    try:
        res = WeekDateStandard.objects.all().values('Year','WeekNum').order_by('id')[limit_start:limit_end]
        # print('res',res)
        for item in res:
            time_list.append(item)
    except Exception as e:
        print('The Error Reason is :',e)
        time_list = []
    return time_list


def get_correct_param_by_week(year,week):
    try:
        res = WeekCorrectionFactor.objects.all().values().filter(Year=year,WeekNum=week)[0]
    except Exception as e:
        print(str(e))

    return res

'''
将每周计算的结果插入baiyu_weeklyCoreTable中
Time: 2019-06-28 
Author:sujie@boyar.cn
'''
def insert_baiyu_weekly_core(Year,WeekNum,TotalYuChengCunLan):
    pass


'''
根据年份和第几周，获取此周的入舍量
入参为：year，week_num，返回值为int
'''
def get_rushe_by_week(year,week_num):
    try:
        rusheNum = IntroducedInfoDetail.objects.values('RuSheNum').filter(Year=year,WeekNum=week_num)[0]['RuSheNum']
    except Exception as e:
        rusheNum = 0
        print('get_rushe_by_week:The Error Reason is :',e)
    return rusheNum

'''
#根据生产周期的第几周，获取死淘率
'''


# def calc_baiyu_weekly_median_core():
#     rushe_DateList = get_Rushe_timeList()[0:3]
#     for index in rushe_DateList:
#         ##step 1:判断上周是否有入舍的鸡苗，如果有查找上周的死淘率
#         # print(index['Year'],index['WeekNum'])
#         last_week = get_period_week(index['Year'],index['WeekNum'],1)[0]
#         print('last_week',last_week)
#         last_week_rushe = get_rushe_by_week(last_week['Year'],last_week['WeekNum'])
#         current_week_rushe = get_rushe_by_week(index['Year'],index['WeekNum'])
#
#         sum_rushe = last_week_rushe + current_week_rushe
#         print('Current Rushe is :',sum_rushe)
#         ##step 2:查看本周是否有入舍的鸡苗，如果有直接加上上周死淘后的鸡苗数量

'''
#根据第几周获取该生产周的死淘率，入参是第几周，返回值为死淘率
ahthor : sujie@boyar.cn
date : 2019-07-02
'''
def get_sitaoRate_by_weekCount(week_num):
    try:
        res = WeekStandardTable.objects.values('siTaoRate').filter(WeekNum=week_num,nGeneration=1)[0]['siTaoRate']
    except Exception as e:
        res = 0
        print('get_sitaoRate_by_weekCount:The Error Reason is:',e,'siTaoLv is invalid !!!')
    return res


'''
#根据第几周获取该生产周的周度生产指标，入参是第几周，返回值为死淘率
ahthor : sujie@boyar.cn
date : 2019-07-04
'''
def get_weekly_param_standard(week_num,bird_type,nGen,SpeciesId=6,feedWayId=1):
    param_res = {
        'SpeciesId' : 1,
        'feedWayId' : 1,
        'siTaoRate' : 0,
        'ChanDanRate' : 0,
        'RuFuZhongDanRate' : 0,
        'ShouJingRate' : 0,
        'FuHuaRate' : 0,
        'JianChuRate' : 0,
        'SaleRate' : 0
    }
    try:
        param_res = WeekStandardTable.objects.values().filter(WeekNum=week_num,nGeneration=nGen,nBirdsType=bird_type)[0]
    except Exception as e:
        print('get_weekly_param_standard:The Error Reason is :',e)

    return param_res


'''
根据年份和周度，获取种蛋数量
'''
def get_chandan_num(year,week_num,origin_year,origin_week,bird_type,nGen):
    dan_num = 0
    try:
        dan_num = WeeklyIntroducedMedian.objects.values('TotalDan').filter(Year=year,WeekNum=week_num,originYear=origin_year,originWeek=origin_week,nBirdsType=bird_type,nGeneration=nGen)[0]['TotalDan']
    except Exception as e:
        print('get_chandan_num:The Error Reason is :',e)

    return dan_num


'''
获取淘汰鸡肉的体重和屠宰率，入参是年份，返回值是dict
'''
def get_taotaiji_param(year,bird_type,nGen):
    param = {}
    try:
        param = YearTaotaiJirouParam.objects.all().values().filter(nYear=year,nBirdsType=bird_type,nGeneration=nGen)[0]
    except Exception as e:
        print('get_taotaiji_param:The Error Reason is:',e)

    return param


'''
获取淘汰鸡肉的体重和屠宰率，入参是年份，返回值是dict
'''
def get_taotaiji_param_all(bird_type,nGen):
    param = {}
    try:
        param = YearTaotaiJirouParam.objects.all().values().filter(nBirdsType=bird_type,nGeneration=nGen)
    except Exception as e:
        print('get_taotaiji_param:The Error Reason is:',e)

    return param


# def calc_baiyu_weekly_median_core(bird_type,nGen,CompanyId,SpeciesId,feedWayId,chandan_interval=3):
#     # now_time1 = datetime.datetime.now()
#     rushe_DateList = get_Rushe_timeList(nGen,bird_type,2006)
#     # now_time2 = datetime.datetime.now()
#     ## 清空baiyu_weeklyintroducedmedian数据库数据
#     cleanup_weeklyintroducedmedian(bird_type,nGen)
#
#     # med_core_data_list = []
#
#     for index in rushe_DateList:
#         #根据年份、周度和生存周期，计算所有在生存周期内的数据
#         start_year = index['Year']  #2006
#         start_week = index['WeekNum']  #2
#         rushe_num = index['RuSheNum']  #15000
#
#         for iWeek in range(index['LivePeriod']+3):
#             shengchanWeek = iWeek+1
#             param = get_weekly_param_standard(iWeek+1,bird_type,nGen,SpeciesId,feedWayId)
#             ##根据起始年和周，算接下来生存周期内的每个周度的年和周，如2006年第1周 三周后是 2006年第4周
#             cur_year,cur_week = get_week_info_by_offset(start_year,start_week,iWeek)
#             start_date,end_date = get_start_end_date_by_week(cur_year,cur_week)
#             yuchengCunlan = 0
#             chandanCunlan = 0
#             chandanNum = 0
#             chuji_num = 0
#             real_sale_chuji_num = 0
#             TaoTaiJiNum = 0
#             taotai_jirou = 0
#
#             if iWeek == index['LivePeriod']:
#                 TaoTaiJiNum = rushe_num
#             else:
#                 TaoTaiJiNum = 0
#
#                 ### 生产周小于25周为育成期，25周之后进入产蛋期
#             if iWeek < index['LivePeriod']:
#                 if shengchanWeek < 25:  #25需要改成动态获取
#                     yuchengCunlan = rushe_num   #15000
#                     chandanCunlan = 0
#                 else:
#                     yuchengCunlan = 0
#                     chandanCunlan = rushe_num
#
#             ##根据产蛋期存栏数，计算产蛋的数量
#             chandanNum = round(chandanCunlan*param['ChanDanRate']/100*7)
#
#             '''
#             获取三个星期之前的产蛋数量,孵化周期是21天，按照3周计算
#             '''
#             _3week_before_year,_3week_before_weeknum, = get_week_info_by_offset(cur_year,cur_week,chandan_interval*(-1))
#             dan_init = get_chandan_num(_3week_before_year, _3week_before_weeknum,start_year,start_week,bird_type,nGen)
#             _3week_before_param = get_weekly_param_standard((shengchanWeek-chandan_interval),bird_type,nGen,SpeciesId,feedWayId)
#             shoujing_rate = _3week_before_param['ShouJingRate']/100
#             rufu_zhongdan_rate = _3week_before_param['RuFuZhongDanRate']/100
#             fuhua_rate = _3week_before_param['FuHuaRate']/100
#             jianchu_rate = param['JianChuRate']/100
#             if nGen == 1:
#                 chuji_num = round(dan_init*shoujing_rate*rufu_zhongdan_rate*fuhua_rate*jianchu_rate*0.45)
#             else:
#                 chuji_num = round(dan_init * shoujing_rate * rufu_zhongdan_rate * fuhua_rate * jianchu_rate)
#             real_sale_chuji_num = chuji_num
#
#
#             # print(rushe_num,cur_year,cur_week,shengchanWeek,yuchengCunlan,chandanCunlan,chandanNum,chuji_num,TaoTaiJiNum,taotai_jirou)
#             taotaiji_param = get_taotaiji_param(cur_year,bird_type, nGen)
#             taotai_jirou = TaoTaiJiNum * taotaiji_param['StandardTZ'] * taotaiji_param['TuZaiRate']*1.0/100
#             insertDB_median_baiyu(
#                 originYear = start_year,
#                 originWeek = start_week,
#                 Year = cur_year,
#                 WeekNum = cur_week,
#                 startDate = start_date,
#                 endDate = end_date,
#                 CompanyId = CompanyId,
#                 SpeciesId = SpeciesId,
#                 feedWayId = feedWayId,
#                 shengchanWeek = shengchanWeek,
#                 TotalYuChengCunLan = yuchengCunlan,
#                 TotalChanDanCunLan = chandanCunlan,
#                 TotalDan = chandanNum,
#                 TotalChuJi = chuji_num,
#                 TotalFactSaleChuJi = real_sale_chuji_num,
#                 TaoTaiJiNum = TaoTaiJiNum,
#                 dTaoTaiJiRou = taotai_jirou,
#                 nBirdsType = bird_type,
#                 nGeneration = nGen,
#             )
#             rushe_num = round(rushe_num*(100-param['siTaoRate'])/100)
#     # WeeklyIntroducedMedian.objects.bulk_create(med_core_data_list)



'''
根据年份和月度，计算该周的育成期存栏量和产蛋期存栏量
'''
def get_data_from_median(year,week_num,bird_type,nGen):
    TotalYuChengCunLan = 0
    TotalChanDanCunLan = 0
    TotalDan = 0
    TotalChuJi = 0
    TotalFactSaleChuJi = 0
    TaoTaiJiNum = 0
    dTaoTaiJiRou = 0
    try:
        res = WeeklyIntroducedMedian.objects.values().filter(Year=year,
                                                             WeekNum=week_num,
                                                             nBirdsType=bird_type,
                                                             nGeneration=nGen)
        for index in res:
            TotalYuChengCunLan += index['TotalYuChengCunLan']
            TotalChanDanCunLan += index['TotalChanDanCunLan']
            TotalDan += index['TotalDan']
            TotalChuJi += index['TotalChuJi']
            TotalFactSaleChuJi += index['TotalFactSaleChuJi']
            TaoTaiJiNum += index['TaoTaiJiNum']
            dTaoTaiJiRou +=  index['dTaoTaiJiRou']
    except Exception as e:
        print('get_data_total_from_median:The Error Reason is :',e)

    return TotalYuChengCunLan,TotalChanDanCunLan,TotalDan,TotalChuJi,TotalFactSaleChuJi,TaoTaiJiNum,dTaoTaiJiRou



'''
根据年份和月度，计算该周的育成期存栏量和产蛋期存栏量
'''
def get_data_sum_from_median(year,week_num,bird_type,nGen,save_type):
    data_med = {
        'TotalYuChengCunLan':0,
        'TotalChanDanCunLan':0,
        'TotalDan':0,
        'TotalChuJi':0,
        'TotalFactSaleChuJi':0,
        'TaoTaiJiNum':0,
        'dTaoTaiJiRou':0
    }
    try:
        res = WeeklyIntroducedSumMedian.objects.values().filter(Year=year,WeekNum=week_num,nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type)
        for index in res:
            data_med['TotalYuChengCunLan'] += index['TotalYuChengCunLan']
            data_med['TotalChanDanCunLan'] += index['TotalChanDanCunLan']
            data_med['TotalDan'] += index['TotalDan']
            data_med['TotalChuJi'] += index['TotalChuJi']
            data_med['TotalFactSaleChuJi'] += index['TotalFactSaleChuJi']
            data_med['TaoTaiJiNum'] += index['TaoTaiJiNum']
            data_med['dTaoTaiJiRou'] +=  index['dTaoTaiJiRou']
    except Exception as e:
        print('get_data_total_from_median:The Error Reason is :',e)

    return data_med

'''
根据年份、第几周和偏移量（当前周后的多少周即为偏移量），获取偏移量周后的年份和第几周
'''
def get_week_info_by_offset(current_year,current_weeknum,offset):
    try:
        index = WeekDateStandard.objects.all().values('id').filter(Year=current_year, WeekNum=current_weeknum)[0]['id']
    except Exception as e:
        print('The Error Reason is :', e)
        index = 1
    try:
        res = WeekDateStandard.objects.values('Year','WeekNum').filter(id=index+offset)[0]
        dest_year = res['Year']
        dest_weeknum = res['WeekNum']
    except Exception as e:
        print(e)

    return dest_year,dest_weeknum


'''
向存储白羽肉鸡中间值的插入数据
'''
def insertDB_median_baiyu(**kwargs):

    param_init = {
        'originYear':0,
        'originWeek':0,
        'Year':2050,
        'WeekNum':1,
        'startDate':'2050-01-01',
        'endDate':'2050-01-07',
        'CompanyId':14,
        'SpeciesId':6,
        'feedWayId':1,
        'shengchanWeek': 0,
        'TotalYuChengCunLan':0,
        'TotalChanDanCunLan':0,
        'TotalDan':0,
        'TotalChuJi':0,
        'TotalFactSaleChuJi':0,
        'TaoTaiJiNum':0,
        'dTaoTaiJiRou':0,
        'nGeneration':1,
        'nDraftOrOriginal':1,
        'nBirdsType':1,
        'Remark':''
    }
    for key in kwargs:
        if key in param_init.keys():
            param_init[key] = kwargs[key]
        else:
            pass


    WeeklyIntroducedMedian.objects.create(
        originYear = param_init['originYear'],
        originWeek = param_init['originWeek'],
        Year = param_init['Year'],
        WeekNum = param_init['WeekNum'],
        startDate = param_init['startDate'],
        endDate = param_init['endDate'],
        CompanyId = param_init['CompanyId'],
        SpeciesId = param_init['SpeciesId'],
        feedWayId = param_init['feedWayId'],
        shengchanWeek = param_init['shengchanWeek'],
        TotalYuChengCunLan = param_init['TotalYuChengCunLan'],
        TotalChanDanCunLan = param_init['TotalChanDanCunLan'],
        TotalDan = param_init['TotalDan'],
        TotalChuJi = param_init['TotalChuJi'],
        TotalFactSaleChuJi = param_init['TotalFactSaleChuJi'],
        TaoTaiJiNum = param_init['TaoTaiJiNum'],
        dTaoTaiJiRou = param_init['dTaoTaiJiRou'],
        nGeneration = param_init['nGeneration'],
        nDraftOrOriginal = param_init['nDraftOrOriginal'],
        nBirdsType = param_init['nBirdsType'],
        Remark = param_init['Remark']
    )



def  cleanup_weeklyintroducedmedian(bird_type,nGen):
    try:
        res = WeeklyIntroducedMedian.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen).delete()
    except Exception as e:
        print("insertDB_median_baiyu:The Error Reason is :", e)
    return

def  cleanup_weeklycoretable(bird_type,nGen,save_type):
    try:
        res = WeeklyCoreTable.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type).delete()
    except Exception as e:
        print("insertDB_median_baiyu:The Error Reason is :", e)
    return

def insertDB_weekly_core_baiyu(**kwargs):

    param_init = {
        'Year':2050,
        'WeekNum':1,
        'startDate':'1000-01-01',
        'endDate':'1000-01-01',
        'TotalYuChengCunLan':0,
        'TotalChanDanCunLan':0,
        'TotalDan':0,
        'TotalChuJi':0,
        'TotalFactSaleChuJi':0,
        'TaoTaiJiNum':0,
        'dTaoTaiJiRou':0,
        'nGeneration':1,
        'nDraftOrOriginal':1,
        'nBirdsType':1,
        'Remark':''
    }
    for key in kwargs:
        if key in param_init.keys():
            param_init[key] = kwargs[key]
        else:
            pass
    try:
        WeeklyCoreTable.objects.create(
            Year = param_init['Year'],
            WeekNum = param_init['WeekNum'],
            startDate = param_init['startDate'],
            endDate = param_init['endDate'],
            TotalYuChengCunLan = param_init['TotalYuChengCunLan'],
            TotalChanDanCunLan = param_init['TotalChanDanCunLan'],
            TotalDan = param_init['TotalDan'],
            TotalChuJi = param_init['TotalChuJi'],
            TotalFactSaleChuJi = param_init['TotalFactSaleChuJi'],
            TaoTaiJiNum = param_init['TaoTaiJiNum'],
            dTaoTaiJiRou = param_init['dTaoTaiJiRou'],
            nGeneration = param_init['nGeneration'],
            nDraftOrOriginal = param_init['nDraftOrOriginal'],
            nBirdsType = param_init['nBirdsType'],
            Remark = param_init['Remark']
        )
    except Exception as e:
        print("The Error Reason is :", e)



'''
根据年份和第几周，获取此周的开始日期和结束日期
'''
def get_start_end_date_by_week(year,week_num):
    try:
        res = WeekDateStandard.objects.values('startDate','endDate').filter(Year=year,WeekNum=week_num)[0]
        start_date = res['startDate']
        end_date = res['endDate']
    except Exception as e:
        start_date = '1000-01-01'
        end_date = '1000-01-01'
        print('get_start_end_date_by_week:The Error Reason is:',e)

    return start_date,end_date


def get_company_info():
    res = []
    try:
        res = CompanyInfo.objects.all().values()
    except Exception as e:
        print('get_company_info:The Error Reason is:',e)

    return res

def get_company_info_by_id(company_id):
    res = []
    try:
        res = CompanyInfo.objects.values().filter(id = company_id)
    except Exception as e:
        print(e)
    return res

def get_feedway_info():
    res = []
    try:
        res = FeedWay.objects.all().values()
    except Exception as e:
        print("get_feedway_info:The Error Reason is:",e)

    return res


def get_species_info():
    result = []
    try:
        result = SpeciesInfo.objects.all().values()
    except Exception as e:
        print('get_species_info:The Error Reason is:',e)

    return result


'''
获取祖代鸡的一日龄雏鸡数量
'''
def get_zudai_chuji_info():
    chuji_list = []
    zd_res = WeeklyCoreTable.objects.values('Year','WeekNum','TotalFactSaleChuJi')
    for index in zd_res:
        # print(index['Year'],index['WeekNum'],index['TotalFactSaleChuJi'])
        chuji_list.append(index)
    return chuji_list


'''
将祖代鸡的一日龄雏鸡的数量，作为父母代鸡的插入父母代引种
'''
def fumudai_introduced_info(*args):

    pass


def insertDB_introduced_detail_info(**kwargs):
    if not kwargs:
        print('no valid kwargs')
        return
    else:
        print('database would be updated')
        init_param ={
            'Year':0,
            'WeekNum':0,
            'startDate':'1000-1-1',
            'endDate':'1000-1-1',
            'CompanyId':0,
            'SpeciesId':0,
            'feedWayId':0,
            'RuSheNum':0,
            'LivePeriod':0,
            'qzhyFlag':0,
            'huanyuRate':0,
            'qzhyStartWeek':0,
            'HuanyuInterval':0,
            'qzhyPeriod':0,
            'nGeneration':0,
            'nDraftOrOriginal':0,
            'nBirdsType':0,
            'Remark':0
        }
        for key in kwargs:
            if key in init_param.keys():
                init_param[key] = kwargs[key]
            else:
                print('Keep the origin key and value!')

        IntroducedInfoDetail.objects.create(
            Year=init_param['Year'],
            WeekNum=init_param['WeekNum'],
            startDate=init_param['startDate'],
            endDate=init_param['endDate'],
            CompanyId=init_param['CompanyId'],
            SpeciesId=init_param['SpeciesId'],
            feedWayId=init_param['feedWayId'],
            RuSheNum=init_param['RuSheNum'],
            LivePeriod=init_param['LivePeriod'],
            qzhyFlag=init_param['qzhyFlag'],
            huanyuRate=init_param['huanyuRate'],
            qzhyStartWeek=init_param['qzhyStartWeek'],
            HuanyuInterval=init_param['HuanyuInterval'],
            qzhyPeriod=init_param['qzhyPeriod'],
            nGeneration=init_param['nGeneration'],
            nDraftOrOriginal=init_param['nDraftOrOriginal'],
            nBirdsType=init_param['nBirdsType'],
            Remark=init_param['Remark']
        )



def insertDB_introduced_sum_info(**kwargs):
    if not kwargs:
        print('no valid kwargs')
        return
    else:
        print('database would be updated')
        init_param ={
            'Year':0,
            'WeekNum':0,
            'startDate':'1000-1-1',
            'endDate':'1000-1-1',
            'RuSheNum':0,
            'LivePeriod':0,
            'nGeneration':0,
            'nDraftOrOriginal':0,
            'nBirdsType':0,
            'Remark':0,
            'flag':0
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
            LivePeriod=init_param['LivePeriod'],
            nGeneration=init_param['nGeneration'],
            nDraftOrOriginal=init_param['nDraftOrOriginal'],
            nBirdsType=init_param['nBirdsType'],
            Remark=init_param['Remark']
        )

def clean_introducd_info(bird_type,nGen):
    try:
        res = IntroducedInfo.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen).delete()
    except Exception as e:
        print("clean_introducd_info:The Error Reason is:",str(e))

    return




'''
出栏数和肉量统计
'''
def insertDB_weekly_detail_statistics(**kwargs):
    param_init =  {
        'Year': 0,
        'WeekNum': 0,
        'startDate': '1000-01-01',
        'endDate': '1000-01-01',
        'CunlLanNum35': 0,
        'CunlLanNum42': 0,
        'CunlLanNum49': 0,
        'CunlLanNum56': 0,
        'ChuLanRouJiNum35': 0,
        'ChuLanRouJiNum42': 0,
        'ChuLanRouJiNum49': 0,
        'ChuLanRouJiNum56': 0,
        'TotalChuLanRouJiNum': 0,
        'HuoZhong35': 0,
        'HuoZhong42': 0,
        'HuoZhong49': 0,
        'HuoZhong56': 0,
        'TotalHuoZhong': 0,
        'JiRou35': 0,
        'JiRou42': 0,
        'JiRou49': 0,
        'JiRou56': 0,
        'TotalJiRou': 0,
        'JiXiong35': 0,
        'JiXiong42': 0,
        'JiXiong49': 0,
        'JiXiong56': 0,
        'TotalJiXiong': 0,
        'JiChi35': 0,
        'JiChi42': 0,
        'JiChi49': 0,
        'JiChi56': 0,
        'TotalJiChi': 0,
        'JiTui35': 0,
        'JiTui42': 0,
        'JiTui49': 0,
        'JiTui56': 0,
        'TotalJiTui': 0,
        'JiGuJia35': 0,
        'JiGuJia42': 0,
        'JiGuJia49': 0,
        'JiGuJia56': 0,
        'TotalJiGuJia': 0,
        'JiNeiZang35': 0,
        'JiNeiZang42': 0,
        'JiNeiZang49': 0,
        'JiNeiZang56': 0,
        'TotalJiNeiZang': 0,
        'nDraftOrOriginal': 1,
        'nBirdsType':1,
        'Remark': '',
    }
    for key in kwargs:
        if key in param_init.keys():
            param_init[key] = kwargs[key]
        else:
            pass


    WeeklyStatisticDetail.objects.create(
        Year=param_init['Year'],
        WeekNum=param_init['WeekNum'],
        startDate=param_init['startDate'],
        endDate=param_init['endDate'],
        CunlLanNum35=param_init['CunlLanNum35'],
        CunlLanNum42=param_init['CunlLanNum42'],
        CunlLanNum49=param_init['CunlLanNum49'],
        CunlLanNum56=param_init['CunlLanNum56'],
        ChuLanRouJiNum35=param_init['ChuLanRouJiNum35'],
        ChuLanRouJiNum42=param_init['ChuLanRouJiNum42'],
        ChuLanRouJiNum49=param_init['ChuLanRouJiNum49'],
        ChuLanRouJiNum56=param_init['ChuLanRouJiNum56'],
        TotalChuLanRouJiNum=param_init['TotalChuLanRouJiNum'],
        HuoZhong35=param_init['HuoZhong35'],
        HuoZhong42=param_init['HuoZhong42'],
        HuoZhong49=param_init['HuoZhong49'],
        HuoZhong56=param_init['HuoZhong56'],
        TotalHuoZhong=param_init['TotalHuoZhong'],
        JiRou35=param_init['JiRou35'],
        JiRou42=param_init['JiRou42'],
        JiRou49=param_init['JiRou49'],
        JiRou56=param_init['JiRou56'],
        TotalJiRou=param_init['TotalJiRou'],
        JiXiong35=param_init['JiXiong35'],
        JiXiong42=param_init['JiXiong42'],
        JiXiong49=param_init['JiXiong49'],
        JiXiong56=param_init['JiXiong56'],
        TotalJiXiong=param_init['TotalJiXiong'],
        JiChi35=param_init['JiChi35'],
        JiChi42=param_init['JiChi42'],
        JiChi49=param_init['JiChi49'],
        JiChi56=param_init['JiChi56'],
        TotalJiChi=param_init['TotalJiChi'],
        JiTui35=param_init['JiTui35'],
        JiTui42=param_init['JiTui42'],
        JiTui49=param_init['JiTui49'],
        JiTui56=param_init['JiTui56'],
        TotalJiTui=param_init['TotalJiTui'],
        JiGuJia35=param_init['JiGuJia35'],
        JiGuJia42=param_init['JiGuJia42'],
        JiGuJia49=param_init['JiGuJia49'],
        JiGuJia56=param_init['JiGuJia56'],
        TotalJiGuJia=param_init['TotalJiGuJia'],
        JiNeiZang35=param_init['JiNeiZang35'],
        JiNeiZang42=param_init['JiNeiZang42'],
        JiNeiZang49=param_init['JiNeiZang49'],
        JiNeiZang56=param_init['JiNeiZang56'],
        TotalJiNeiZang=param_init['TotalJiNeiZang'],
        nDraftOrOriginal=param_init['nDraftOrOriginal'],
        nBirdsType=param_init['nBirdsType'],
        Remark=param_init['Remark']
    )


'''
出栏数和肉量统计
'''
def insertDB_weekly_statistics(**kwargs):
    param_init =  {
        'Year': 0,
        'WeekNum': 0,
        'startDate': '1000-01-01',
        'endDate': '1000-01-01',
        'CunlLanNum35': 0,
        'CunlLanNum42': 0,
        'CunlLanNum49': 0,
        'CunlLanNum56': 0,
        'ChuLanRouJiNum35': 0,
        'ChuLanRouJiNum42': 0,
        'ChuLanRouJiNum49': 0,
        'ChuLanRouJiNum56': 0,
        'TotalChuLanRouJiNum': 0,
        'HuoZhong35': 0,
        'HuoZhong42': 0,
        'HuoZhong49': 0,
        'HuoZhong56': 0,
        'TotalHuoZhong': 0,
        'JiRou35': 0,
        'JiRou42': 0,
        'JiRou49': 0,
        'JiRou56': 0,
        'TotalJiRou': 0,
        'JiXiong35': 0,
        'JiXiong42': 0,
        'JiXiong49': 0,
        'JiXiong56': 0,
        'TotalJiXiong': 0,
        'JiChi35': 0,
        'JiChi42': 0,
        'JiChi49': 0,
        'JiChi56': 0,
        'TotalJiChi': 0,
        'JiTui35': 0,
        'JiTui42': 0,
        'JiTui49': 0,
        'JiTui56': 0,
        'TotalJiTui': 0,
        'JiGuJia35': 0,
        'JiGuJia42': 0,
        'JiGuJia49': 0,
        'JiGuJia56': 0,
        'TotalJiGuJia': 0,
        'JiNeiZang35': 0,
        'JiNeiZang42': 0,
        'JiNeiZang49': 0,
        'JiNeiZang56': 0,
        'TotalJiNeiZang': 0,
        'nDraftOrOriginal': 1,
        'nBirdsType':1,
        'Remark': '',
    }
    for key in kwargs:
        if key in param_init.keys():
            param_init[key] = kwargs[key]
        else:
            pass


    WeeklyStatisticTable.objects.create(
        Year=param_init['Year'],
        WeekNum=param_init['WeekNum'],
        startDate=param_init['startDate'],
        endDate=param_init['endDate'],
        CunlLanNum35=param_init['CunlLanNum35'],
        CunlLanNum42=param_init['CunlLanNum42'],
        CunlLanNum49=param_init['CunlLanNum49'],
        CunlLanNum56=param_init['CunlLanNum56'],
        ChuLanRouJiNum35=param_init['ChuLanRouJiNum35'],
        ChuLanRouJiNum42=param_init['ChuLanRouJiNum42'],
        ChuLanRouJiNum49=param_init['ChuLanRouJiNum49'],
        ChuLanRouJiNum56=param_init['ChuLanRouJiNum56'],
        TotalChuLanRouJiNum=param_init['TotalChuLanRouJiNum'],
        HuoZhong35=param_init['HuoZhong35'],
        HuoZhong42=param_init['HuoZhong42'],
        HuoZhong49=param_init['HuoZhong49'],
        HuoZhong56=param_init['HuoZhong56'],
        TotalHuoZhong=param_init['TotalHuoZhong'],
        JiRou35=param_init['JiRou35'],
        JiRou42=param_init['JiRou42'],
        JiRou49=param_init['JiRou49'],
        JiRou56=param_init['JiRou56'],
        TotalJiRou=param_init['TotalJiRou'],
        JiXiong35=param_init['JiXiong35'],
        JiXiong42=param_init['JiXiong42'],
        JiXiong49=param_init['JiXiong49'],
        JiXiong56=param_init['JiXiong56'],
        TotalJiXiong=param_init['TotalJiXiong'],
        JiChi35=param_init['JiChi35'],
        JiChi42=param_init['JiChi42'],
        JiChi49=param_init['JiChi49'],
        JiChi56=param_init['JiChi56'],
        TotalJiChi=param_init['TotalJiChi'],
        JiTui35=param_init['JiTui35'],
        JiTui42=param_init['JiTui42'],
        JiTui49=param_init['JiTui49'],
        JiTui56=param_init['JiTui56'],
        TotalJiTui=param_init['TotalJiTui'],
        JiGuJia35=param_init['JiGuJia35'],
        JiGuJia42=param_init['JiGuJia42'],
        JiGuJia49=param_init['JiGuJia49'],
        JiGuJia56=param_init['JiGuJia56'],
        TotalJiGuJia=param_init['TotalJiGuJia'],
        JiNeiZang35=param_init['JiNeiZang35'],
        JiNeiZang42=param_init['JiNeiZang42'],
        JiNeiZang49=param_init['JiNeiZang49'],
        JiNeiZang56=param_init['JiNeiZang56'],
        TotalJiNeiZang=param_init['TotalJiNeiZang'],
        nDraftOrOriginal=param_init['nDraftOrOriginal'],
        nBirdsType=param_init['nBirdsType'],
        Remark=param_init['Remark']
    )



def get_xuanyongrate(bird_type,nGen):
    result = 0
    try:
        result = WholeParameter.objects.all().values('XuanYongRate').filter(nBirdsType=bird_type,nGeneration=nGen)[0]['XuanYongRate']
    except Exception as e:
        print('The error reson is:',str(e))
    return result


# def calc_baiyu_weekly_median_core(bird_type,nGen,CompanyId,SpeciesId,feedWayId,chandan_interval=3):
#
#     print("%"*20)
#     param_all = get_weekly_param_standard_all(bird_type,nGen,SpeciesId,feedWayId)
#     taotaiji_param_all = get_taotaiji_param_all(bird_type,nGen)
#     xuanyongrate = get_xuanyongrate(bird_type,nGen)
#     date_list = get_date_standard_list()
#     print("%" * 20)
#     rushe_DateList = get_Rushe_timeList(nGen,bird_type,2006)
#
#     ## 清空baiyu_weeklyintroducedmedian数据库数据
#     cleanup_weeklyintroducedmedian(bird_type,nGen)
#
#     med_core_data_list = []
#
#     for index in rushe_DateList:
#         #根据年份、周度和生存周期，计算所有在生存周期内的数据
#         start_year = index['Year']  #2006
#         start_week = index['WeekNum']  #2
#         rushe_num = index['RuSheNum']  #15000
#         dan_tmp_list = []
#         for iWeek in range(index['LivePeriod']+chandan_interval):
#             cur_year,cur_week,start_date,end_date = get_year_week_by_offset_function(date_list, start_year, start_week, iWeek)
#             shengchanWeek = iWeek+1
#             ##根据起始年和周，算接下来生存周期内的每个周度的年和周，如2006年第1周 三周后是 2006年第4周
#             yuchengCunlan = 0
#             chandanCunlan = 0
#             chandanNum = 0
#             chuji_num = 0
#             real_sale_chuji_num = 0
#             TaoTaiJiNum = 0
#             taotai_jirou = 0
#
#             if iWeek == index['LivePeriod']:
#                 TaoTaiJiNum = rushe_num
#             else:
#                 TaoTaiJiNum = 0
#
#             if iWeek < index['LivePeriod']:
#                 ### 生产周小于25周为育成期，25周之后进入产蛋期
#                 if shengchanWeek < 25:  #25需要改成动态获取
#                     yuchengCunlan = rushe_num   #15000
#                     chandanCunlan = 0
#                 else:
#                     yuchengCunlan = 0
#                     chandanCunlan = rushe_num
#
#             ##根据产蛋期存栏数，计算产蛋的数量
#             chandanNum = round(chandanCunlan*param_all[iWeek]['ChanDanRate']/100*7)
#             dan_tmp_list.append(chandanNum)
#
#             '''
#             获取三个星期之前的产蛋数量,孵化周期是21天，按照3周计算
#             '''
#             if shengchanWeek < (25+ chandan_interval):
#                 dan_init = 0
#                 shoujing_rate = 0
#                 rufu_zhongdan_rate = 0
#                 fuhua_rate = 0
#
#             else:
#                 dan_init = dan_tmp_list[iWeek-chandan_interval]
#                 shoujing_rate = param_all[iWeek-chandan_interval]['ShouJingRate'] / 100
#                 rufu_zhongdan_rate = param_all[iWeek-chandan_interval]['RuFuZhongDanRate']/100
#                 fuhua_rate = param_all[iWeek-chandan_interval]['FuHuaRate']/100
#             jianchu_rate = param_all[iWeek]['JianChuRate']/100
#             chuji_num = round(dan_init*shoujing_rate*rufu_zhongdan_rate*fuhua_rate*jianchu_rate*xuanyongrate/100)
#             real_sale_chuji_num = chuji_num
#
#
#             taotai_jirou = TaoTaiJiNum * taotaiji_param_all[index['Year']-1990]['StandardTZ'] * taotaiji_param_all[index['Year']-1990]['TuZaiRate']*1.0/100
#
#             rushe_num = round(rushe_num*(100-param_all[iWeek]['siTaoRate'])/100)
#
#             # print(index['Year'],index['WeekNum'],shengchanWeek,yuchengCunlan, chandanCunlan, chandanNum, chuji_num, real_sale_chuji_num,TaoTaiJiNum,taotai_jirou)
#             item = WeeklyIntroducedMedian(
#
#                 originYear=start_year,
#                 originWeek=start_week,
#                 Year=cur_year,
#                 WeekNum=cur_week,
#                 startDate=start_date,
#                 endDate=end_date,
#                 CompanyId=CompanyId,
#                 SpeciesId=SpeciesId,
#                 feedWayId=feedWayId,
#                 shengchanWeek=shengchanWeek,
#                 TotalYuChengCunLan=yuchengCunlan,
#                 TotalChanDanCunLan=chandanCunlan,
#                 TotalDan=chandanNum,
#                 TotalChuJi=chuji_num,
#                 TotalFactSaleChuJi=real_sale_chuji_num,
#                 TaoTaiJiNum=TaoTaiJiNum,
#                 dTaoTaiJiRou=taotai_jirou,
#                 nBirdsType=bird_type,
#                 nGeneration=nGen,
#                 Remark=''
#             )
#             med_core_data_list.append(item)
#     WeeklyIntroducedMedian.objects.bulk_create(med_core_data_list)


def get_weekly_param_standard_all(bird_type,nGen):
    result = []
    try:
        res = WeekStandardTable.objects.all().values().filter(nBirdsType=bird_type,nGeneration=nGen)
        result = res
    except Exception as e:
        pass
    return result




def get_date_standard_list():
    try:
        res = WeekDateStandard.objects.all().values('id', 'Year', 'WeekNum','startDate','endDate').filter(Year__gt=2000)
    except Exception as e:
        print(e)

    return res


# def get_year_week_by_offset_function(list_res,year,week_num,offset):
#
#     cur_year = '0000-00-00'
#     cur_week = 0
#     tmp = 0
#     for index,elem in enumerate(list_res):
#         if elem['Year'] == year and elem['WeekNum'] == week_num:
#             tmp = index
#             break
#     cur_year = list_res[tmp + offset]['Year']
#     cur_week = list_res[tmp + offset]['WeekNum']
#     start_date = list_res[tmp + offset]['startDate']
#     end_date = list_res[tmp + offset]['endDate']
#     return cur_year,cur_week,start_date,end_date



# def gen_fumudai_introdeced_data(
#         CompanyId = 1,
#         SpeciesId = 1,
#         feedWayId = 1,
#         nGen=2,
#         nDraftOrOriginal=1,
#         nBirdsType=1,
#         Remark=''
#     ):
#     ##  step0: 清除表中原有的父母代入舍所有数据
#     clean_introducd_detail_info(nBirdsType,nGen)
#     ##  step1: 获取父母代引种时间列表
#     time_res = IntroducedInfoDetail.objects.values('Year','WeekNum','LivePeriod').filter(nBirdsType=nBirdsType,nGeneration=nGen-1)
#     ## step2: 按时间列表插入数据
#     for index in time_res:
#         startDate,endDate = get_start_end_date_by_week(index['Year'], index['WeekNum'])
#         rushe_num = get_fumudai_rushe_num(index['Year'], index['WeekNum'], nBirdsType, nGen-1)
#         print(startDate,endDate,rushe_num)
#         insertDB_introduced_detail_info(
#             Year=index['Year'],
#             WeekNum=index['WeekNum'],
#             startDate=startDate,
#             endDate=endDate,
#             CompanyId=CompanyId,
#             SpeciesId=SpeciesId,
#             feedWayId=feedWayId,
#             RuSheNum=rushe_num,  ##根据祖代鸡的实际销售的雏鸡数量得来
#             LivePeriod=index['LivePeriod'],  ##根据父母代鸡的周标准得来
#             qzhyFlag= 0 ,
#             huanyuRate= 0,
#             qzhyStartWeek=0,
#             HuanyuInterval=0,
#             qzhyPeriod=0,
#             nGeneration = nGen,
#             nDraftOrOriginal = nDraftOrOriginal,
#             nBirdsType = nBirdsType,
#             Remark=Remark
#         )



def clean_introducd_detail_info(nBirdsType,nGen):
    try:
        IntroducedInfoDetail.objects.filter(nBirdsType=nBirdsType,nGeneration=nGen).delete()
    except Exception as e:
        print(e)

def get_fumudai_rushe_num(year,week_num,bird_type,nGen):

    RuSheNum = 0
    try:
        res = WeeklyCoreTable.objects.values('TotalFactSaleChuJi').filter(Year = year, WeekNum= week_num,nBirdsType=bird_type,nGeneration=nGen)
        RuSheNum = res[0]['TotalFactSaleChuJi']
    except Exception as e:
        print('get_fumudai_rushe_num:The error reason is :',str(e))

    return RuSheNum


def  cleanup_weeklyintroducedmedian(bird_type,nGen):
    try:
        res = WeeklyIntroducedMedian.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen).delete()
    except Exception as e:
        print('The Error Reason is :',str(e))
