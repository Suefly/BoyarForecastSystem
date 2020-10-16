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
    path('zudai_statistics/',danji.zudai_statistics,name='zudai_statistics_danji'),
    path('detail_introduced/',danji.show_progenitor_introduced,name='show_progenitor_introduced_danji'),
    path('shangpin_statistics/',danji.shangpin_statistics,name='shangpin_statistics_danji'),
    path('danjiWeeklyStandard/<int:bird_type>/<int:nGen>/',danji.show_weekly_standard_national,name='danjiWeeklyStandard'),
    path('sDaily_standard/',danji.show_sDaily_standard,name='show_sDaily_standard_danji'),
    path('sYearly_param/',danji.show_sYearly_param,name='show_sYearly_param_danji'),
    path('wholeParam/<int:bird_type>/<int:nGen>/',danji.show_danji_whole_param,name='wholeParam'),
    path('fmdai_all_param/',danji.show_fumudai_allParam,name='fmdai_all_param_danji'),
    path('danjiYearTtjirouParam/<int:bird_type>/<int:nGen>/',danji.show_yearly_taotaijirou_param,name='danjiYearTtjirouParam'),
    path('add_whole_param/',danji.add_whole_param,name='add_whole_param_danji'),

]





