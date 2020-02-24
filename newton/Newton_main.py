'''
Created on Feb 21, 2020

@author: mizuno
'''

import sympy as sp
import newton.Newton_lib as mdl

#今回利用する関数
x0, x1, x2 = sp.symbols('x0 x1 x2')
#https://qiita.com/utahkaA/items/45ebadd70c3020e8c320
f = x1**3 +x2**3 -9*x1*x2 +27
print(f)
x0 = sp.Matrix([10,8]) #初期値
n = 7 #繰り返し回数
nlib = mdl.Newton_lib(f, x0, n)
nlib.getSolution()
x0 = nlib.getPoint()
print('最適解')
print(x0)

