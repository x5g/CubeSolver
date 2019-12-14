import numpy as np
from brokenaxes import brokenaxes
from selenium import webdriver
import time
import xlrd
import kociemba


def remove_same(arr):  # Delete array continuous repeating elements
    i=0
    while(i<(len(arr) - 1)):
        if (arr[i] == arr[i + 1] or arr[i]=="X" or arr[i]=="X'" or arr[i]=="Y" or arr[i]=="Y'" or arr[i]=="Z" or arr[i]=="Z'" or arr[i]=="X2" or arr[i]=="Y2" or arr[i]=="Z2"):
            arr.pop(i)
            i=i-1
        i=i+1

'''
# 获取层先法和CFOP 其中CFOP可以通过CHAOS-master
browser = webdriver.Chrome()
browser.get('http://159.226.5.97:9006')  # 发起http请求
time.sleep(2)

autoelem = browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[3]/div/ul/li[3]/div/div/input')
autoelem.click()
time.sleep(1)

xl = xlrd.open_workbook('result.xls')
sheet = xl.sheet_by_name('Comparision')

for num in range(1000):
    # input = "D U' B' U' B D' B' D' L' L' U B F' D U' B R' U' D' D' U' F' U L'"
    input = sheet.row(num+1)[0].value
    #print(input)

    recoveryelem = browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/div/ul/li[5]')
    recoveryelem.click()
    time.sleep(1)

    inputelem = browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[4]/div/ul/li[2]/div/div/input')
    inputelem.send_keys(input)
    time.sleep(1)

    executeelem = browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[4]/div/ul/li[6]')
    executeelem.click()
    time.sleep(5)

    executedelem = browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[4]/div/ul/li[3]/div/div/input')
    executedelem.clear()
    time.sleep(1)

    solveelem = browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[3]/div/ul/li[4]')
    solveelem.click()
    # time.sleep(20)
    while str(inputelem.get_attribute('value')) == "":
        pass
    time.sleep(1)

    output = inputelem.get_attribute('value')
    print(output)

    # output_arr = output.split(' ')
    # remove_same(output_arr)
    # print(len(output_arr))

    # stateelem = browser.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/div/ul/li[3]/div/div/input')
    # print(stateelem.get_attribute('value'))
'''

'''
# 获取CubeSolver(20,2)和CubeSolver(18,5)
browser = webdriver.Chrome()
# browser.get('https://czx.ac.cn/cubesolvertest')  # 发起http请求
browser.get('http://127.0.0.1:8000/cubesolvertest')
time.sleep(2)

for num in range(1000):
    # input = "D U' B' U' B D' B' D' L' L' U B F' D U' B R' U' D' D' U' F' U L'"
    input = sheet.row(num+1)[4].value

    inputelem = browser.find_element_by_id('solinput')
    inputelem.clear()
    inputelem.send_keys(input)
    rotationelem = browser.find_element_by_id('Rotation')
    rotationelem.click()
    time.sleep(2)

    solveelem = browser.find_element_by_id('sbtn')
    solveelem.click()
    time.sleep(6)

    outputelem = browser.find_element_by_id('soloutput')

    output = outputelem.get_attribute('value')
    print(output)

    homeelem = browser.find_element_by_xpath('/html/body/div[2]/center/table/tbody/tr/td[1]/table[2]/tbody/tr[2]/td[1]/button')
    homeelem.click()
    time.sleep(1)
'''

'''
# 计算步数 去重
xl = xlrd.open_workbook (r'result.xls')
sheet = xl.sheet_by_name('Comparision')
for num in range(1000):
    input = sheet.row(num + 1)[13].value
    output_arr = input.split(' ')
    remove_same(output_arr)
    print(len(output_arr))
'''

'''
# 计算步数 不去重
xl = xlrd.open_workbook('result.xls')
sheet = xl.sheet_by_name('Comparision')
for num in range(1000):
    input = sheet.row(num + 1)[7].value
    output_arr = input.split(' ')

    # 带步数(20f)这样的写法
    # step_number = len(output_arr) - 1
    # for i in range(len(output_arr) - 1) :
    # if output_arr[i].find('2') == 1:
    #     step_number = step_number + 1

    # 不带步数的写法
    step_number = len(output_arr)
    for i in range(len(output_arr)):
        if output_arr[i].find('2') == 1:
            step_number = step_number + 1
    print(step_number)
'''

