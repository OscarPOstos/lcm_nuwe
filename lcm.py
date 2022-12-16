import numpy as np


def lcm_range_from_1_to_number(number):
    return np.lcm.reduce(np.arange(1, number + 1))


print(lcm_range_from_1_to_number(20))
