from baiyu.db import *
from baiyu.common import *


def calc_taotaiji_num_jirou(bird_type,nGen,SpeciesId,feedWayId):
    date_list = get_shangpindai_date(bird_type,nGen,SpeciesId,feedWayId)
    for index in date_list:
        shangpinji_num = get_shangpinji_num(index['Year'],index['WeekNum'],bird_type,nGen,SpeciesId,feedWayId)
        startDate, endDate = get_start_end_date_by_week(index['Year'],index['WeekNum'])
        param = get_shangpin_year_param(index['Year'])
        # day35_year,day35_week = get_week_info_by_offset(index['Year'],index['WeekNum'],5)
        # startDate35, endDate35 = get_start_end_date_by_week(day35_year,day35_week)
        # after_sitao_35 =calc_sitao_rate(bird_type,35)
        # chulan_35 = shangpinji_num*after_sitao_35
        # jirou_35 = chulan_35*param['TuZaiRate35']*param['ChulanQZ35']*param['ChuLanTZ35']
        # insertDB_weekly_core_baiyu(
        #     Year=day35_year,
        #     WeekNum=day35_week,
        #     startDate=startDate35,
        #     endDate=endDate35,
        #     TaoTaiJiNum=chulan_35,
        #     dTaoTaiJiRou=jirou_35,
        #     nBirdsType=bird_type,
        #     nGeneration=nGen
        # )

        day42_year, day42_week = get_week_info_by_offset(index['Year'], index['WeekNum'], 6)
        startDate42, endDate42 = get_start_end_date_by_week(day42_year, day42_week)
        after_sitao_42 = calc_sitao_rate(bird_type, 42)
        # chulan_42 = shangpinji_num * after_sitao_42* param['ChulanQZ42']
        # jirou_42 = chulan_42 * param['TuZaiRate42']  * param['ChuLanTZ42']
        chulan_42 = shangpinji_num * after_sitao_42
        jirou_42 = chulan_42 * param['TuZaiRate42']*1.0/100 * param['ChuLanTZ42']
        insertDB_weekly_core_baiyu(
            Year=day42_year,
            WeekNum=day42_week,
            startDate=startDate42,
            endDate=endDate42,
            TaoTaiJiNum=chulan_42,
            dTaoTaiJiRou=jirou_42,
            nBirdsType=bird_type,
            nGeneration=nGen
        )

        # day49_year, day49_week = get_week_info_by_offset(index['Year'], index['WeekNum'], 7)
        # startDate49, endDate49 = get_start_end_date_by_week(day49_year, day49_week)
        # after_sitao_49 = calc_sitao_rate(bird_type, 49)
        # chulan_49 = shangpinji_num * after_sitao_49 * param['ChulanQZ49']
        # jirou_49 = chulan_49 * param['TuZaiRate49'] * param['ChuLanTZ49']
        # insertDB_weekly_core_baiyu(
        #     Year=day49_year,
        #     WeekNum=day49_week,
        #     startDate=startDate49,
        #     endDate=endDate49,
        #     TaoTaiJiNum=chulan_49,
        #     dTaoTaiJiRou=jirou_49,
        #     nBirdsType=bird_type,
        #     nGeneration=nGen
        # )
        #
        # day56_year, day56_week = get_week_info_by_offset(index['Year'], index['WeekNum'], 8)
        # startDate56, endDate56 = get_start_end_date_by_week(day56_year, day56_week)
        # after_sitao_56 = calc_sitao_rate(bird_type, 56)
        # chulan_56 = shangpinji_num * after_sitao_56*param['ChulanQZ56']
        # jirou_56 = chulan_56 * param['TuZaiRate56'] * param['ChuLanTZ56']
        # insertDB_weekly_core_baiyu(
        #     Year=day56_year,
        #     WeekNum=day56_week,
        #     startDate=startDate56,
        #     endDate=endDate56,
        #     TaoTaiJiNum=chulan_56,
        #     dTaoTaiJiRou=jirou_56,
        #     nBirdsType=bird_type,
        #     nGeneration=nGen
        # )

        # total_rouji = chulan_35 + chulan_42 + chulan_49 + chulan_56
        total_rouji = chulan_42
        insertDB_weekly_detail_statistics(
            Year = index['Year'],
            WeekNum = index['WeekNum'],
            startDate = startDate,
            endDate = endDate,
            CunlLanNum35 = 0,
            CunlLanNum42 = chulan_42,
            CunlLanNum49 = 0,
            CunlLanNum56 = 0,
            ChuLanRouJiNum35= 0,
            ChuLanRouJiNum42= jirou_42,
            ChuLanRouJiNum49= 0,
            ChuLanRouJiNum56= 0,
            TotalChuLanRouJiNum= total_rouji,

        )


