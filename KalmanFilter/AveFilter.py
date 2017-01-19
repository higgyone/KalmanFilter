class AveFilter():
    """Average filter"""

    #prevAvg = 0
   # k = 1
    def __init__(self):
        self.k = 1
        self.prevAvg = 0


    def AvgFilter(self, data):
        #global k
        #global prevAvg

        alpha = (self.k-1)/self.k
        avg = alpha*self.prevAvg + (1-alpha)*data

        self.prevAvg = avg
        self.k = self.k + 1

        return avg

    def ResetAvgFilter(self):
        #global k
        #global prevAvg
        self.k = 1
        self.prevAvg = 0