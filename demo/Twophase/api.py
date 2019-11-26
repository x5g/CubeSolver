import Twophase.solver as sv
import re

def cube_solver(cubestring):
    a = sv.solve(cubestring, 20, 2)  # solve with a maximum of 20 moves and a timeout of 2 seconds for example
    # a = sv.solve(cubestring, 18, 5)  # solve with a maximum of 18 moves and a timeout of 5 seconds for example
    a = re.compile('1').sub('', a)  # 替换算法中的1
    a = re.compile('3').sub('\'', a)    # 替换算法中的3
    pos = a.find('(')   # 删掉后面的步数
    # print(a[:pos - 1])
    return a[:pos - 1]

if __name__=='__main__':
    cube_solver('DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL')