from baiyu.models import *
from django.db.models import Q,Sum,Count,Avg
# from baiyu.function.zudai_to_fumudai import *
from baiyu.db import *
import datetime
from baiyu.common import *

def clean_introducd_info(bird_type,nGen):
    try:
        res = IntroducedInfo.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen).delete()
    except Exception as e:
        print("clean_introducd_info:The Error Reason is:",str(e))

    return

'''
将祖代的实际销售雏鸡数，作为父母带的入舍量，插入引种数据库，nGeneration == 2
'''
def gen_fumudai_introdeced_data(
        nGen=2,
        nDraftOrOriginal=1,
        nBirdsType=1,
        Remark=''
    ):
    ##  step0: 清除表中原有的父母代入舍所有数据
    clean_introducd_info(nBirdsType,nGen)
    ##  step1: 获取父母代引种时间列表
    time_res = WeeklyCoreTable.objects.values('Year','WeekNum').filter(nBirdsType=nBirdsType,nGeneration=nGen-1)
    ## step2: 按时间列表插入数据
    for index in time_res:
        startDate,endDate = get_start_end_date_by_week(index['Year'], index['WeekNum'])
        rushe_num = get_fumudai_rushe_num(index['Year'], index['WeekNum'], nBirdsType, nGen-1,nDraftOrOriginal)
        print(startDate,endDate,rushe_num)
        insertDB_introduced_sum_info(
            Year=index['Year'],
            WeekNum=index['WeekNum'],
            startDate=startDate,
            endDate=endDate,
            RuSheNum=rushe_num,  ##根据祖代鸡的实际销售的雏鸡数量得来
            LivePeriod= 65 ,  ##根据父母代鸡的周标准得来
            nGeneration = nGen,
            nDraftOrOriginal = nDraftOrOriginal,
            nBirdsType = nBirdsType,
            Remark=Remark
        )



def clean_introducd_detail_info(nBirdsType,nGen):
    try:
        IntroducedInfo.objects.filter(nBirdsType=nBirdsType,nGeneration=nGen).delete()
    except Exception as e:
        print(e)

def get_fumudai_rushe_num(year,week_num,bird_type,nGen,save_type):

    RuSheNum = 0
    try:
        res = WeeklyCoreTable.objects.values('TotalFactSaleChuJi').filter(Year = year, WeekNum= week_num,nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type)
        RuSheNum = res[0]['TotalFactSaleChuJi']
    except Exception as e:
        print('get_fumudai_rushe_num:The error reason is :',str(e))

    return RuSheNum


def  cleanup_weeklyintroducedmedian(bird_type,nGen,save_type):
    try:
        res = WeeklyIntroducedMedian.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type).delete()
    except Exception as e:
        print('The Error Reason is :',str(e))



def  cleanup_weekly_introduced_sum_median(bird_type,nGen,save_type):
    try:
        res = WeeklyIntroducedSumMedian.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type).delete()
    except Exception as e:
        print('The Error Reason is :',str(e))

