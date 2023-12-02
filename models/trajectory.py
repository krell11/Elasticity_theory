class Trajectory:
    def __init__(self, coefficients: [], *task_type):
        self.coefficients = coefficients

        if len(coefficients) != 3:
            self.coefficients[2] = 0

    def get_velocity(self):
        pass
