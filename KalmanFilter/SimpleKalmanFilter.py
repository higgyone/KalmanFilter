class SimpleKalmanFilter(object):
    """Simple kalman filter with constant value"""

    def __init__(self):
        """set up the initial values"""

        # Kalman fixed values for simple model~
        self.A = 1
        self.H = 1
        self.Q = 0
        self.R = 4

        #computation of estimate
        self.x = 0
        #computation of error covariance
        self.p = 0
        # prediction of estimate
        self.xp = 0
        #prediction of error covariance
        self.pp = 0
        #computation of Kalman gain
        self.K = 0

    def SetInitalXandP(self, x=0.0, p=0.0):
        """ set the initial estimate and error covariance
        
        Parameters
        ----------
        x : float
            initial estimate
        p : float
            initial covariance"""
        self.x = x
        self.p = p

    def SetAHQR(self, a, h, q, r):
        """ set the AHQ&R values

        Parameters
        ----------
        A : float
            state transition from previous to new estimate (system model)
        H : float
            system model state transition for state to measurement
        Q : float
            covariance (i.e. noise) added to A's state variable prediction to get x
         R : float
            covariance (i.e. noise) added to H's state to measurement to get z""" 
        self.A = a
        self.H = h
        self.Q = q
        self.R = r

    def SimpleKalman(self, z):
        """ calculate the kalman result from the measurement z
        
        Parameters
        ----------
        z : float
            measurement

        Returns
        -------
        x : float
            prediction of the state"""
        self.xp = self.A * self.x

        # second self.A should be transopsed, but is the same value in a 1D array
        self.pp = self.A * self.p * self.A + self.Q

        # again first and third H should be transposed but same value in 1D array after transposition
        self.K = (self.pp * self.H) / (self.H * self.pp * self.H + self.R)

        self.x = self.xp + self.K * (z - self.H * self.xp)
        self.p = self.pp - self.K * self.H * self.pp

        return self.x