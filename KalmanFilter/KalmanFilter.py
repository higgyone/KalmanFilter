from TestValueGenerator import TestValueGenerator
from AveFilter import AveFilter
from MovingAverage import MovingAverage

testGenerator = TestValueGenerator()
aveFilter = AveFilter()
movAve = MovingAverage(5)

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