def Delete_db_shangpin_detail_statistics(bird_type,save_type):
    try:
        res = WeeklyStatisticDetail.objects.all().filter(nBirdsType=bird_type,nDraftOrOriginal=save_type).delete()
    except Exception as e:
        print("insertDB_median_baiyu:The Error Reason is :", e)
    return

def Delete_db_shangpin_sum_statistics(bird_type,save_type):
    try:
        res = WeeklyStatisticDetail.objects.all().filter(nBirdsType=bird_type,nDraftOrOriginal=save_type).delete()
    except Exception as e:
        print("insertDB_median_baiyu:The Error Reason is :", e)
    return



def calc_shangpinji_detail_statistics(bird_type,nGen,save_type):
    # save_type = 1
    Delete_db_shangpin_sum_statistics(bird_type,save_type)
    # rushe_num = 305
    # setp 1: 获取商品代引种的时间列表
    ### 商品代的引种时间，由父母代产生的一日龄雏鸡产生
    date_list = get_shangpindai_introduced_date(bird_type,nGen)
    date_standard_list = get_date_standard_list()
    # sitao_rate_list = [calc_sitao_rate(1,35),calc_sitao_rate(1,42),calc_sitao_rate(1,49),calc_sitao_rate(1,56)]

    ##根据日度的死淘率，计算周度的死淘率
    sitao_rate_35 = calc_sitao_rate(1,35)
    sitao_rate_42 = calc_sitao_rate(1, 42)
    sitao_rate_49 = calc_sitao_rate(1, 49)
    sitao_rate_56 = calc_sitao_rate(1, 56)

    year_param = get_shangpin_year_param_all()
    # step 2:
    for index,elem in enumerate(date_list):
        year, week_num, startDate, endDate = get_year_week_by_offset_function(date_standard_list, elem['Year'], elem['WeekNum'], 0 )
        param = year_param[year-1990]
        rushe_num = elem['RuSheNum']
        for period in range(9):
            year_cur, week_num_cur, startDate, endDate = get_year_week_by_offset_function(date_standard_list, year,week_num, period)
            if period < 5:
                insertDB_weekly_detail_statistics(
                    Year=year_cur,
                    WeekNum=week_num_cur,
                    startDate=startDate,
                    endDate=endDate
                )
            elif period == 5:
                cunlan35 = round(rushe_num * sitao_rate_35 / 100)
                chulan35 = round(rushe_num * (sitao_rate_35 / 100) * (param['ChulanQZ35'] / 100))
                dHuoZhong35 = chulan35 * param['ChuLanTZ35']  ##单位转换成吨
                JiRou35 = dHuoZhong35 * (param['TuZaiRate35'] / 100)
                JiXiong35 = dHuoZhong35 * (param['JiXiongRate35'] / 100)
                JiChi35 = dHuoZhong35 * (param['JiChiRate35'] / 100)
                JiTui35 = dHuoZhong35 * (param['JiTuiRate35'] / 100)
                JiGuJia35 = dHuoZhong35 * (param['JiGuJiaRate35'] / 100)
                JiNeiZang35 = dHuoZhong35 * (param['JiNeiZangRate35'] / 100)
                insertDB_weekly_detail_statistics(
                    Year=year_cur,
                    WeekNum=week_num_cur,
                    startDate=startDate,
                    endDate=endDate,
                    CunlLanNum35=cunlan35,
                    ChuLanRouJiNum35=chulan35,
                    HuoZhong35=dHuoZhong35,
                    JiRou35=JiRou35,
                    JiXiong35=JiXiong35,
                    JiChi35=JiChi35,
                    JiTui35=JiTui35,
                    JiGuJia35=JiGuJia35,
                    JiNeiZang35=JiNeiZang35
                )
            elif period == 6:
                cunlan42 = round(rushe_num * sitao_rate_42 / 100)
                chulan42 = round(rushe_num * (sitao_rate_42 / 100) * (param['ChulanQZ42'] / 100))
                dHuoZhong42 = chulan42 * param['ChuLanTZ42']  ##单位转换成吨
                JiRou42 = dHuoZhong42 * (param['TuZaiRate42'] / 100)
                JiXiong42 = dHuoZhong42 * (param['JiXiongRate42'] / 100)
                JiChi42 = dHuoZhong42 * (param['JiChiRate42'] / 100)
                JiTui42 = dHuoZhong42 * (param['JiTuiRate42'] / 100)
                JiGuJia42 = dHuoZhong42 * (param['JiGuJiaRate42'] / 100)
                JiNeiZang42 = dHuoZhong42 * (param['JiNeiZangRate42'] / 100)
                insertDB_weekly_detail_statistics(
                    Year=year_cur,
                    WeekNum=week_num_cur,
                    startDate=startDate,
                    endDate=endDate,
                    CunlLanNum42=cunlan42,
                    ChuLanRouJiNum42=chulan42,
                    HuoZhong42=dHuoZhong42,
                    JiRou42=JiRou42,
                    JiXiong42=JiXiong42,
                    JiChi42=JiChi42,
                    JiTui42=JiTui42,
                    JiGuJia42=JiGuJia42,
                    JiNeiZang42=JiNeiZang42
                )
            elif period == 7:
                cunlan49 = round(rushe_num * sitao_rate_49 / 100)
                chulan49 = round(rushe_num * (sitao_rate_49 / 100) * (param['ChulanQZ49'] / 100))
                dHuoZhong49 = chulan49 * param['ChuLanTZ49']  ##单位转换成吨
                JiRou49 = dHuoZhong49 * (param['TuZaiRate49'] / 100)
                JiXiong49 = dHuoZhong49 * (param['JiXiongRate49'] / 100)
                JiChi49 = dHuoZhong49 * (param['JiChiRate49'] / 100)
                JiTui49 = dHuoZhong49 * (param['JiTuiRate49'] / 100)
                JiGuJia49 = dHuoZhong49 * (param['JiGuJiaRate49'] / 100)
                JiNeiZang49 = dHuoZhong49 * (param['JiNeiZangRate49'] / 100)
                insertDB_weekly_detail_statistics(
                    Year=year_cur,
                    WeekNum=week_num_cur,
                    startDate=startDate,
                    endDate=endDate,
                    CunlLanNum49=cunlan49,
                    ChuLanRouJiNum49=chulan49,
                    HuoZhong49=dHuoZhong49,
                    JiRou49=JiRou49,
                    JiXiong49=JiXiong49,
                    JiChi49=JiChi49,
                    JiTui49=JiTui49,
                    JiGuJia49=JiGuJia49,
                    JiNeiZang49=JiNeiZang49
                )
            elif period == 8:
                cunlan56 = round(rushe_num * sitao_rate_56 / 100)
                chulan56 = round(rushe_num * (sitao_rate_56 / 100) * (param['ChulanQZ56'] / 100))
                dHuoZhong56 = chulan56 * param['ChuLanTZ56']  ##单位转换成吨
                JiRou56 = dHuoZhong56 * (param['TuZaiRate56'] / 100)
                JiXiong56 = dHuoZhong56 * (param['JiXiongRate56'] / 100)
                JiChi56 = dHuoZhong56 * (param['JiChiRate56'] / 100)
                JiTui56 = dHuoZhong56 * (param['JiTuiRate56'] / 100)
                JiGuJia56 = dHuoZhong56 * (param['JiGuJiaRate56'] / 100)
                JiNeiZang56 = dHuoZhong56 * (param['JiNeiZangRate56'] / 100)
                insertDB_weekly_detail_statistics(
                    Year=year_cur,
                    WeekNum=week_num_cur,
                    startDate=startDate,
                    endDate=endDate,
                    CunlLanNum56=cunlan56,
                    ChuLanRouJiNum56=chulan56,
                    HuoZhong56=dHuoZhong56,
                    JiRou56=JiRou56,
                    JiXiong56=JiXiong56,
                    JiChi56=JiChi56,
                    JiTui56=JiTui56,
                    JiGuJia56=JiGuJia56,
                    JiNeiZang56=JiNeiZang56
                )



