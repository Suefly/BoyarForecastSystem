import xlwt
file = 'C:\\Users\\sujie\\Desktop\\家禽计量系统\\database\\LivePeriodTable.txt'

birth_data = []
workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = workbook.add_sheet('test', cell_overwrite_ok=True)
with open(file,'r') as f:
    reader = f.read().split('\n')  # 使用csv.reader读取csvfile中的文件
    # print(reader,type(reader))
    for index,value in enumerate(reader):
        print(index)
        s = value.split(' ')
        rr = []
        for i in s:
            if i !='':
                rr.append(i)
        print(rr)
        sheet.write(index, 0, rr[0])
        sheet.write(index, 1, rr[1])
        sheet.write(index, 2, rr[2])
        sheet.write(index, 3, rr[3])
        sheet.write(index, 4, rr[4])
        sheet.write(index, 5, rr[5])
workbook.save('D:\\test.xls')

