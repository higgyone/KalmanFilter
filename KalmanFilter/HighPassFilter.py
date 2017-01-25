class HighPassFilter(object):
    """Implements a high pass filter"""

    def __init__(self):
        """setup the initial values"""
        self.prevX = 0.0
        self.prevU = 0.0
        self.dt = 0.01

        # this works out to give an alpha of 0.7
        self.tau = 0.023


    def ResetFilter(self):
        """Reset the filter previous values to start again"""
        self.prevX = 0.0
        self.prevU = 0.0

    def SetAlpha(self, dt = 0.01, tau = 0.023):
        """set the weighting value alpha via dt and tau
        Where alpha = tau/(tau +dt)

        Parameters
        -----------
        dt : float
            change in time step
        tau : float
            time constant for the filter"""
        self.dt = dt
        self.tau = tau

    def HighPassFilter(self, u):
        """Run the recursive high pass filter with the new value

        Parameters
        ----------
        u : float
            next value to filter

        Returns
        -------
        xhpf : float
            the current value of the high pass filter"""
        alpha = self.tau / (self.tau + self.dt)
        xhpf = alpha * self.prevX + alpha * (u - self.prevU)
        self.prevX = xhpf
        self.prevU = u

        return xhpf






