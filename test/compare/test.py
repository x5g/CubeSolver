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
xl = xlrd.open_workbook (r'result.xls')
sheet = xl.sheet_by_name('Comparision')
for num in range(1000):
    input = sheet.row(num + 1)[11].value
    output_arr = input.split(' ')
    print(len(output_arr) - 1)
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


y_cube=[]
y_deep=[]
y_cengxianfa=[]
y_cfop=[]
y_kociemba=[]
y_cubesolver2=[]
xl = xlrd.open_workbook (r'result.xls')
sheet = xl.sheet_by_name('Comparision')
ave_cube = 0
ave_deep = 0
ave_cengxianfa=0
ave_cfop=0
ave_kociemba=0
ave_cubesolver2=0
for num in range (1000):
    y_cube.append(sheet.row(num+1)[1].value)
    y_deep.append(sheet.row(num+1)[3].value)
    y_cengxianfa.append(sheet.row(num+1)[6].value)
    y_cfop.append(sheet.row(num+1)[8].value)
    y_kociemba.append(sheet.row(num+1)[10].value)
    y_cubesolver2.append(sheet.row(num+1)[12].value)
    ave_cube=ave_cube + y_cube[num]
    ave_deep=ave_deep + y_deep[num]
    ave_cengxianfa=ave_cengxianfa+y_cengxianfa[num]
    ave_cfop=ave_cfop+y_cfop[num]
    ave_kociemba=ave_kociemba+y_kociemba[num]
    ave_cubesolver2=ave_cubesolver2+y_cubesolver2[num]

ave_cube = ave_cube/1000
ave_deep = ave_deep/1000
ave_cengxianfa = ave_cengxianfa/1000
ave_cfop = ave_cfop/1000
ave_kociemba = ave_kociemba/1000
ave_cubesolver2 = ave_cubesolver2/1000
print(str(ave_kociemba), str(min(y_kociemba)), str(max(y_kociemba)))
print(str(ave_cube), str(min(y_cube)), str(max(y_cube)))
print(str(ave_cubesolver2), str(min(y_cubesolver2)), str(max(y_cubesolver2)))
print(str(ave_cfop), str(min(y_cfop)), str(max(y_cfop)))
print(str(ave_cengxianfa), str(min(y_cengxianfa)), str(max(y_cengxianfa)))
print(str(ave_deep), str(min(y_deep)), str(max(y_deep)))

# Draw the result
x=[]
for i in range (1000): # Abscissa assignment
    x.append((i+1))
plt.figure(figsize=[20,5],dpi= 400)

# Broken line diagram
plt.plot(x, y_cubesolver2, 'blue', label='CubeSolver(18,5)')
plt.plot(x, y_cube, 'red', label='CubeSolver(20,2)')
plt.plot(x, y_deep, 'green', label='DeepCubeA')
plt.plot(x, y_cengxianfa, 'black', label='LayerFirst')
plt.plot(x, y_cfop, 'purple', label='CFOP')
plt.plot(x, y_kociemba, 'orange', label='Kociemba')

# Scatter diagram
# plt.scatter(x, y_cubesolver2, marker = '.', color = 'blue', s = 15, label = 'CubeSolver(18,5)')
# plt.scatter(x, y_cube, marker = '.',color = 'red', s = 15 ,label = 'CubeSolver(20,2)')
# plt.scatter(x, y_deep, marker = '.', color = 'green', s = 15, label = 'DeepCubeA')
# plt.scatter(x, y_cengxianfa, marker = '.',color = 'black', s = 15 ,label = 'LayerFirst')
# plt.scatter(x, y_cfop, marker = '.', color = 'purple', s = 15, label = 'CFOP')
# plt.scatter(x, y_kociemba, marker = '.',color = 'orange', s = 15 ,label = 'Kociemba')

plt.title('Comparision of CubeSolver(18,5), CubeSolver(20,2), DeepCubeA, LayerFirst, CFOP and Kociemba')
plt.xlabel('Time')
plt.ylabel('Step Number')
plt.xlim(0,1000)
plt.ylim(0,180)
plt.legend(loc = 1)
plt.show()
'''

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

y_cube=[]
y_deep=[]
y_cengxianfa=[]
y_cfop=[]
y_kociemba=[]
y_cubesolver2=[]
xl = xlrd.open_workbook (r'result.xls')
sheet = xl.sheet_by_name('Comparision')
ave_cube = 0
ave_deep = 0
ave_cengxianfa=0
ave_cfop=0
ave_kociemba=0
ave_cubesolver2=0
for num in range (1000):
    y_cube.append(sheet.row(num+1)[1].value)
    y_deep.append(sheet.row(num+1)[3].value)
    y_cengxianfa.append(sheet.row(num+1)[6].value)
    y_cfop.append(sheet.row(num+1)[8].value)
    y_kociemba.append(sheet.row(num+1)[10].value)
    y_cubesolver2.append(sheet.row(num+1)[12].value)
    ave_cube=ave_cube + y_cube[num]
    ave_deep=ave_deep + y_deep[num]
    ave_cengxianfa=ave_cengxianfa+y_cengxianfa[num]
    ave_cfop=ave_cfop+y_cfop[num]
    ave_kociemba=ave_kociemba+y_kociemba[num]
    ave_cubesolver2=ave_cubesolver2+y_cubesolver2[num]

ave_cube = ave_cube/1000
ave_deep = ave_deep/1000
ave_cengxianfa = ave_cengxianfa/1000
ave_cfop = ave_cfop/1000
ave_kociemba = ave_kociemba/1000
ave_cubesolver2 = ave_cubesolver2/1000
print(ave_cube)
print(ave_deep)
print(ave_cengxianfa)
print(ave_cfop)
print(ave_kociemba)
print(ave_cubesolver2)

# Draw the result
x=[]
for i in range (1000): # Abscissa assignment
    x.append((i+1))
plt.figure(figsize=[20,5],dpi= 400)

# Broken line diagram
plt.plot(x, y_cubesolver2, 'blue', label='CubeSolver(18,5)')
plt.plot(x, y_cube, 'red', label='CubeSolver(20,2)')
plt.plot(x, y_deep, 'green', label='DeepCubeA')
# plt.plot(x, y_cengxianfa, 'black', label='LayerFirst')
# plt.plot(x, y_cfop, 'purple', label='CFOP')
plt.plot(x, y_kociemba, 'orange', label='Kociemba')

# Scatter diagram
# plt.scatter(x, y_cubesolver2, marker = '.', color = 'blue', s = 15, label = 'CubeSolver(18,5)')
# plt.scatter(x, y_cube, marker = '.',color = 'red', s = 15 ,label = 'CubeSolver(20,2)')
# plt.scatter(x, y_deep, marker = '.', color = 'green', s = 15, label = 'DeepCubeA')
# #plt.scatter(x, y_cengxianfa, marker = '.',color = 'black', s = 15 ,label = 'LayerFirst')
# #plt.scatter(x, y_cfop, marker = '.', color = 'purple', s = 15, label = 'CFOP')
# plt.scatter(x, y_kociemba, marker = '.',color = 'orange', s = 15 ,label = 'Kociemba')

plt.title('Comparision of CubeSolver(18,5), CubeSolver(20,2), DeepCubeA and Kociemba')
plt.xlabel('Time')
plt.ylabel('Step Number')
plt.xlim(0,1000)
plt.ylim(15,40)
plt.legend(loc = 1)
plt.show()
'''
