import pandas as pd

def convert_stata_to_excel(stata_file, excel_file):
    try:
        # 从Stata文件中读取数据
        data = pd.read_stata(stata_file)
        
        # 将数据保存为Excel文件
        data.to_excel(excel_file, index=False)
        
        print("转换成功！")
    except Exception as e:
        print("转换失败：", str(e))

# 调用函数进行转换
convert_stata_to_excel('data.dta', 'output.xlsx')
