import random

class TestValueGenerator:
    """Creates test values for Kalman filter function tests"""

    def __init__(self):
        None             

    def GetRandomAroundFixedValue(self, fixedValue = 0):
        """Return a noisy number"""
        rand = random.uniform(-1.0, 1.0)
        return  rand + fixedValue


