# Compare Cube Solver and DeepCubeA
# Author: Wang Wei
from selenium import webdriver
from matplotlib import pyplot as plt
from time import sleep
import xlwt
import pylab as pl

def setcolor():  # set cube's color for cubesolver
    # front
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[i] + "';", sqa[i + 12])
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[i + 3] + "';", sqa[i + 24])
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[i + 6] + "';", sqa[i + 36])
    # back
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[17 - i] + "';", sqa[18 + i])
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[14 - i] + "';", sqa[i + 30])
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[11 - i] + "';", sqa[42 + i])
    # right
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[18 + i] + "';", sqa[15 + i])
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[21 + i] + "';", sqa[27 + i])
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[24 + i] + "';", sqa[39 + i])
    # left
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[i + 27] + "';", sqa[i + 9])
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[i + 30] + "';", sqa[i + 21])
    for i in range(3):
        browser.execute_script("arguments[0].style = '" + square[i + 33] + "';", sqa[i + 33])
    # top
    for i in range(9):
        browser.execute_script("arguments[0].style = '" + square[i + 36] + "';", sqa[i])
    # bottom
    for j in range(9):
        browser.execute_script("arguments[0].style = '" + square[j + 45] + "';", sqa[j + 45])
    # because two cube's style is different, need a little transform
    for i in range(54):
        if (sqa[i].get_attribute('style') == "background-color: rgb(51, 204, 51);"):
            browser.execute_script("arguments[0].style = 'background-color:green';", sqa[i])
        elif (sqa[i].get_attribute('style') == "background-color: rgb(255, 128, 0);"):
            browser.execute_script("arguments[0].style = 'background-color:orange';", sqa[i])
        elif (sqa[i].get_attribute('style') == "background-color: rgb(255, 255, 255);"):
            browser.execute_script("arguments[0].style = 'background-color:white';", sqa[i])
        elif (sqa[i].get_attribute('style') == "background-color: rgb(0, 0, 255);"):
            browser.execute_script("arguments[0].style = 'background-color:blue';", sqa[i])
        elif (sqa[i].get_attribute('style') == "background-color: rgb(255, 255, 26);"):
            browser.execute_script("arguments[0].style = 'background-color:yellow';", sqa[i])
        else:
            browser.execute_script("arguments[0].style = 'background-color:red';", sqa[i])

    sleep(5)


def remove_same(arr):  # Delete array continuous repeating elements
    i=0
    while(i<(len(arr) - 1)):
        if (arr[i] == arr[i + 1]):
            arr.pop(i)
            i=i-1
        i=i+1

# Create a sheet to save the results
work_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = work_book.add_sheet('Comparision', cell_overwrite_ok=True)

sheet.write(0, 0, 'CubeSolver')
sheet.write(0, 1, 'Step_Number')
sheet.write(0, 2, 'DeepCube')
sheet.write(0, 3, 'Step_Number')

# "test" refers to the name of the table, "cell_overwrite_ok=true" allows overwrite

chrome_driver = 'D:\Google\Chrome\Application\chromedriver.exe'  # 配置chromedriver
browser = webdriver.Chrome(executable_path=chrome_driver)
browser0 = webdriver.Chrome(executable_path=chrome_driver)
browser.get('https://czx.ac.cn/cubesolvertest')  # 发起http请求
browser0.get('http://deepcube.igb.uci.edu')
browser0.implicitly_wait(4)

# Get the interface element location of DeepCubeA
scramble = browser0.find_element_by_id('scramble')
solve0 = browser0.find_element_by_id('solve')

# Get the interface element location of CubeSolver
cubein = browser.find_element_by_id('solinput')
executeall = browser.find_element_by_id('ExecuteAll')
solve = browser.find_element_by_id('sbtn')
sqa = []  # Locate 54 small square points
for j in range(54):
    sqa.append(browser.find_element_by_id('f' + str(j)))
sleep(2)

y_cube = []
y_deep = []
for num in range (1000) :     # Loop test code
    # Scramble Rubik's cube
    scramble.click()
    sleep(2)
    list = browser0.find_elements_by_class_name("sticker")
    square = []  # Get the color of all squares
    for i in range(54):
        style = list[i].get_attribute('style')
        square.append(style)

    setcolor()  # Set Rubik's cube colors for CubeSolver

    # CubeSolver solve
    sqa[0].click()
    solve.click()
    # DeepCubeA solve
    solve0.click()
    sleep(3)

    next = browser.find_element_by_id('nextBtn')
    for i in range(22):
        next.click()
        sleep(0.5)
    sleep(10)

    # Get the solution formula and steps
    # Cube Solver
    solotput = browser.find_element_by_id('soloutput')
    formula = str(solotput.get_attribute('value'))
    len_f = formula.split(" ")  # Split steps by space
    len_num = len(len_f) - 1
    y_cube.append(len_num)
    print("CubeSolver's solution sequence and step number :")
    print(formula)
    print(len(len_f) - 1)
    # deepcube
    solotput0 = browser0.find_element_by_id('solution_text')
    formula0 = str(solotput0.text)
    formula0 = formula0[10:-8]
    len_f0 = formula0.split(" ")  # Split steps by space
    remove_same(len_f0)  # Remove the same steps
    len_num0 = len(len_f0)
    y_deep.append(len_num0)
    print("DeepCube's solution sequence and step number :")
    print(formula0)
    print(len(len_f0))

    print("Loop"+ str(num))
    # Write in a sheet
    sheet.write(num + 1, 0, formula)
    sheet.write(num + 1, 1, len_num)
    sheet.write(num + 1, 2, formula0)
    sheet.write(num + 1, 3, len_num0)

    work_book.save(r'F:\result.xls')


    sleep(3)


pass
