import numpy as np
from corcondia import corcondia_3d

def test_corcondia_3d_runs():
    T = np.random.rand(50, 60, 70)
    corcondia_3d(T, k=5)
    T = np.random.rand(60, 50, 70)
    corcondia_3d(T, k=6)
    T = np.random.rand(70, 50, 60)
    corcondia_3d(T, k=4)
