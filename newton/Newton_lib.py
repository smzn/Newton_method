'''
Created on Feb 21, 2020

@author: mizuno
'''
import sympy as sp
from numpy.linalg import solve

class Newton_lib:
    def __init__(self, f, x0, n):
        self._f = f
        self._x0 = sp.symbols('x0')
        self._x1, self._x2 = sp.symbols('x1 x2') #今回は2変数(x1, x2)
        self._x0 = x0
        self._n = n #繰り返し回数
        self._dfx1 = sp.diff(f, self._x1) #x1での偏微分
        self._dfx2 = sp.diff(f, self._x2) #x2での偏微分
        self._dfx1x2 = sp.diff(self._dfx1, self._x2)
        self._dfx2x1 = sp.diff(self._dfx2, self._x1)
        self._ddfx1 = sp.diff(f, self._x1, 2) #x1での2階偏微分
        self._ddfx2 = sp.diff(f, self._x2, 2) #x2での2階偏微分
        self._df = sp.Matrix([[self._dfx1], [self._dfx2]])
        print('df1階微分行列')
        print(self._df)
        self._hesse = sp.Matrix([[self._ddfx1, self._dfx1x2], [self._dfx2x1, self._ddfx2]])
        #self._hesse_n = sp.matrix2numpy(self._hesse)
        print('ddf 2階微分：ヘッセ行列')
        print(self._hesse)

    def getSolution(self):
        for i in range(self._n):
            print(str(i+1)+'回目')
            df_sub = self._df.subs([(self._x1, self._x0[0]), (self._x2, self._x0[1])])
            df_sub_n = sp.matrix2numpy(df_sub, dtype='float') #solveに入れる時実数にしないとダメ
            print('df代入')
            print(df_sub_n)
            hesse_sub = self._hesse.subs([(self._x1, self._x0[0]), (self._x2, self._x0[1])])
            hesse_sub_n = sp.matrix2numpy(hesse_sub, dtype='float') #solveに入れる時実数にしないとダメ
            print('Hesse代入')
            print(hesse_sub_n)
            slv = solve(hesse_sub_n,  -1 * df_sub_n) #numpy型に変換してから計算
            print('方程式の解：増分Δx算出')
            print(slv)
            self._x0 = self._x0 + slv
            print('更新x0')
            print(self._x0)

    def getPoint(self):
        return self._x0
