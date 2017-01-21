class MovingAverage(object):
    """Calculates the moving average"""

    def __init__(self, movingAveCount = 10):
        """initialise the class and set the initial moveing average count
        
        Parameters
        ----------
        movingAverageCount : int
            number of values to take an averge of, must be an int"""
        self.movAveCount = 10
        self.movAveList = []

        self.ResetMovAveFilter(movingAveCount);
        

    def SetMovingAverageCount(self, count):
        """set the number of values to use in the running average
        
        Parameters
        ----------
        count : int
            numer of values to take the average of
            
        Returns
        -------
        None"""
        value = int(count)

        """set it to the value if it is int of 1 or more to make it work
        Otherwise keep it as it was if duff value"""
        if value > 0:
            self.movAveCount = value


    def ResetMovAveFilter(self, movingAveCount = 10):
        """Reset the moving average filter

        Parameters
        ----------
        movingAveCount : int
            moving average count

        Returns
        -------
        None"""

        self.SetMovingAverageCount(movingAveCount)

        """Reset the list"""
        self.movAveList = [0] * self.movAveCount

    def MovAvgFilter(self, value):
        """Add the next value to the filter and return the current moving average

        Parameters
        ----------
        value : numebr type
            number to add to the filter

        Returns
        -------
        float
            Current moving average"""

        for i in range(0,self.movAveCount - 1):
           self.movAveList[i] = self.movAveList[i+1]

        self.movAveList[self.movAveCount - 1] = value

        total = sum(self.movAveList)

        movAve = total/float(self.movAveCount)

        return movAve


