import math

class BiquadIIRFilter:
    """
    Direct Form II Transposed Biquad IIR Filter.
    Supports lowpass filter coefficients.
    H(z) = (b0 + b1*z^-1 + b2*z^-2) / (1 + a1*z^-1 + a2*z^-2)
    """
    def __init__(self, cutoff_ratio=0.1):
        theta = math.pi * cutoff_ratio
        sn = math.sin(theta)
        cs = math.cos(theta)
        alpha = sn / math.sqrt(2)
        a0 = 1.0 + alpha
        self.b0 = ((1.0 - cs) / 2.0) / a0
        self.b1 = (1.0 - cs) / a0
        self.b2 = ((1.0 - cs) / 2.0) / a0
        self.a1 = (-2.0 * cs) / a0
        self.a2 = (1.0 - alpha) / a0
        self.s1 = 0.0
        self.s2 = 0.0

    def process_sample(self, x):
        y = self.b0 * x + self.s1
        self.s1 = self.b1 * x - self.a1 * y + self.s2
        self.s2 = self.b2 * x - self.a2 * y
        return y
