from TestValueGenerator import TestValueGenerator
from AveFilter import AveFilter
from MovingAverage import MovingAverage
from LowPassFilter1st import LowPassFilter1st
import matplotlib.pyplot as pyplot


testGenerator = TestValueGenerator()
aveFilter = AveFilter()
movAve = MovingAverage(5)
lpf = LowPassFilter1st()

for i in range (0,9):
    print(aveFilter.AvgFilter(i))

aveFilter.ResetAvgFilter()
print()

for i in range (0,10000):
    val = testGenerator.GetRandomAroundFixedValue()
    aveFilter.AvgFilter(val)

print(aveFilter.prevAvg)

print("*****MovAve*****")

for i in range(0,100):
    print(movAve.MovAvgFilter(i))

print()

movAve.ResetMovAveFilter()
print("*****MovAveReset*****")
for i in range(0,100):
    print(movAve.MovAvgFilter(i))

xVals = []
yValue = []
yLpf = []

for i in range (0,500):
    val = testGenerator.GetRandom(-30.0, 30.0) + i * i * 0.001
    lpfCurrent = lpf.LowPass1stOrderFilter(val)
    xVals.append(i)
    yValue.append(val)
    yLpf.append(lpfCurrent)

pyplot.plot(xVals, yValue, 'b-', xVals, yLpf, 'r-')
pyplot.show()
