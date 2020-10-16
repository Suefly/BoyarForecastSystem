from django.shortcuts import render

# Create your views here.

from baiyu.views import *

def index(request):
    return render(request,'index_danji.html')


'''
#渲染接口，展示祖代引种周度标准参数
#by sujie 2019/05/27
'''
def show_zWeekly_standard(request):
    bird_type = 3   #白羽肉鸭
    nGen = 1  #祖代
    content = {
        'zhudai_weekly_standard':get_weekly_standard(bird_type,nGen)
    }
    return render(request,'danji_zWeeklyStandard.html',content)



'''
#渲染接口，展示祖代引种入舍总量
#by sujie 2019/05/27
'''
def show_progenitor_introduced(request):
    bird_type = 3  # 白羽肉鸭
    nGen = 1  # 祖代
    content = {
        'introduced_info':get_introduced_detail_info(bird_type,nGen),
        'count':get_count_ProgenitorIntroduced(bird_type,nGen)
    }
    return render(request,'danji_introduced.html',content)


def zudai_statistics(request):

    content  ={
        "zudai_statistic":get_zudai_statistic()
    }
    return render(request,'danji_zudai_statistics.html',content)


def parent_statistics(request):
    return render(request,'danji_parent_statistics.html')

def shangpin_statistics(request):
    content = {
        'shangpin_statistics':get_sWeekly_statistic()
    }
    return render(request,'danji_shangpin_statistics.html',content)

###################################################################
## written by sujie@boyar.cn   2019-05-27
##  Below is the standard paramter of calculate
###################################################################

'''
#渲染接口，展示父母代周度标准参数
#by sujie 2019/05/27
'''
def show_fWeekly_standard(request):
    bird_type = 3
    nGen = 2
    content = {
        'fumudai_weekly_standard':get_weekly_standard(bird_type,nGen)
    }
    return render(request,'danji_fWeeklyStandard.html',content)


'''
#渲染接口，展示商品代日度标准参数
#by sujie 2019/05/27
'''
def show_sDaily_standard(request):
    bird_type = 3
    content = {
        'shangpindai_daily_standard':get_shangpindai_daily_standard(bird_type)
    }
    return render(request,'danji_sDailyStandard.html',content)

'''
#渲染接口，展示商品代年度参数
#by sujie 2019/05/27
'''
def show_sYearly_param(request):
    content = {
        'shangpindai_yearly_param':get_shangpindai_yearly_param()
    }
    return render(request,'danji_sYearlyParam.html',content)


'''
#渲染接口，展示祖代总参数
#by sujie 2019/05/27
'''
def show_zudai_allParam(request):
    bird_type = 3
    nGen = 1
    content = {
        'zudai_whole_param':get_all_param(bird_type,nGen) #1为祖代，2为父母代
    }
    return render(request,'danji_show_zd_allParam.html',content)

'''
#渲染接口，展示父母代总参数
#by sujie 2019/05/30
'''
def show_fumudai_allParam(request):
    bird_type = 3
    nGen = 2
    content = {
        'fmdai_whole_param':get_all_param(bird_type,nGen) #1为祖代，2为父母代
    }
    return render(request,'danji_show_fmdai_allParam.html',content)


'''
#渲染接口，展示祖代年淘汰鸡肉参数
#by sujie 2019/05/27
'''
def zdYearly_TtJirou_Param(request):
    bird_type = 3
    nGen = 1
    content = {
        'zudai_tcjirou_param':get_tcjirou_param(bird_type,nGen) #1为祖代，2为父母代
    }
    return render(request,'danji_zdYearly_TtJirouParam.html',content)

'''
#渲染接口，展示父母代年淘汰鸡肉参数
#by sujie 2019/05/27
'''
def fmdYearly_TtJirou_Param(request):
    bird_type = 3
    nGen = 2
    content = {
        'fmdai_tcjirou_param':get_tcjirou_param(bird_type,nGen) #1为祖代，2为父母代
    }
    return render(request,'danji_fmdYearly_TtJirouParam.html',content)


def add_whole_param(request):
    return render(request,'danji_add_whole_param.html')