def get_date_standard_list():
    try:
        res = WeekDateStandard.objects.all().values('id', 'Year', 'WeekNum','startDate','endDate').filter(Year__gt=2000)
    except Exception as e:
        print(e)

    return res

def get_shangpin_year_param_all():
    result = []
    try:
        result = YearParameter.objects.all().values().order_by('id')
    except Exception as e:
        print(str(e))
    return result


def get_shangpindai_introduced_date(bird_type,nGen):

    date_list = []
    try:
        date_list = IntroducedInfo.objects.all().values('Year','WeekNum','RuSheNum').filter(nBirdsType=bird_type,nGeneration=nGen,RuSheNum__gt=0)
    except Exception as e:
        print(str(e))
    return date_list


def get_shangpindai_date(bird_type,nGen):

    date_list = []
    res = IntroducedInfo.objects.all().values('Year','WeekNum','RuSheNum').filter(nBirdsType=bird_type,
                                                                             nGeneration=nGen,
                                                                             RuSheNum__gt=0)
    for index in res:
        date_list.append(index)
    return date_list

def get_shangpinji_num(year,week_num,bird_type,nGen,SpeciesId,feedWayId):
    num = 0
    try:
        res = IntroducedInfoDetail.objects.values('RuSheNum').filter(
                                                                     Year= year,
                                                                     WeekNum= week_num,
                                                                     nBirdsType=bird_type,
                                                                     nGeneration=nGen,
                                                                     SpeciesId = SpeciesId,
                                                                     feedWayId = feedWayId)
    except Exception as e:
        print('e')
    num = res[0]['RuSheNum']

    return num


