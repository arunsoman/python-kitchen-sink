import numpy as np
from numpy import exp

def rmse(predictions, targets):
    return np.sqrt(np.mean((predictions - targets) ** 2))


def rmseN(predictions, targets, n):
    return rmse(predictions[-n:], targets[-n:])


def computeSweetSpot(min, max, minTol, maxTol):
    return (max - maxTol) - (min + minTol)

def analyze(min, max, minP, maxP):
    status = dict()

    minRMSE5 = rmseN(min, minP,5)
    minRMSE15 = rmseN(min, minP,15)

    maxRMSE5 = rmseN(max, maxP,5)
    maxRMSE15 = rmseN(max, maxP,15)

    status['minRMSE'] = minRMSE5 / minRMSE15
    status['maxRMSE'] = maxRMSE5 / maxRMSE15
    status['sweetspot'] = computeSweetSpot(min, max, minRMSE5, maxRMSE5)

    return status

def customSigmoid(x):
    return 100/(100+exp(x*4))

def analyzeStats(statsList):
