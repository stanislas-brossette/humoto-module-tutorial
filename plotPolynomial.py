import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
time = np.array([   10, 10.01, 10.02, 10.03, 10.04, 10.05, 10.05, 10.06, 10.07, 10.08, 10.09,  10.1, 10.11, 10.12, 10.13, 10.14, 10.15, 10.15, 10.16, 10.17, 10.18, 10.19,  10.2, 10.21, 10.22, 10.23, 10.24, 10.25, 10.25, 10.26, 10.27, 10.28, 10.29,  10.3, 10.31, 10.32, 10.33, 10.34, 10.35, 10.35, 10.36, 10.37, 10.38, 10.39,  10.4, 10.41, 10.42, 10.43, 10.44, 10.45, 10.45, 10.46, 10.47, 10.48, 10.49,  10.5, 10.51, 10.52, 10.53, 10.54, 10.55, 10.55, 10.56, 10.57, 10.58, 10.59,  10.6, 10.61, 10.62, 10.63, 10.64, 10.65, 10.65, 10.66, 10.67, 10.68, 10.69,  10.7, 10.71, 10.72, 10.73, 10.74, 10.75, 10.75, 10.76, 10.77, 10.78, 10.79,  10.8, 10.81, 10.82, 10.83, 10.84, 10.85, 10.85, 10.86, 10.87, 10.88, 10.89,  10.9])
trajX = np.array([-140.9, -138.2, -135.5, -132.8, -130.2, -127.6,   -125, -122.5, -120.1, -117.6, -115.2, -112.9, -110.6, -108.3,   -106, -103.8, -101.7, -99.54, -97.44, -95.37, -93.34, -91.34, -89.38, -87.45, -85.55, -83.68, -81.85, -80.05, -78.27, -76.53, -74.82, -73.14, -71.48, -69.86, -68.26, -66.69, -65.15, -63.64, -62.16,  -60.7, -59.26, -57.86, -56.48, -55.12, -53.79, -52.49,  -51.2, -49.95, -48.71,  -47.5, -46.31, -45.15, -44.01, -42.88, -41.79, -40.71, -39.65, -38.62,  -37.6,  -36.6, -35.63, -34.67, -33.74, -32.82, -31.92, -31.04, -30.18, -29.33, -28.51,  -27.7,  -26.9, -26.13, -25.37, -24.63,  -23.9, -23.19, -22.49, -21.81, -21.15,  -20.5, -19.86, -19.24, -18.63, -18.04, -17.46, -16.89, -16.34,  -15.8, -15.27, -14.76, -14.25, -13.76, -13.28, -12.81, -12.36, -11.91, -11.48, -11.05, -10.64, -10.24])
trajY = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
trajZ = np.array([ -8199,  -8011,  -7828,  -7647,  -7470,  -7297,  -7127,  -6960,  -6796,  -6636,  -6479,  -6324,  -6173,  -6025,  -5880,  -5738,  -5598,  -5462,  -5328,  -5197,  -5068,  -4942,  -4819,  -4699,  -4580,  -4465,  -4351,  -4241,  -4132,  -4026,  -3922,  -3820,  -3721,  -3623,  -3528,  -3435,  -3344,  -3254,  -3167,  -3082,  -2999,  -2917,  -2838,  -2760,  -2684,  -2609,  -2537,  -2466,  -2396,  -2329,  -2263,  -2198,  -2135,  -2074,  -2014,  -1955,  -1898,  -1842,  -1787,  -1734,  -1682,  -1632,  -1583,  -1535,  -1488,  -1442,  -1398,  -1354,  -1312,  -1271,  -1231,  -1192,  -1154,  -1117,  -1081,  -1046,  -1011, -978.3,   -946, -914.5,   -884, -854.3, -825.4, -797.3,   -770, -743.5, -717.7, -692.7, -668.3, -644.7, -621.8, -599.6,   -578,   -557, -536.7,   -517, -497.9, -479.4, -461.4,   -444])
plt.plot(time, trajX, 'r', label='X')
plt.plot(time, trajY, 'g', label='Y')
plt.plot(time, trajZ, 'b', label='Z')
plt.legend()
plt.show()
