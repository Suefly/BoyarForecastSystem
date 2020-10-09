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
from danji import views as danji
urlpatterns = [
    # path('',danji.index,name='index'),
    # path('show_date_template/',danji.index,name='show_date_template'),
    path('zudai_statistics/',danji.zudai_statistics,name='zudai_statistics_danji'),
    # path('parent_statistics/',danji.parent_statistics,name='parent_statistics'),
    path('detail_introduced/',danji.show_progenitor_introduced,name='show_progenitor_introduced_danji'),
    path('shangpin_statistics/',danji.shangpin_statistics,name='shangpin_statistics_danji'),
    path('zWeekly_standard/',danji.show_zWeekly_standard,name='show_zWeekly_standard_danji'),
    path('fWeekly_standard/',danji.show_fWeekly_standard,name='show_fWeekly_standard_danji'),
    path('sDaily_standard/',danji.show_sDaily_standard,name='show_sDaily_standard_danji'),
    path('sYearly_param/',danji.show_sYearly_param,name='show_sYearly_param_danji'),
    path('zudai_all_param/',danji.show_zudai_allParam,name='zudai_all_param_danji'),
    path('fmdai_all_param/',danji.show_fumudai_allParam,name='fmdai_all_param_danji'),
    path('zdYearly_TtJirou_Param/',danji.zdYearly_TtJirou_Param,name='zdYearly_TtJirou_Param_danji'),
    path('fmdYearly_TtJirouParam/',danji.fmdYearly_TtJirou_Param,name='fmdYearly_TtJirou_Param_danji'),
    path('add_whole_param/',danji.add_whole_param,name='add_whole_param_danji'),
    path('weeklydate_standard/',danji.show_weeklydate_standard,name='weeklydate_standard_danji'),
    # path('import_origin_introduced/',danji.import_origin_introduced,name='import_origin_introduced'),
    # path('show_company_info/',danji.show_company_info,name='show_company_info'),
    # path('show_feedway_info/',danji.show_feedway_info,name='show_feedway_info'),
    # path('show_species_info/',danji.show_species_info,name='show_species_info'),
    # path('add_company/',danji.add_company,name='add_company'),
    # re_path('edit_company/(?P<company_id>\d+)/change/',danji.edit_company,name='edit_company'),
    # re_path('del_company/(?P<company_id>\d+)/delete/',danji.del_company,name='del_company'),
    # re_path('add_qzhy/(?P<input_id>\d+)/edit/',danji.add_qzhy,name='add_qzhy'),
    # path('calc_qzhy/',danji.calc_qzhy,name='calc_qzhy'),
    # path('add_species/',danji.add_species,name='add_species'),
    # re_path('edit_species/(?P<species_id>\d+)/change/',danji.edit_species,name='edit_species'),
    # re_path('del_species/(?P<species_id>\d+)/delete/',danji.del_species,name='del_species'),
    # path('add_feedway/',danji.add_feedway,name='add_feedway'),
    # re_path('edit_feedway/(?P<feedway_id>\d+)/change/',danji.edit_feedway,name='edit_feedway'),
    # re_path('del_feedway/(?P<feedway_id>\d+)/delete/',danji.del_feedway,name='del_feedway'),
    path('total_introdeced_data',danji.introduced_total_info,name='total_introdeced_data_danji'),
    path('total_introduced_info/',danji.show_total_introduced_info,name='show_total_introduced_info_danji')
]





