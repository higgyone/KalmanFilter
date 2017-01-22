class LowPassFilter1st(object):
    """Low pass first order filter for noise reduction"""

    def __init__(self, alpha = 0.7):
        """setup the previous x value store and set it to 0
        
        Parameters
        ----------
        alpha : float
            alpha value for the filter between 0 & 1"""

        self.prevX = 0.0
        self.alpha = 0.7

        self.ResetFilter(alpha)


    def ResetFilter(self, alpha):
        """Reset the values to 0 for new data set
        
        Parameters
        ----------
        alpha : float
            positive alpha value for the filter between 0.0 & 1.0"""
       
        self.prevX = 0.0

        alp = float(self.alpha)

        if alp < 0.0:
            self.alpha = 0.0
        elif alp > 1.0:
            self.alpha = 1.0
        else:
            self.alpha = alp

    

    def LowPass1stOrderFilter(self, value):
        """Run the low pass first order filter and add the new value

        Parameters
        ----------
        value : number type
            Add the value to the filter

        Return
        ------
        float
            current first order filter value"""

        xlpf = self.alpha * self.prevX + (1 - self.alpha) * value
        self.prevX = xlpf
        return self.prevX