def calc_baiyu_weekly_median_core(bird_type,nGen,chandan_interval,save_type):
    # save_type = 1
    param_all = get_weekly_param_standard_all(bird_type,nGen)
    taotaiji_param_all = get_taotaiji_param_all(bird_type,nGen)
    xuanyongrate = get_xuanyongrate(bird_type,nGen)
    date_list = get_date_standard_list()
    rushe_DateList = get_Sum_Rushe_timeList(nGen,bird_type,save_type)

    ## 清空baiyu_weeklyintroducedmedian数据库数据
    # cleanup_weekly_introduced_sum_median(bird_type,nGen)
    cleanup_weekly_introduced_sum_median(bird_type,nGen,save_type)

    med_core_data_list = []

    for index in rushe_DateList:
        #根据年份、周度和生存周期，计算所有在生存周期内的数据
        start_year = index['Year']  #2006
        start_week = index['WeekNum']  #2
        rushe_num = index['RuSheNum']  #15000
        dan_tmp_list = []
        for iWeek in range(index['LivePeriod']+chandan_interval):
            cur_year,cur_week,start_date,end_date = get_year_week_by_offset_function(date_list, start_year, start_week, iWeek)
            shengchanWeek = iWeek+1
            ##根据起始年和周，算接下来生存周期内的每个周度的年和周，如2006年第1周 三周后是 2006年第4周
            yuchengCunlan = 0
            chandanCunlan = 0
            chandanNum = 0
            chuji_num = 0
            real_sale_chuji_num = 0
            TaoTaiJiNum = 0
            taotai_jirou = 0

            if iWeek == index['LivePeriod']:
                TaoTaiJiNum = rushe_num
            else:
                TaoTaiJiNum = 0

            if iWeek < index['LivePeriod']:
                ### 生产周小于25周为育成期，25周之后进入产蛋期
                if shengchanWeek < 25:  #25需要改成动态获取
                    yuchengCunlan = rushe_num   #15000
                    chandanCunlan = 0
                else:
                    yuchengCunlan = 0
                    chandanCunlan = rushe_num

            ##根据产蛋期存栏数，计算产蛋的数量
            chandanNum = round(chandanCunlan*param_all[iWeek]['ChanDanRate']/100*7)
            dan_tmp_list.append(chandanNum)

            '''
            获取三个星期之前的产蛋数量,孵化周期是21天，按照3周计算
            '''
            if shengchanWeek < (25+ chandan_interval):
                dan_init = 0
                shoujing_rate = 0
                rufu_zhongdan_rate = 0
                fuhua_rate = 0

            else:
                dan_init = dan_tmp_list[iWeek-chandan_interval]
                shoujing_rate = param_all[iWeek-chandan_interval]['ShouJingRate'] / 100
                rufu_zhongdan_rate = param_all[iWeek-chandan_interval]['RuFuZhongDanRate']/100
                fuhua_rate = param_all[iWeek-chandan_interval]['FuHuaRate']/100
            jianchu_rate = param_all[iWeek]['JianChuRate']/100
            chuji_num = round(dan_init*shoujing_rate*rufu_zhongdan_rate*fuhua_rate*jianchu_rate*xuanyongrate/100)
            real_sale_chuji_num = chuji_num


            taotai_jirou = TaoTaiJiNum * taotaiji_param_all[index['Year']-1990]['StandardTZ'] * taotaiji_param_all[index['Year']-1990]['TuZaiRate']*1.0/100

            rushe_num = round(rushe_num*(100-param_all[iWeek]['siTaoRate'])/100)
            item = WeeklyIntroducedSumMedian(
                originYear=start_year,
                originWeek=start_week,
                Year=cur_year,
                WeekNum=cur_week,
                startDate=start_date,
                endDate=end_date,
                shengchanWeek=shengchanWeek,
                TotalYuChengCunLan=yuchengCunlan,
                TotalChanDanCunLan=chandanCunlan,
                TotalDan=chandanNum,
                TotalChuJi=chuji_num,
                TotalFactSaleChuJi=real_sale_chuji_num,
                TaoTaiJiNum=TaoTaiJiNum,
                dTaoTaiJiRou=taotai_jirou,
                nBirdsType=bird_type,
                nGeneration=nGen,
                nDraftOrOriginal = 1,
                Remark=''
            )
            # print(item)
            med_core_data_list.append(item)
        WeeklyIntroducedSumMedian.objects.bulk_create(med_core_data_list)
        med_core_data_list = []
    IntroducedInfo.objects.filter(nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type).update(flag = 1)


def calc_generation_data(bird_type,nGen,save_type):
    print('W'*20,save_type)
    chandan_interval =3
    now_time1 = datetime.datetime.now()
    if int(save_type) == 1:
        print("Hello " * 20)
        calc_baiyu_weekly_median_core(bird_type,nGen,chandan_interval,save_type)

    else:
        print("Correct " * 20)
        calc_baiyu_weekly_correct_median_core_correct(bird_type, nGen, chandan_interval, save_type)

    now_time2 = datetime.datetime.now()
    time_1 = now_time2 - now_time1
    print(time_1)
    cleanup_weeklycoretable(bird_type,nGen,save_type)
    print("#"*30)
    try:
        core_date_list = WeeklyIntroducedSumMedian.objects.values('Year','WeekNum').filter(nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type).distinct()
    except Exception as e:
        core_date_list = []
        print(e)
        return
    weekly_core_list = []
    for index in core_date_list:
        med_dict = get_data_sum_from_median(index['Year'],index['WeekNum'],bird_type,nGen,save_type)
        start_date,end_date = get_start_end_date_by_week(index['Year'],index['WeekNum'])

        item_core = WeeklyCoreTable(
            Year=index['Year'],
            WeekNum=index['WeekNum'],
            startDate = start_date,
            endDate = end_date,
            TotalYuChengCunLan=med_dict['TotalYuChengCunLan'],
            TotalChanDanCunLan=med_dict['TotalChanDanCunLan'],
            TotalDan=med_dict['TotalDan'],
            TotalChuJi=med_dict['TotalChuJi'],
            TotalFactSaleChuJi=med_dict['TotalFactSaleChuJi'],
            TaoTaiJiNum=med_dict['TaoTaiJiNum'],
            dTaoTaiJiRou=med_dict['dTaoTaiJiRou'],
            nBirdsType = bird_type,
            nGeneration= nGen,
            nDraftOrOriginal = save_type
        )
        weekly_core_list.append(item_core)
    WeeklyCoreTable.objects.bulk_create(weekly_core_list)
    now_time3 = datetime.datetime.now()
    time_2 = now_time2 - now_time1
    print('tt'*5,time_2)
    next_ngen = int(nGen)+1
    gen_fumudai_introdeced_data(next_ngen,save_type,bird_type,'')



