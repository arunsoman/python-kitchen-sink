import numpy as np
from pulp import *
def create_bar(bars, height, width, minbarwith = 2, maxbarwidth = 10, bargap=1):
    status, w = solve(len(bars),width, minbarwith,maxbarwidth,bargap)
    if status is 'Infeasible':
        raise "Infeasible"
    ss = np.array(range(0,len(bars)))
    bxv = ss*(w+bargap)
    bwv = w+bxv
    rects = [(s,0,e,v) for s,e,v in zip(bxv,bwv,bars)]
    print rects
    return rects

def solve(barCnt, width, minVal, maxVal, bargap):
    prob = LpProblem("The Bar Problem", LpMinimize)
    x1 = LpVariable("Bar width", 0, None, LpInteger)
    prob+= x1 , "zal"
    prob+= barCnt*(x1+bargap) <= width, "mal"
    prob+= x1<= maxVal, "c1"
    prob+= x1>= minVal, "c2"
    prob.solve()
    #print("Status:", LpStatus[prob.status])
    #for v in prob.variables():
    #    print(v.name, "=", v.varValue)
    #print("Total Cost = ", value(prob.objective))
    return LpStatus[prob.status], value(prob.objective)

create_bar({10,7,12},100, 200,9, 10, 5)
solve(10,200,9, 10, 5)
solve(10,90,9, 10, 5)
