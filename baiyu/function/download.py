import xlwt
from io import BytesIO
from django.shortcuts import HttpResponse
from baiyu.models import *

# # 导出excel数据
# def export_excel():
#     # 设置HTTPResponse的类型
#     response = HttpResponse(content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment;filename=order.xls'
#     # 创建一个文件对象
#     wb = xlwt.Workbook(encoding='utf8')
#     # 创建一个sheet对象
#     sheet = wb.add_sheet('order-sheet')
#
#     # 设置文件头的样式,这个不是必须的可以根据自己的需求进行更改
#     style_heading = xlwt.easyxf("""
#             font:
#                 name Arial,
#                 colour_index white,
#                 bold on,
#                 height 0xA0;
#             align:
#                 wrap off,
#                 vert center,
#                 horiz center;
#             pattern:
#                 pattern solid,
#                 fore-colour 0x19;
#             borders:
#                 left THIN,
#                 right THIN,
#                 top THIN,
#                 bottom THIN;
#             """)
#
#     # 写入文件标题
#     sheet.write(0,0,'申请编号',style_heading)
#     sheet.write(0,1,'客户名称',style_heading)
#     sheet.write(0,2,'联系方式',style_heading)
#     sheet.write(0,3,'身份证号码',style_heading)
#     sheet.write(0,4,'办理日期',style_heading)
#     sheet.write(0,5,'处理人',style_heading)
#     sheet.write(0,6,'处理状态',style_heading)
#     sheet.write(0,7,'处理时间',style_heading)
#
#     # 写入数据
#     data_row = 1
#     # UserTable.objects.all()这个是查询条件,可以根据自己的实际需求做调整.
#     res_list = WeeklyCoreTable.objects.all().values().filter(nBirdsType=1,nGeneration=1)
#     print('%'*20,res_list)
#     for i in res_list:
#         print('####',i)
#         # 格式化datetime
#         # pri_time = i.pri_date.strftime('%Y-%m-%d')
#         # oper_time = i.operating_time.strftime('%Y-%m-%d')
#         sheet.write(data_row,0,i['Year'])
#         sheet.write(data_row,1,i['WeekNum'])
#         sheet.write(data_row,2,i['startDate'])
#         sheet.write(data_row,3,i['endDate'])
#         sheet.write(data_row,4,i['TotalYuChengCunLan'])
#         sheet.write(data_row,5,i['TotalChanDanCunLan'])
#         sheet.write(data_row,6,i['TotalDan'])
#         sheet.write(data_row,7,i['TotalChuJi'])
#         data_row = data_row + 1
#
#     # 写出到IO
#     output = BytesIO()
#     wb.save(output)
#     # 重新定位到开始
#     output.seek(0)
#     response.write(output.getvalue())
#     return response