'''
# 画图1
# Draw the result from result.xls
# Author: Wang Wei
from selenium import webdriver
from matplotlib import pyplot as plt
from time import sleep
import xlwt
import xlrd
import pylab as pl


y_OKociemba=[]
y_DeepCubeA=[]
y_LayerFirst=[]
y_CFOP=[]
y_Kociemba=[]
y_OKociemba2=[]
xl = xlrd.open_workbook (r'result.xls')
sheet = xl.sheet_by_name('Comparision')
ave_OKociemba = 0
ave_DeepCubeA = 0
ave_LayerFirst = 0
ave_CFOP = 0
ave_Kociemba = 0
ave_OKociemba2 = 0
for num in range (1000):
    # 两种技计数模式：模式一 计算认为D2为1步，模式二 认为D2为2步

    # 第一种计数模式下的数据源
    # y_OKociemba.append(sheet.row(num+1)[2].value)
    # y_DeepCubeA.append(sheet.row(num+1)[5].value)
    # y_LayerFirst.append(sheet.row(num+1)[8].value)
    # y_CFOP.append(sheet.row(num+1)[11].value)
    # y_Kociemba.append(sheet.row(num+1)[14].value)
    # y_OKociemba2.append(sheet.row(num+1)[17].value)

    # 第二种计数模式下的数据源
    y_OKociemba.append(sheet.row(num+1)[3].value)
    y_DeepCubeA.append(sheet.row(num+1)[6].value)
    y_LayerFirst.append(sheet.row(num+1)[9].value)
    y_CFOP.append(sheet.row(num+1)[12].value)
    y_Kociemba.append(sheet.row(num+1)[15].value)
    y_OKociemba2.append(sheet.row(num+1)[18].value)

    ave_OKociemba = ave_OKociemba + y_OKociemba[num]
    ave_DeepCubeA = ave_DeepCubeA + y_DeepCubeA[num]
    ave_LayerFirst = ave_LayerFirst + y_LayerFirst[num]
    ave_CFOP = ave_CFOP + y_CFOP[num]
    ave_Kociemba = ave_Kociemba + y_Kociemba[num]
    ave_OKociemba2 = ave_OKociemba2 + y_OKociemba2[num]

ave_OKociemba = ave_OKociemba / 1000
ave_DeepCubeA = ave_DeepCubeA / 1000
ave_LayerFirst = ave_LayerFirst / 1000
ave_CFOP = ave_CFOP / 1000
ave_Kociemba = ave_Kociemba / 1000
ave_OKociemba2 = ave_OKociemba2 / 1000
print("Kociemba = ", str(ave_Kociemba), str(min(y_Kociemba)), str(max(y_Kociemba)))
print("OKociemba = ", str(ave_OKociemba), str(min(y_OKociemba)), str(max(y_OKociemba)))
print("Okociemba2 = ", str(ave_OKociemba2), str(min(y_OKociemba2)), str(max(y_OKociemba2)))
print("CFOP = ", str(ave_CFOP), str(min(y_CFOP)), str(max(y_CFOP)))
print("LayerFirst = ", str(ave_LayerFirst), str(min(y_LayerFirst)), str(max(y_LayerFirst)))
print("DeepCubeA = ", str(ave_DeepCubeA), str(min(y_DeepCubeA)), str(max(y_DeepCubeA)))

# Draw the result
x=[]
for i in range (1000): # Abscissa assignment
    x.append((i+1))
plt.figure(figsize=[20,5],dpi= 400)

# Broken line diagram
plt.plot(x, y_OKociemba2, 'blue', label='O-Kociemba(18,5)')
plt.plot(x, y_OKociemba, 'red', label='O-Kociemba(20,2)')
plt.plot(x, y_DeepCubeA, 'green', label='DeepCubeA')
plt.plot(x, y_LayerFirst, 'black', label='LayerFirst')
plt.plot(x, y_CFOP, 'purple', label='CFOP')
plt.plot(x, y_Kociemba, 'orange', label='Kociemba')

# Scatter diagram
# plt.scatter(x, y_OKociemba2, marker = '.', color = 'blue', s = 15, label = 'O-Kociemba(18,5)')
# plt.scatter(x, y_OKociemba, marker = '.',color = 'red', s = 15 ,label = 'O-Kociemba(20,2)')
# plt.scatter(x, y_DeepCubeA, marker = '.', color = 'green', s = 15, label = 'DeepCubeA')
# plt.scatter(x, y_LayerFirst, marker = '.',color = 'black', s = 15 ,label = 'LayerFirst')
# plt.scatter(x, y_CFOP, marker = '.', color = 'purple', s = 15, label = 'CFOP')
# plt.scatter(x, y_Kociemba, marker = '.',color = 'orange', s = 15 ,label = 'Kociemba')

# 第一种计数模式下的标题
# plt.title('Comparision of O-Kociemba(18,5), O-Kociemba(20,2), DeepCubeA, LayerFirst, CFOP and Kociemba in Counting Mode 1')
# 第二种计数模式下的标题
plt.title('Comparision of O-Kociemba(18,5), O-Kociemba(20,2), DeepCubeA, LayerFirst, CFOP and Kociemba in Counting Mode 2')
plt.xlabel('Time')
plt.ylabel('Step Number')
plt.xlim(0,1000)
# 第一种计数模式下的范围
# plt.ylim(0,180)
# 第二种计数模式下的范围
plt.ylim(0, 200)
plt.legend(loc = 1)
plt.show()
'''


