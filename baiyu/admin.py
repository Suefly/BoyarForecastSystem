from django.contrib import admin
from baiyu.models import CompanyInfo,SpeciesInfo,FeedWay

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','companyName','Remark')

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id','SpeciesName','BirdType','Generation','Remark')

class FeedWayAdmin(admin.ModelAdmin):
    list_display = ('id','feedWayName','description','remark')
# class ProgenitorIntroducedDetailAdmin(admin.ModelAdmin):
#     list_display = ('id','Year','WeekNum','startDate','endDate','CompanyId','SpeciesId','RuSheNum','LivePeriod','nGeneration','nDraftOrOriginal','nBirdsType','Remark')



admin.site.register(CompanyInfo,CompanyAdmin)
admin.site.register(SpeciesInfo,SpeciesAdmin)
admin.site.register(FeedWay,FeedWayAdmin)
# admin.site.register(ProgenitorIntroducedDetail,ProgenitorIntroducedDetailAdmin)