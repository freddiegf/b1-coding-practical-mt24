
class PDController:
    def __init__(self, kp, kd):
        """
        Initialize the PD Controller with given gains.
        
        :param kp: Proportional gain
        :param kd: Derivative gain
        """
        self.kp = kp
        self.kd = kd
        self.previous_error = 0

    def compute(self, setpoint, measured_value):
        """
        Compute the control signal based on the setpoint and measured value.
        
        :param setpoint: Desired target value
        :param measured_value: Current measured value
        :return: Control signal
        """
        error = setpoint - measured_value
        derivative = (error - self.previous_error)
        output = self.kp * error + self.kd * derivative
        self.previous_error = error
        return output