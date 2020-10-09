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
from huangji import views as huangji
urlpatterns = [
    # path('',huangji.index,name='index'),
    # path('show_date_template/',huangji.index,name='show_date_template'),
    path('zudai_statistics/',huangji.zudai_statistics,name='zudai_statistics_huangji'),
    # path('parent_statistics/',huangji.parent_statistics,name='parent_statistics'),
    path('detail_introduced/',huangji.show_progenitor_introduced,name='show_progenitor_introduced_huangji'),
    path('shangpin_statistics/',huangji.shangpin_statistics,name='shangpin_statistics_huangji'),
    path('zWeekly_standard/',huangji.show_zWeekly_standard,name='show_zWeekly_standard_huangji'),
    path('fWeekly_standard/',huangji.show_fWeekly_standard,name='show_fWeekly_standard_huangji'),
    path('sDaily_standard/',huangji.show_sDaily_standard,name='show_sDaily_standard_huangji'),
    path('sYearly_param/',huangji.show_sYearly_param,name='show_sYearly_param_huangji'),
    path('zudai_all_param/',huangji.show_zudai_allParam,name='zudai_all_param_huangji'),
    path('fmdai_all_param/',huangji.show_fumudai_allParam,name='fmdai_all_param_huangji'),
    path('zdYearly_TtJirou_Param/',huangji.zdYearly_TtJirou_Param,name='zdYearly_TtJirou_Param_huangji'),
    path('fmdYearly_TtJirouParam/',huangji.fmdYearly_TtJirou_Param,name='fmdYearly_TtJirou_Param_huangji'),
    path('add_whole_param/',huangji.add_whole_param,name='add_whole_param_huangji'),
    path('weeklydate_standard/',huangji.show_weeklydate_standard,name='weeklydate_standard_huangji'),
    # path('import_origin_introduced/',huangji.import_origin_introduced,name='import_origin_introduced'),
    # path('show_company_info/',huangji.show_company_info,name='show_company_info'),
    # path('show_feedway_info/',huangji.show_feedway_info,name='show_feedway_info'),
    # path('show_species_info/',huangji.show_species_info,name='show_species_info'),
    # path('add_company/',huangji.add_company,name='add_company'),
    # re_path('edit_company/(?P<company_id>\d+)/change/',huangji.edit_company,name='edit_company'),
    # re_path('del_company/(?P<company_id>\d+)/delete/',huangji.del_company,name='del_company'),
    # re_path('add_qzhy/(?P<input_id>\d+)/edit/',huangji.add_qzhy,name='add_qzhy'),
    # path('calc_qzhy/',huangji.calc_qzhy,name='calc_qzhy'),
    # path('add_species/',huangji.add_species,name='add_species'),
    # re_path('edit_species/(?P<species_id>\d+)/change/',huangji.edit_species,name='edit_species'),
    # re_path('del_species/(?P<species_id>\d+)/delete/',huangji.del_species,name='del_species'),
    # path('add_feedway/',huangji.add_feedway,name='add_feedway'),
    # re_path('edit_feedway/(?P<feedway_id>\d+)/change/',huangji.edit_feedway,name='edit_feedway'),
    # re_path('del_feedway/(?P<feedway_id>\d+)/delete/',huangji.del_feedway,name='del_feedway'),
    path('total_introdeced_data',huangji.introduced_total_info,name='total_introdeced_data_huangji'),
    path('total_introduced_info/',huangji.show_total_introduced_info,name='show_total_introduced_info_huangji')
]





