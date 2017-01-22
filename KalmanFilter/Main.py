from TestValueGenerator import TestValueGenerator
from AveFilter import AveFilter
from MovingAverage import MovingAverage
from LowPassFilter1st import LowPassFilter1st
from SimpleKalmanFilter import SimpleKalmanFilter

import matplotlib.pyplot as pyplot


testGenerator = TestValueGenerator()
aveFilter = AveFilter()
movAve = MovingAverage(5)
lpf = LowPassFilter1st()
kal  = SimpleKalmanFilter()

def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

xKVals = []
yKVals = []
yKRandVals = []

kal.SetInitalXandP(14, 6)

for i in frange (0.0,10.0, 0.2):
    xKVals.append(i)

    z = testGenerator.GetRandomFixedvalueLimits(14.4, 4)
    yKRandVals.append(z)

    volt = kal.SimpleKalman(z)
    yKVals.append(volt)

pyplot.plot(xKVals, yKVals, 'o-', xKVals, yKRandVals, 'r:*')
pyplot.show()

#**************Test AveFilter**************
#for i in range (0,9):
#    print(aveFilter.AvgFilter(i))

#aveFilter.ResetAvgFilter()
#print()

#for i in range (0,10000):
#    val = testGenerator.GetRandomAroundFixedValue()
#    aveFilter.AvgFilter(val)

#print(aveFilter.prevAvg)



#**************Test Moving Average Filter**************
#print("*****MovAve*****")

#for i in range(0,100):
#    print(movAve.MovAvgFilter(i))

#print()

#movAve.ResetMovAveFilter()
#print("*****MovAveReset*****")
#for i in range(0,100):
#    print(movAve.MovAvgFilter(i))



#**************Test Low Pass Filter**************
#xVals = []
#yValue = []
#yLpf = []

#for i in range (0,500):
#    val = testGenerator.GetRandom(-30.0, 30.0) + i * i * 0.001
#    lpfCurrent = lpf.LowPass1stOrderFilter(val)
#    xVals.append(i)
#    yValue.append(val)
#    yLpf.append(lpfCurrent)

#pyplot.plot(xVals, yValue, 'b-', xVals, yLpf, 'r-')
#pyplot.show()
