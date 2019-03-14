# speedcontrol.py

# author: awakenedhaki

import numpy as np

from typing import List

def gps(s, x):
    if len(x) < 2:
        return 0
    x = np.array(x)
    delta_distances = x[1:] - x[:-1]
    speeds = np.floor((delta_distances * 3600) / s)
    return np.max(speeds)
