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
from rouya import views as rouya
urlpatterns = [
    # path('',rouya.index,name='index'),
    # path('show_date_template/',rouya.index,name='show_date_template'),
    path('zudai_statistics/',rouya.zudai_statistics,name='zudai_statistics_rouya'),
    # path('parent_statistics/',rouya.parent_statistics,name='parent_statistics'),
    path('detail_introduced/',rouya.show_progenitor_introduced,name='show_progenitor_introduced_rouya'),
    path('shangpin_statistics/',rouya.shangpin_statistics,name='shangpin_statistics_rouya'),
    path('zWeekly_standard/',rouya.show_zWeekly_standard,name='show_zWeekly_standard_rouya'),
    path('fWeekly_standard/',rouya.show_fWeekly_standard,name='show_fWeekly_standard_rouya'),
    path('sDaily_standard/',rouya.show_sDaily_standard,name='show_sDaily_standard_rouya'),
    path('sYearly_param/',rouya.show_sYearly_param,name='show_sYearly_param_rouya'),
    path('zudai_all_param/',rouya.show_zudai_allParam,name='zudai_all_param_rouya'),
    path('fmdai_all_param/',rouya.show_fumudai_allParam,name='fmdai_all_param_rouya'),
    path('zdYearly_TtJirou_Param/',rouya.zdYearly_TtJirou_Param,name='zdYearly_TtJirou_Param_rouya'),
    path('fmdYearly_TtJirouParam/',rouya.fmdYearly_TtJirou_Param,name='fmdYearly_TtJirou_Param_rouya'),
    path('add_whole_param/',rouya.add_whole_param,name='add_whole_param_rouya'),
    path('weeklydate_standard/',rouya.show_weeklydate_standard,name='weeklydate_standard_rouya'),
    # path('import_origin_introduced/',rouya.import_origin_introduced,name='import_origin_introduced'),
    # path('show_company_info/',rouya.show_company_info,name='show_company_info'),
    # path('show_feedway_info/',rouya.show_feedway_info,name='show_feedway_info'),
    # path('show_species_info/',rouya.show_species_info,name='show_species_info'),
    # path('add_company/',rouya.add_company,name='add_company'),
    # re_path('edit_company/(?P<company_id>\d+)/change/',rouya.edit_company,name='edit_company'),
    # re_path('del_company/(?P<company_id>\d+)/delete/',rouya.del_company,name='del_company'),
    # re_path('add_qzhy/(?P<input_id>\d+)/edit/',rouya.add_qzhy,name='add_qzhy'),
    # path('calc_qzhy/',rouya.calc_qzhy,name='calc_qzhy'),
    # path('add_species/',rouya.add_species,name='add_species'),
    # re_path('edit_species/(?P<species_id>\d+)/change/',rouya.edit_species,name='edit_species'),
    # re_path('del_species/(?P<species_id>\d+)/delete/',rouya.del_species,name='del_species'),
    # path('add_feedway/',rouya.add_feedway,name='add_feedway'),
    # re_path('edit_feedway/(?P<feedway_id>\d+)/change/',rouya.edit_feedway,name='edit_feedway'),
    # re_path('del_feedway/(?P<feedway_id>\d+)/delete/',rouya.del_feedway,name='del_feedway'),
    path('total_introdeced_data',rouya.introduced_total_info,name='total_introdeced_data_rouya'),
    path('total_introduced_info/',rouya.show_total_introduced_info,name='show_total_introduced_info_rouya')
]





