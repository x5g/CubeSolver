# Automated Test
# Author: Wang Wei
from selenium import webdriver

from time import sleep

file=open("input.txt",mode="r",encoding="utf-8") # open test file

chrome_driver = 'D:\Google\Chrome\Application\chromedriver.exe' # configure chromedriver
browser =webdriver.Chrome(executable_path=chrome_driver)
browser.get('https://czx.ac.cn/cubesolver') # send http request
browser.implicitly_wait(4)

# Interface element positioning
cubein = browser.find_element_by_id('solinput')
executeall = browser.find_element_by_id('ExecuteAll')
solve = browser.find_element_by_id('sbtn')
sqa=[]   # Locate 54 small square points
for j in range (54):
    sqa.append(browser.find_element_by_id('f'+str(j)))

def comp():  # Confirm whether the result after solve is correct
    style=[]  # Style value of the box
    for i in range (54):
        style.append(sqa[i].get_attribute('style'))
    if(style[0]==style[1]==style[2]==style[3]==style[4]==style[5]==style[6]==style[7]==style[8]and
    style[9]==style[10]==style[11]==style[21]==style[22]==style[23]==style[33]==style[34]==style[35]and
    style[12]==style[13]==style[14]==style[24]==style[25]==style[26]==style[36]==style[37]==style[38]and
    style[15]==style[16]==style[17]==style[27]==style[28]==style[29]==style[39]==style[40]==style[41]and
    style[18]==style[19]==style[20]==style[30]==style[31]==style[32]==style[42]==style[43]==style[44]and
    style[45]==style[46]==style[47]==style[48]==style[49]==style[50]==style[51]==style[52]==style[53]):
        print("The cube solver is correct")
    else:
        print("The cube solver is wrong")


content =file.readline()
print("Test 1 :ExecuteAll \nEnter the testing formula: "+content.strip())
cubein.send_keys(content) # Enter scramble code
sleep(3)

print("Disorganize the cube according to the formula")
executeall.click()
sleep(3)

print("Solve the problem and get the reduction formula")
solve.click()
sleep(1)
formula = cubein.get_attribute('value')
print("The reduction formula is: " +str(formula))
sleep(3)

print("Restore the cube according to the formula")
executeall.click()
sleep(3)

comp()   # Test whether the result of slove is correct
sleep(3)


cubein.clear()
content =file.readline()
print("\nTest 2 :Distributed execution \nEnter the testing formula: "+content.strip())
cubein.send_keys(content) # Enter scramble code
sleep(3)

print("Disorganize the cube according to the formula")
executeall.click()
sleep(3)

print("Solve the problem and get the reduction formula")
solve.click()
sleep(1)
formula = cubein.get_attribute('value')
print("The reduction formula is: " +str(formula))
sleep(3)

print("Restore the cube according to the formula")
next = browser.find_element_by_id('nextBtn')
for i in range (22):
    next.click()
    sleep(1)

comp()   # Test whether the result of slove is correct
sleep(3)

file.close()
browser.close()
pass
