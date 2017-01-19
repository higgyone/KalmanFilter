from TestValueGenerator import TestValueGenerator
from AveFilter import AveFilter

testGenerator = TestValueGenerator()
aveFilter = AveFilter()

for i in range (0,9):
    print(aveFilter.AvgFilter(i))

aveFilter.ResetAvgFilter()
print()

for i in range (0,10000):
    val = testGenerator.GetRandomAroundFixedValue()
    aveFilter.AvgFilter(val)

print(aveFilter.prevAvg)


