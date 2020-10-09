from django.test import TestCase
from baiyu.db import *

# Create your tests here.
def calc_baiyu_weekly_median_core(bird_type,nGen,CompanyId,SpeciesId,feedWayId,chandan_interval=3):
    rushe_DateList = get_Rushe_timeList(nGen,bird_type)

    ## 清空baiyu_weeklyintroducedmedian数据库数据
    cleanup_weeklyintroducedmedian(bird_type,nGen)

    # med_core_data_list = []

    for index in rushe_DateList:
        #根据年份、周度和生存周期，计算所有在生存周期内的数据
        start_year = index['Year']  #2006
        start_week = index['WeekNum']  #2
        rushe_num = index['RuSheNum']  #15000
        shengchan_list = []

        for iWeek in range(index['LivePeriod']+1):
            shengchanWeek = iWeek+1
            param = get_weekly_param_standard(iWeek+1,bird_type,nGen,SpeciesId,feedWayId)
            ##根据起始年和周，算接下来生存周期内的每个周度的年和周，如2006年第1周 三周后是 2006年第4周
            cur_year,cur_week = get_week_info_by_offset(start_year,start_week,iWeek)
            start_date,end_date = get_start_end_date_by_week(cur_year,cur_week)
            yuchengCunlan = 0
            chandanCunlan = 0
            chandanNum = 0
            chuji_num = 0
            real_sale_chuji_num = 0
            TaoTaiJiNum = 0
            taotai_jirou = 0

            if iWeek != index['LivePeriod']:
                ### 生产周小于25周为育成期，25周之后进入产蛋期
                if shengchanWeek < 25:  #25需要改成动态获取
                    yuchengCunlan = rushe_num   #15000
                    chandanCunlan = 0
                else:
                    yuchengCunlan = 0
                    chandanCunlan = rushe_num

                ##根据产蛋期存栏数，计算产蛋的数量
                chandanNum = round(chandanCunlan*param['ChanDanRate']/100*7)

                '''
                获取三个星期之前的产蛋数量,孵化周期是21天，按照3周计算
                '''

            med_data = WeeklyIntroducedMedian(
                            originYear=start_year,
                            originWeek=start_week,
                            Year=cur_year,
                            WeekNum=cur_week,
                            startDate=start_date,
                            endDate=end_date,
                            CompanyId=CompanyId,
                            SpeciesId=SpeciesId,
                            feedWayId=feedWayId,
                            shengchanWeek=shengchanWeek,
                            TotalYuChengCunLan=yuchengCunlan,
                            TotalChanDanCunLan=chandanCunlan,
                            TotalDan=chandanNum,
                        )
            shengchan_list.append(med_data)
            rushe_num = round(rushe_num*(100-param['siTaoRate'])/100)
        WeeklyIntroducedMedian.objects.bulk_create(shengchan_list)


