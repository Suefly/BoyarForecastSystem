"""BoyarData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,re_path
from baiyu import views as baiyu
import login.views as login
urlpatterns = [
    # path('index/',baiyu.index,name='index'),
    path('logout/',login.logout,name='logout'),
    path('show_date_template/',baiyu.index,name='show_date_template'),
    path('zudai_statistics/',baiyu.zudai_statistics,name='zudai_statistics'),
    path('parent_statistics/',baiyu.parent_statistics,name='parent_statistics'),
    path('show_progenitor_introduced/',baiyu.show_progenitor_introduced,name='show_progenitor_introduced'),
    path('shangpin_statistics/',baiyu.shangpin_statistics,name='shangpin_statistics'),
    path('show_zWeekly_standard/',baiyu.show_zWeekly_standard,name='show_zWeekly_standard'),
    path('show_fWeekly_standard/',baiyu.show_fWeekly_standard,name='show_fWeekly_standard'),
    path('show_sDaily_standard/',baiyu.show_sDaily_standard,name='show_sDaily_standard'),
    path('show_sYearly_param/',baiyu.show_sYearly_param,name='show_sYearly_param'),
    path('zudai_all_param/',baiyu.show_zudai_allParam,name='zudai_all_param'),
    path('fmdai_all_param/',baiyu.show_fumudai_allParam,name='fmdai_all_param'),
    path('zdYearly_TtJirou_Param/',baiyu.zdYearly_TtJirou_Param,name='zdYearly_TtJirou_Param'),
    path('fmdYearly_TtJirouParam/',baiyu.fmdYearly_TtJirou_Param,name='fmdYearly_TtJirou_Param'),
    path('add_whole_param/',baiyu.add_whole_param,name='add_whole_param'),
    path('weeklydate_standard/',baiyu.show_weeklydate_standard,name='weeklydate_standard'),
    path('import_origin_introduced/',baiyu.import_origin_introduced,name='import_origin_introduced'),
    path('show_company_info/',baiyu.show_company_info,name='show_company_info'),
    path('show_feedway_info/',baiyu.show_feedway_info,name='show_feedway_info'),
    path('show_species_info/',baiyu.show_species_info,name='show_species_info'),
    path('add_company/',baiyu.add_company,name='add_company'),
    re_path('edit_company/(?P<company_id>\d+)/change/',baiyu.edit_company,name='edit_company'),
    re_path('del_company/(?P<company_id>\d+)/delete/',baiyu.del_company,name='del_company'),
    re_path('add_qzhy/(?P<input_id>\d+)/edit/',baiyu.add_qzhy,name='add_qzhy'),
    path('calc_qzhy/',baiyu.calc_qzhy,name='calc_qzhy'),
    path('add_species/',baiyu.add_species,name='add_species'),
    re_path('edit_species/(?P<species_id>\d+)/change/',baiyu.edit_species,name='edit_species'),
    re_path('del_species/(?P<species_id>\d+)/delete/',baiyu.del_species,name='del_species'),
    path('add_feedway/',baiyu.add_feedway,name='add_feedway'),
    re_path('edit_feedway/(?P<feedway_id>\d+)/change/',baiyu.edit_feedway,name='edit_feedway'),
    re_path('del_feedway/(?P<feedway_id>\d+)/delete/',baiyu.del_feedway,name='del_feedway'),
    path('total_introdeced_data',baiyu.introduced_total_info,name='total_introdeced_data'),
    path('show_total_introduced_info/',baiyu.show_total_introduced_info,name='show_total_introduced_info'),
    re_path('calc_gen (?P<bird_type>\d+) (?P<nGen>\d+) (?P<save_type>\d+)/',baiyu.start_calc_generation,name='calc_gen'),
    path('show_progress/',baiyu.show_progress,name='show_progress'),
    path('show_progress1/',baiyu.show_progress,name='show_progress1'),
    path('process_data/',baiyu.process_data,name='process_data'),
    path('calc_index/',baiyu.show_calc_index,name='calc_index'),
    re_path('calc_sGen/ (?P<bird_type>\d+) (?P<nGen>\d+) (?P<save_type>\d+)/', baiyu.calc_shangpindai_statistics, name='calc_sGen'),
    path('export_excel_zudai/',baiyu.export_excel_zudai,name='export_excel_zudai'),
    path('export_excel_fumudai/',baiyu.export_excel_fumudai,name='export_excel_fumudai'),
    path('export_excel_shangpindai/',baiyu.export_excel_shangpindai,name='export_excel_shangpindai'),
    path('uploadZudaiIntroduced/',baiyu.uploadZudaiIntroduced,name='uploadZudaiIntroduced'),
    path('zdjiaozheng/',baiyu.zdjiaozheng,name='zdjiaozheng'),
    path('zudai_correct_sitaorate/',baiyu.zudai_correct_sitaorate,name='zudai_correct_sitaorate'),
    path('zudai_correct_chandanrate/',baiyu.zudai_correct_chandanrate,name='zudai_correct_chandanrate'),
    path('zudai_correct_rufurate/',baiyu.zudai_correct_rufurate,name='zudai_correct_rufurate'),
    path('zudai_correct_shoujingrate/',baiyu.zudai_correct_shoujingrate,name='zudai_correct_shoujingrate'),
    path('zudai_correct_fuhuarate/',baiyu.zudai_correct_fuhuarate,name='zudai_correct_fuhuarate'),
    path('zudai_correct_jianchurate/',baiyu.zudai_correct_jianchurate,name='zudai_correct_jianchurate'),
    path('zudai_correct_salerate/',baiyu.zudai_correct_salerate,name='zudai_correct_salerate'),
    path('fmdjiaozheng/', baiyu.fmdjiaozheng, name='fmdjiaozheng'),
    path('fmdai_correct_sitaorate/', baiyu.fmdai_correct_sitaorate, name='fmdai_correct_sitaorate'),
    path('fmdai_correct_chandanrate/', baiyu.fmdai_correct_chandanrate, name='fmdai_correct_chandanrate'),
    path('fmdai_correct_rufurate/', baiyu.fmdai_correct_rufurate, name='fmdai_correct_rufurate'),
    path('fmdai_correct_shoujingrate/', baiyu.fmdai_correct_shoujingrate, name='fmdai_correct_shoujingrate'),
    path('fmdai_correct_fuhuarate/', baiyu.fmdai_correct_fuhuarate, name='fmdai_correct_fuhuarate'),
    path('fmdai_correct_jianchurate/', baiyu.fmdai_correct_jianchurate, name='fmdai_correct_jianchurate'),
    path('fmdai_correct_salerate/', baiyu.fmdai_correct_salerate, name='fmdai_correct_salerate'),
    path('tongji_detail/',baiyu.tongji_detail,name='tongji_detail'),
    path('yearly_tongji_detail/',baiyu.yearly_tongji_detail,name='yearly_tongji_detail')
]





