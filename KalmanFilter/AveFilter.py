class AveFilter():
    """Average filter"""

    def __init__(self):
        self.k = 1
        self.prevAvg = 0


    def AvgFilter(self, number):
        """Calculates the running average and returns is
        
        Parameters
        ----------
        number : number
             next number to add to the collectoin to get the average of
             
        Returns
        -------
        current running average"""

        alpha = (self.k-1)/self.k
        avg = alpha*self.prevAvg + (1-alpha)*number

        self.prevAvg = avg
        self.k = self.k + 1

        return avg

    def ResetAvgFilter(self):
        """Resets the average filter for new run
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.k = 1
        self.prevAvg = 0