# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:39:01 2021

@author: Admin
"""

import os
import pandas as pd
import re

path = os.getcwd()
os.chdir(path)

data = pd.read_csv("output1.csv", encoding='UTF-8')

#Cột price range, min price, max price, rank, number_images_Traveler ban đầu khi chưa chỉnh sửa
print(data[["Price_range"]])
print(data["Price_min"])
print(data["Price_max"])
print(data["Rank"])
print(data["number_images_Traveler"])
print(data["Room_number"])
print(data["Review_number"])

#Tạo list rỗng
data0 = []
data1= []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []

#Chỉnh sửa các cột 
#Hàm re.split trả về một danh sách trong đó chuỗi đã được phân chia theo mỗi kết quả khớp.
for item0 in data["Price_range"]:
    item0 = re.split(r'₫', item0)
    data0.append(item0[1:])

for item in data["Price_min"]:
    item = re.split(r'₫', item)
    data1.append(item[1])

for item1 in data["Price_max"]:
    item1 = re.split(r'₫', item1)
    data2.append(item1[1])

for item2 in data["Rank"]:
    item2 = re.split(r'#', item2)
    data3.append(item2[1])

#Hàm re.sub thay thế một hoặc nhiều kết quả khớp trong chuỗi
for item3 in data["number_images_Traveler"]:
    item3 = re.sub(r"\r", "", item3)
    data4.append(item3[3:-3])

for item4 in data["Room_number"]:
    item4 = re.sub(r"Hue", "0", item4)
    item4 = int(item4)
    data5.append(item4)

for item5 in data["Review_number"]:
    item5 = re.sub(r"reviews", "", item5)
    data6.append(item5)

#def ARG(data):
    #for item6 in data[("Attractions", "Restaurant_nearby", "Great_for_walker")]:
        #item6 = re.sub(r" ", "0", item6)
        #data7.append(item6)

    
#Cột price range, min price, max price, rank, number_images_Traveler sau khi đã chỉnh sửa
data["Price_range"] = data0
data["Price_min"] = data1
data["Price_max"] = data2
data["Rank"] = data3
data["number_images_Traveler"] = data4
data["Room_number"] = data5
data["Review_number"] = data6
#data[["Attractions", "Restaurant_nearby", "Great_for_walker"]] = data7 


#Lưu file mới
data.to_csv("Tripadvisor_Data.csv")










  