def get_shangpin_year_param(year):
    param = {}
    try:
        res = YearParameter.objects.values().filter(nYear=year)
        param = res[0]
    except Exception as e:
        print(e)
    return param


def calc_sitao_rate(bird_type,day_num):
    '''
    根据日度的死淘率，计算周度的死淘率
    :param bird_type:
    :param day_num:日度
    :return:
    '''
    leiji_sitaorate = 1
    try:
        res = DailyStandardTable.objects.values('id','nDay','SiTaoRate').filter(nBirdsType=bird_type).order_by('nDay')[:day_num]

        for index in res:
            leiji_sitaorate *= ((100-index['SiTaoRate'])*1.0/100)
    except Exception as e:
        print(e)
    return round(leiji_sitaorate*100,2)


def get_total_jirou(year,week_num,bird_type,nGen):
    res_dict = {
        "TotalYuChengCunLan":0,
        "TotalChanDanCunLan":0,
        "TotalDan":0,
        "TotalChuJi":0,
        "TotalFactSaleChuJi":0,
        "TaoTaiJiNum":0,
        "dTaoTaiJiRou":0
    }
    TotalYuChengCunLan = 0
    TotalChanDanCunLan = 0
    TotalDan = 0
    TotalChuJi = 0
    TotalFactSaleChuJi = 0
    TaoTaiJiNum = 0
    dTaoTaiJiRou = 0
    try:
        res = WeeklyIntroducedSumMedian.objects.values().filter(Year=year,
                                                             WeekNum=week_num,
                                                             nBirdsType=bird_type,
                                                             nGeneration=nGen)
        for index in res:
            res_dict["TotalYuChengCunLan"] += index['TotalYuChengCunLan']
            res_dict["TotalChanDanCunLan"] += index['TotalChanDanCunLan']
            res_dict["TotalDan"] += index['TotalDan']
            res_dict["TotalChuJi"] += index['TotalChuJi']
            res_dict["TotalFactSaleChuJi"] += index['TotalFactSaleChuJi']
            res_dict["TaoTaiJiNum"] += index['TaoTaiJiNum']
            res_dict["dTaoTaiJiRou"] +=  index['dTaoTaiJiRou']
    except Exception as e:
        print('get_data_total_from_median:The Error Reason is :',e)

    return res_dict

def get_shangpindai_detail_info(bird_type,save_type):
    result = []
    with OpenDB() as cursor:
        sql = '''
            SELECT
                Year,
                WeekNum,
                SUM(CunlLanNum35),
                SUM(CunlLanNum42),
                SUM(CunlLanNum49),
                SUM(CunlLanNum56),
                SUM(ChuLanRouJiNum35),
                SUM(ChuLanRouJiNum42),
                SUM(ChuLanRouJiNum49),
                SUM(ChuLanRouJiNum56),
                SUM(TotalChuLanRouJiNum),
                SUM(HuoZhong35),
                SUM(HuoZhong42),
                SUM(HuoZhong49),
                SUM(HuoZhong56),
                SUM(TotalHuoZhong),
                SUM(JiRou35),
                SUM(JiRou42),
                SUM(JiRou49),
                SUM(JiRou56),
                SUM(TotalJiRou),
                SUM(JiXiong35),
                SUM(JiXiong42),
                SUM(JiXiong49),
                SUM(JiXiong56),
                SUM(TotalJiXiong),
                SUM(JiChi35),
                SUM(JiChi42),
                SUM(JiChi49),
                SUM(JiChi56),
                SUM(TotalJiChi),
                SUM(JiTui35),
                SUM(JiTui42),
                SUM(JiTui49),
                SUM(JiTui56),
                SUM(TotalJiTui),
                SUM(JiGuJia35),
                SUM(JiGuJia42),
                SUM(JiGuJia49),
                SUM(JiGuJia56),
                SUM(TotalJiGuJia),
                SUM(JiNeiZang35),
                SUM(JiNeiZang42),
                SUM(JiNeiZang49),
                SUM(JiNeiZang56),
                SUM(TotalJiNeiZang)
            FROM
                baiyu_weeklystatisticdetail
            WHERE
	            nBirdsType = %d AND nDraftOrOriginal = %d	            
            GROUP BY
                Year,WeekNum
        ''' % (int(bird_type),int(save_type))
        try:
            cursor.execute(sql)
            db_res = cursor.fetchall()
            for i in db_res:
                result.append(i)
        except Exception as e:
            print('Error Reason is :',e)
        print('result',result)
        return result


