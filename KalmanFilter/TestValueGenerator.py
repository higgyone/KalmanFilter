import random

class TestValueGenerator:
    """Creates test values for Kalman filter function tests"""

    def __init__(self):
        None             

    def GetRandomAroundFixedValue(self, fixedValue = 0):
        """Return a noisy number"""
        rand = random.uniform(-1.0, 1.0)
        return  rand + fixedValue

    def GetRandom(self, randMin = -1.0, randMax = 1.0):
        """Return a noisy number between specified limits"""
        rand = random.uniform(randMin, randMax)
        return  rand

    def GetRandomFixedvalueLimits(self, fixedValue = 0, multiplier = 1):
        """Return a noisy number between specified limits"""
        rand = self.GetRandom()
        return  rand * multiplier  + fixedValue