# 画图2
# Draw the result from result.xls
# Author: Wang Wei
from selenium import webdriver
from matplotlib import pyplot as plt
from time import sleep
import xlwt
import xlrd
import pylab as pl

y_OKociemba=[]
y_DeepCubeA=[]
y_Kociemba=[]
y_OKociemba2=[]
xl = xlrd.open_workbook (r'result.xls')
sheet = xl.sheet_by_name('Comparision')
ave_OKociemba = 0
ave_DeepCubeA = 0
ave_Kociemba = 0
ave_OKociemba2 = 0
for num in range (1000):
    # 两种技计数模式：模式一 计算认为D2为1步，模式二 认为D2为2步

    # 第一种计数模式下的数据源
    # y_OKociemba.append(sheet.row(num+1)[2].value)
    # y_DeepCubeA.append(sheet.row(num+1)[5].value)
    # y_Kociemba.append(sheet.row(num+1)[14].value)
    # y_OKociemba2.append(sheet.row(num+1)[17].value)

    # 第二种计数模式下的数据源
    y_OKociemba.append(sheet.row(num+1)[3].value)
    y_DeepCubeA.append(sheet.row(num+1)[6].value)
    y_Kociemba.append(sheet.row(num+1)[15].value)
    y_OKociemba2.append(sheet.row(num+1)[18].value)

    ave_OKociemba = ave_OKociemba + y_OKociemba[num]
    ave_DeepCubeA = ave_DeepCubeA + y_DeepCubeA[num]
    ave_Kociemba = ave_Kociemba + y_Kociemba[num]
    ave_OKociemba2 = ave_OKociemba2 + y_OKociemba2[num]

ave_OKociemba = ave_OKociemba / 1000
ave_DeepCubeA = ave_DeepCubeA / 1000
ave_Kociemba = ave_Kociemba / 1000
ave_OKociemba2 = ave_OKociemba2 / 1000
print("Kociemba = ", str(ave_Kociemba), str(min(y_Kociemba)), str(max(y_Kociemba)))
print("OKociemba = ", str(ave_OKociemba), str(min(y_OKociemba)), str(max(y_OKociemba)))
print("Okociemba2 = ", str(ave_OKociemba2), str(min(y_OKociemba2)), str(max(y_OKociemba2)))
print("DeepCubeA = ", str(ave_DeepCubeA), str(min(y_DeepCubeA)), str(max(y_DeepCubeA)))


# Draw the result
x=[]
for i in range (1000): # Abscissa assignment
    x.append((i+1))
plt.figure(figsize=[20,5],dpi= 400)

# Broken line diagram
plt.plot(x, y_OKociemba2, 'blue', label='O-Kociemba(18,5)')
plt.plot(x, y_OKociemba, 'red', label='O-Kociemba(20,2)')
plt.plot(x, y_DeepCubeA, 'green', label='DeepCubeA')
plt.plot(x, y_Kociemba, 'orange', label='Kociemba')

# Scatter diagram
# plt.scatter(x, y_OKociemba2, marker = '.', color = 'blue', s = 15, label = 'O-Kociemba(18,5)')
# plt.scatter(x, y_OKociemba, marker = '.',color = 'red', s = 15 ,label = 'O-Kociemba(20,2)')
# plt.scatter(x, y_DeepCubeA, marker = '.', color = 'green', s = 15, label = 'DeepCubeA')
# plt.scatter(x, y_Kociemba, marker = '.',color = 'orange', s = 15 ,label = 'Kociemba')


# 第一种计数模式下的标题
# plt.title('Comparision of O-Kociemba(18,5), O-Kociemba(20,2), DeepCubeA and Kociemba in Counting Mode 1')
# 第二种计数模式下的标题
plt.title('Comparision of O-Kociemba(18,5), O-Kociemba(20,2), DeepCubeA and Kociemba in Counting Mode 2')
plt.xlabel('Time')
plt.ylabel('Step Number')
plt.xlim(0,1000)
# 第一种计数模式下的范围
# plt.ylim(15,40)
# 第二种技术模式下的范围
plt.ylim(15,45)
plt.legend(loc = 1)
plt.show()