def calc_baiyu_weekly_correct_median_core_correct(bird_type,nGen,chandan_interval,save_type):
    # save_type = 2
    param_all = get_weekly_param_standard_all(bird_type,nGen)
    taotaiji_param_all = get_taotaiji_param_all(bird_type,nGen)
    xuanyongrate = get_xuanyongrate(bird_type,nGen)
    date_list = get_date_standard_list()
    rushe_DateList = get_Sum_Rushe_timeList(nGen,bird_type,save_type)

    ## 清空baiyu_weeklyintroducedmedian数据库数据
    # cleanup_weekly_introduced_sum_median(bird_type,nGen)
    cleanup_weeklyintroducedmedian(bird_type,nGen,save_type)

    med_core_data_list = []

    for index in rushe_DateList:
        #根据年份、周度和生存周期，计算所有在生存周期内的数据
        start_year = index['Year']  #2006
        start_week = index['WeekNum']  #2
        rushe_num = index['RuSheNum']  #15000
        dan_tmp_list = []
        param_correct_all = get_correct_param_by_week(index['Year'], index['WeekNum'])
        for iWeek in range(index['LivePeriod']+chandan_interval):
            cur_year,cur_week,start_date,end_date = get_year_week_by_offset_function(date_list, start_year, start_week, iWeek)

            shengchanWeek = iWeek+1
            ##根据起始年和周，算接下来生存周期内的每个周度的年和周，如2006年第1周 三周后是 2006年第4周
            yuchengCunlan = 0
            chandanCunlan = 0
            chandanNum = 0
            chuji_num = 0
            real_sale_chuji_num = 0
            TaoTaiJiNum = 0
            taotai_jirou = 0

            if iWeek == index['LivePeriod']:
                TaoTaiJiNum = rushe_num
            else:
                TaoTaiJiNum = 0

            if iWeek < index['LivePeriod']:
                ### 生产周小于25周为育成期，25周之后进入产蛋期
                if shengchanWeek < 25:  #25需要改成动态获取
                    yuchengCunlan = rushe_num   #15000
                    chandanCunlan = 0
                else:
                    yuchengCunlan = 0
                    chandanCunlan = rushe_num

            ##根据产蛋期存栏数，计算产蛋的数量
            chandanNum = round(chandanCunlan*(param_all[iWeek]['ChanDanRate']/100*7)*(1+param_correct_all['ChanDanC']))
            dan_tmp_list.append(chandanNum)

            '''
            获取三个星期之前的产蛋数量,孵化周期是21天，按照3周计算
            '''
            if shengchanWeek < (25+ chandan_interval):
                dan_init = 0
                shoujing_rate = 0
                rufu_zhongdan_rate = 0
                fuhua_rate = 0

            else:
                dan_init = dan_tmp_list[iWeek-chandan_interval]
                shoujing_rate = (param_all[iWeek-chandan_interval]['ShouJingRate'] / 100)*(1+param_correct_all['ShouJingC'])
                rufu_zhongdan_rate = (param_all[iWeek-chandan_interval]['RuFuZhongDanRate']/100)*(1+param_correct_all['RuFuZhongDanC'])
                fuhua_rate = (param_all[iWeek-chandan_interval]['FuHuaRate']/100)*(1+param_correct_all['FuHuaC'])
            jianchu_rate = (param_all[iWeek]['JianChuRate']/100)*(1+param_correct_all['JianChuC'])
            chuji_num = round(dan_init*shoujing_rate*rufu_zhongdan_rate*fuhua_rate*jianchu_rate*xuanyongrate/100)
            real_sale_chuji_num = chuji_num


            taotai_jirou = TaoTaiJiNum * taotaiji_param_all[index['Year']-1990]['StandardTZ'] * taotaiji_param_all[index['Year']-1990]['TuZaiRate']*1.0/100

            rushe_num = round(rushe_num*(100-param_all[iWeek]['siTaoRate'])/100)
            item = WeeklyIntroducedSumMedian(
                originYear=start_year,
                originWeek=start_week,
                Year=cur_year,
                WeekNum=cur_week,
                startDate=start_date,
                endDate=end_date,
                shengchanWeek=shengchanWeek,
                TotalYuChengCunLan=yuchengCunlan,
                TotalChanDanCunLan=chandanCunlan,
                TotalDan=chandanNum,
                TotalChuJi=chuji_num,
                TotalFactSaleChuJi=real_sale_chuji_num,
                TaoTaiJiNum=TaoTaiJiNum,
                dTaoTaiJiRou=taotai_jirou,
                nBirdsType=bird_type,
                nGeneration=nGen,
                nDraftOrOriginal = save_type,
                Remark=''
            )
            print(item)
            med_core_data_list.append(item)
        WeeklyIntroducedSumMedian.objects.bulk_create(med_core_data_list)
        med_core_data_list = []
    IntroducedInfo.objects.filter(nBirdsType=bird_type,nGeneration=nGen,nDraftOrOriginal=save_type).update(flag = 1)