## result_list传入类型为list
def gen_shangpindai_data_format(input_list):
    result_list = []
    print('result_list',input_list)
    for ituple in input_list:
        print('ituple',ituple)
        index = list(ituple)
        print('index',index)
        index[10] = index[6] + index[7] + index[8] + index[9]
        print('###')
        index[15] = index[11] + index[12] + index[13] + index[14]
        index[20] = index[16] + index[17] + index[18] + index[19]
        index[25] = index[21] + index[22] + index[23] + index[24]
        index[30] = index[26] + index[27] + index[28] + index[29]
        index[35] = index[31] + index[32] + index[33] + index[34]
        index[40] = index[36] + index[37] + index[38] + index[39]
        index[45] = index[41] + index[42] + index[43] + index[44]
        print(index)
        result_list.append(index)
    print('result',result_list)
    return result_list



def Delete_db_shangpin_statistics(bird_type):
    try:
        res = WeeklyStatisticTable.objects.all().filter(nBirdsType=bird_type).delete()
    except Exception as e:
        print("insertDB_median_baiyu:The Error Reason is :", e)
    return


def Delete_db_shangpin_statistics_sum(bird_type,save_type):
    try:
        res = WeeklyStatisticTable.objects.all().filter(nBirdsType=bird_type,nDraftOrOriginal=save_type).delete()
    except Exception as e:
        print("insertDB_median_baiyu:The Error Reason is :", e)
    return

def insert_to_shangpindai_statisctis(input_list,bird_type,save_type):
    Delete_db_shangpin_statistics_sum(bird_type,save_type)
    item_list = []
    for index in input_list:
        start_date , end_date = get_start_end_date_by_week(index[0],index[1])
        item = WeeklyStatisticTable(
            Year=index[0],
            WeekNum=index[1],
            startDate= start_date,
            endDate= end_date,
            CunlLanNum35=index[2],
            CunlLanNum42=index[3],
            CunlLanNum49=index[4],
            CunlLanNum56=index[5],
            ChuLanRouJiNum35=index[6],
            ChuLanRouJiNum42=index[7],
            ChuLanRouJiNum49=index[8],
            ChuLanRouJiNum56=index[9],
            TotalChuLanRouJiNum=index[10],
            HuoZhong35=index[11],
            HuoZhong42=index[12],
            HuoZhong49=index[13],
            HuoZhong56=index[14],
            TotalHuoZhong=index[15],
            JiRou35=index[16],
            JiRou42=index[17],
            JiRou49 = index[18],
            JiRou56=index[19],
            TotalJiRou=index[20],
            JiXiong35=index[21],
            JiXiong42=index[22],
            JiXiong49=index[23],
            JiXiong56=index[24],
            TotalJiXiong=index[25],
            JiChi35=index[26],
            JiChi42=index[27],
            JiChi49=index[28],
            JiChi56=index[29],
            TotalJiChi=index[30],
            JiTui35=index[31],
            JiTui42=index[32],
            JiTui49=index[33],
            JiTui56=index[34],
            TotalJiTui=index[35],
            JiGuJia35=index[36],
            JiGuJia42=index[37],
            JiGuJia49=index[38],
            JiGuJia56=index[39],
            TotalJiGuJia=index[40],
            JiNeiZang35=index[41],
            JiNeiZang42=index[42],
            JiNeiZang49=index[43],
            JiNeiZang56=index[44],
            TotalJiNeiZang=index[45],
            nDraftOrOriginal=1,
            nBirdsType=bird_type,
            Remark='success'
        )
        item_list.append(item)
    WeeklyStatisticTable.objects.bulk_create(item_list)




def calc_shangpin_data(bird_type,nGen,save_type):

    calc_shangpinji_detail_statistics(bird_type,nGen,save_type)
    detail_result_list = get_shangpindai_detail_info(bird_type,save_type)
    result_list = gen_shangpindai_data_format(detail_result_list)
    insert_to_shangpindai_statisctis(result_list,bird_type,save_type)




