from baiyu.models import *

def get_weekly_standard_national(nBirdType,nGen):
    '''
    :param:代次，品种
    :return:list
    '''
    ret_list = []
    try:
        ret = WeekStandardTable.objects.values().filter(nBirdsType=nBirdType,nGeneration=nGen)
        for index in ret:
            ret_list.append(index)
    except Exception as e:
        print('get_weekly_standard_national-->',str(e))

    return ret_list


def get_all_param(bird_type,nGeneration):
    res = []
    try:
        db_res = WholeParameter.objects.all().values().filter(nBirdsType=bird_type,nGeneration = nGeneration)
        for index in db_res:
            res.append(index)
    except Exception as e:
        print('Error Reason is :',e)
    return res