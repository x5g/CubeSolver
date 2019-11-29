# Cube Solver
![image](https://czx.ac.cn/static/static/media/logo.4bd204f82.svg)
##Instructions
The idea is simple: you mix up a Rubik's cube. You show the cube to your computer's webcam. Some magic happens, and your cube appears onscreen. Then the cube begins to solve itself, and all you have to do is follow along and you will have solved your cube!

Here we provide a [video](http://player.bilibili.com/player.html?aid=76684072&cid=131158836&page=1) to introduce the capabilities of Cube Solver. 

In conclusion, compared with other online Rubik's cube solving web pages, our highlights are: 

1. Support multiple input modes: scanning, coloring and rotation sequence. 
2. The demonstration process of Rubik's cube solution supports the use of progress bar. 
3. Offline saving is supported in the demonstration process of Rubik's cube solution.

##Demo Website
You can experience the fun of cube solver by yourself. The demo website is [Cube Solver](https://czx.ac.cn/cubesolver)

##Code Files Description
1. demo: Cube Solver full runnable files
2. src: source file .zip of each module in Cube Solver
3. test: test files and test results in Cube Solver

##Usage
This project needs Python 3.7, Django 2 and other necessary modules. You can download all the files or just the "demo", and then enter the command in "demo":
```
python3 manage.py runserver      
```
then you can visit http://127.0.0.1:8000/cubesolver to experience the fun of Cube Solver.

##Thanks
1. hkociemba, author of our solving Rubik's cube algorithm file [RubiksCube-TwophaseSovler](https://github.com/hkociemba/rubikscube-twophasesolver).
2. petr-lee, author of our scanning Rubik's cube module file [RubikScan](https://github.com/petr-lee/RubikScan).
3. mfeather1, author of our drawing Rubik's cube module file [3ColorCube](https://github.com/mfeather1/3ColorCube).
4. kmh0228, author of our showing Rubik's cube module file [Cube.js](https://github.com/kmh0228/kmh0228.github.com/tree/master/study/Cube).
5. iyangyuan, author of our solving Rubik's cube process bar module file [ystep](https://github.com/iyangyuan/ystep).
6. carbon-app, author of our highlight codes pictures file [carbon](https://github.com/carbon-app/carbon).
7. Forest Agostinelli, Stephen McAleer, Alexander Shmakov, Pierre Baldi, thank you for opening the source code of the algorithm [DeepCubeA](https://codeocean.com/capsule/5723040/tree/v1).
8. Peng Qiancheng, Qi Bing, Duan Xu, thank you for your help in analyzing algorithm DeepCubeA.
9. Alibaba Cloud Computing, our server supplier, thank you for your low price server.
10. Professor Luo Tiejian, thank you for your idea.

<br>
Made by GZY, CZX, WW
