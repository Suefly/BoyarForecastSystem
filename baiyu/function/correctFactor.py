from baiyu.models import *

def get_date_list():
    date_list = []
    try:
        date_list = WeekDateStandard.objects.all().values()
    except Exception as e:
        print('e')

    return date_list


def insert_to_correct(date_list):

    correct_list = []
    for index in date_list:
        item = WeekCorrectionFactor(
            Year = index['Year'],
            WeekNum = index['WeekNum'],
            startDate = index['startDate'],
            endDate = index['endDate'],
            SiTaoC = 0,
            SiTaoCNote = '',
            ChanDanC = 0,
            ChanDanCNote = '',
            RuFuZhongDanC = 0,
            RuFuZhongDanCNote = '',
            ShouJingC = 0,
            ShouJingCNote = '',
            FuHuaC = 0,
            FuHuaCNote = '',
            JianChuC = 0,
            JianChuCNote = '',
            SaleRateC = 0,
            SaleRateCNote = '',
            nGeneration = 2,
            nBirdsType = 1,
            Remark = ''
        )
        correct_list.append(item)
    WeekCorrectionFactor.objects.bulk_create(correct_list)

if __name__ == '__main__':
    date_list = get_date_list()
    print("#"*20)
    insert_to_correct(date_list)