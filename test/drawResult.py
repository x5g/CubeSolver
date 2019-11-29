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
xl = xlrd.open_workbook (r'F:\result.xls')
sheet = xl.sheet_by_name('Comparision')
ave_cube = 0
ave_deep = 0
for num in  range (1000):
    y_cube.append(sheet.row((num+1))[1].value)
    y_deep.append(sheet.row((num+1))[3].value)
    ave_cube=ave_cube + y_cube[num]
    ave_deep=ave_deep + y_deep[num]

ave_deep = ave_deep/1000
ave_cube = ave_cube/1000
print(ave_cube)
print(ave_deep)

# Draw line chart
x=[]
for i in range (1000): # Abscissa assignment
    x.append((i+1))
pl.figure(figsize=[20,5],dpi= 400)
pl.plot(x, y_cube, 'r', label='CubeSolver')
pl.plot(x, y_deep, 'g', label='DeepCubeA')


pl.title('Comparision of CubeSolver and DeepCubeA')
pl.xlabel('Time')
pl.ylabel('Step Number')
pl.xlim(0,1000)
pl.ylim(15,40)
pl.legend()
pl.show()
