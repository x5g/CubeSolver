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
xl = xlrd.open_workbook (r'result.xls')
sheet = xl.sheet_by_name('Comparision')
ave_cube = 0
ave_deep = 0
for num in range (1000):
    y_cube.append(sheet.row(num+1)[1].value)
    y_deep.append(sheet.row(num+1)[3].value)
    ave_cube=ave_cube + y_cube[num]
    ave_deep=ave_deep + y_deep[num]

ave_deep = ave_deep/1000
ave_cube = ave_cube/1000
print(ave_cube)
print(ave_deep)

# Draw the result
x=[]
for i in range (1000): # Abscissa assignment
    x.append((i+1))
plt.figure(figsize=[20,5],dpi= 400)

# Broken line diagram
#plt.plot(x, y_cube, 'r', label='CubeSolver')
#plt.plot(x, y_deep, 'g', label='DeepCubeA')

# Scatter diagram
plt.scatter(x, y_cube, marker = 'x',color = 'red', s = 15 ,label = 'CubeSolver')
plt.scatter(x, y_deep, marker = 'o', color = 'green', s = 15, label = 'DeepCubeA')

plt.title('Comparision of CubeSolver and DeepCubeA')
plt.xlabel('Time')
plt.ylabel('Step Number')
plt.xlim(0,1000)
plt.ylim(15,40)
plt.legend()
plt.show()
