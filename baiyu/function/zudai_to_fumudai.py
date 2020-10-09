# from baiyu.db import *
# from baiyu.common import *
#
# def clean_introducd_info(bird_type,nGen):
#     try:
#         res = IntroducedInfo.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen).delete()
#     except Exception as e:
#         print("clean_introducd_info:The Error Reason is:",str(e))
#
#     return
#
# '''
# 将祖代的实际销售雏鸡数，作为父母带的入舍量，插入引种数据库，nGeneration == 2
# '''
# def gen_fumudai_introdeced_data(
#         nGen=2,
#         nDraftOrOriginal=1,
#         nBirdsType=1,
#         Remark=''
#     ):
#     ##  step0: 清除表中原有的父母代入舍所有数据
#     clean_introducd_info(nBirdsType,nGen)
#     ##  step1: 获取父母代引种时间列表
#     time_res = IntroducedInfo.objects.values('Year','WeekNum','LivePeriod').filter(nBirdsType=nBirdsType,nGeneration=nGen-1)
#     ## step2: 按时间列表插入数据
#     for index in time_res:
#         startDate,endDate = get_start_end_date_by_week(index['Year'], index['WeekNum'])
#         rushe_num = get_fumudai_rushe_num(index['Year'], index['WeekNum'], nBirdsType, nGen-1)
#         print(startDate,endDate,rushe_num)
#         insertDB_introduced_sum_info(
#             Year=index['Year'],
#             WeekNum=index['WeekNum'],
#             startDate=startDate,
#             endDate=endDate,
#             RuSheNum=rushe_num,  ##根据祖代鸡的实际销售的雏鸡数量得来
#             LivePeriod=index['LivePeriod'],  ##根据父母代鸡的周标准得来
#             nGeneration = nGen,
#             nDraftOrOriginal = nDraftOrOriginal,
#             nBirdsType = nBirdsType,
#             Remark=Remark
#         )
#
#
#
# def clean_introducd_detail_info(nBirdsType,nGen):
#     try:
#         IntroducedInfo.objects.filter(nBirdsType=nBirdsType,nGeneration=nGen).delete()
#     except Exception as e:
#         print(e)
#
# def get_fumudai_rushe_num(year,week_num,bird_type,nGen):
#
#     RuSheNum = 0
#     try:
#         res = WeeklyCoreTable.objects.values('TotalFactSaleChuJi').filter(Year = year, WeekNum= week_num,nBirdsType=bird_type,nGeneration=nGen)
#         RuSheNum = res[0]['TotalFactSaleChuJi']
#     except Exception as e:
#         print('get_fumudai_rushe_num:The error reason is :',str(e))
#
#     return RuSheNum
#
#
# def  cleanup_weeklyintroducedmedian(bird_type,nGen):
#     try:
#         res = WeeklyIntroducedMedian.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen).delete()
#     except Exception as e:
#         print('The Error Reason is :',str(e))
#
#
#
# def  cleanup_weekly_introduced_sum_median(bird_type,nGen):
#     try:
#         res = WeeklyIntroducedSumMedian.objects.all().filter(nBirdsType=bird_type,nGeneration=nGen).delete()
#     except Exception as e:
#         print('The Error Reason is :',str(e))
#
#
# # def calc_weekly_core(bird_type):
# #     calc_baiyu_weekly_median_core(bird_type,4)
# #     cleanup_weeklycoretable(bird_type)
# #     try:
# #         res = WeekDateStandard.objects.values('Year','WeekNum').filter(Year__gte=2006,Year__lte=2020)
# #     except Exception as e:
# #         res = []
# #         print(e)
# #         return
# #     for index in res:
# #         TotalYuChengCunLan, TotalChanDanCunLan, TotalDan, TotalChuJi, TotalFactSaleChuJi, TaoTaiJiNum, dTaoTaiJiRou = \
# #             get_data_total_from_median(index['Year'],index['WeekNum'])
# #         start_date,end_date = get_start_end_date_by_week(index['Year'],index['WeekNum'])
# #         print(index['Year'],index['WeekNum'],TotalYuChengCunLan,TotalChanDanCunLan,TotalDan,
# #               TotalChuJi,TotalFactSaleChuJi,TaoTaiJiNum,dTaoTaiJiRou)
# #         insertDB_weekly_core_baiyu(
# #             Year=index['Year'],
# #             WeekNum=index['WeekNum'],
# #             startDate = start_date,
# #             endDate = end_date,
# #             TotalYuChengCunLan=TotalYuChengCunLan,
# #             TotalChanDanCunLan=TotalChanDanCunLan,
# #             TotalDan=TotalDan,
# #             TotalChuJi=TotalChuJi,
# #             TotalFactSaleChuJi=TotalFactSaleChuJi,
# #             TaoTaiJiNum=TaoTaiJiNum,
# #             dTaoTaiJiRou=dTaoTaiJiRou,
# #             nBirdsType = bird_type
# #         )
#
#
#
