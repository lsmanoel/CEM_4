import pandas as pd

url_elc_plane_bottom_24_MHz = 'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20%20plane_bottom_24_MHz.csv'
url_elc_plane_bottom_500_KHz = 'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20plane_bottom_500_KHz.csv'
url_elc_plane_top_24_MHz = 'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20plane_top_24_MHz.csv'
url_elc_plane_top_500_KHz = 'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20plane_top_500_KHz.csv'
url_mag_plane_bottom_24_MHz = 'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20mag_plane_bottom_24_MHz.csv'
url_mag_plane_top_24_MHz = 'https://raw.githubusercontent.com/lsmanoel/CEM_4/master/13.06/placaL_medidas%20-%20mag_plane_top_24_MHz.csv'

columns_name = ['A','B','C','D','E','F','G','H','I','J','K','L','M']

pd_elc_plane_bottom_24_MHz = pd.read_csv(url_elc_plane_bottom_24_MHz, names=columns_name)
pd_elc_plane_bottom_500_KHz = pd.read_csv(url_elc_plane_bottom_500_KHz, names=columns_name)
pd_elc_plane_top_24_MHz = pd.read_csv(url_elc_plane_top_24_MHz, names=columns_name)
pd_elc_plane_top_500_KHz = pd.read_csv(url_elc_plane_top_500_KHz, names=columns_name)
pd_mag_plane_bottom_24_MHz = pd.read_csv(url_mag_plane_bottom_24_MHz, names=columns_name)
pd_mag_plane_top_24_MHz = pd.read_csv(url_mag_plane_top_24_MHz, names=columns_name)

elc_plane_bottom_24_MHz = pd_elc_plane_bottom_24_MHz.values
elc_plane_bottom_500_KHz = pd_elc_plane_bottom_500_KHz.values
elc_plane_top_24_MHz = pd_elc_plane_top_24_MHz.values
elc_plane_top_500_KHz = pd_elc_plane_top_500_KHz.values
mag_plane_bottom_24_MHz = pd_mag_plane_bottom_24_MHz.values
mag_plane_top_24_MHz = pd_mag_plane_top_24_MHz.values

elc_plane_bottom_24_MHz = -elc_plane_bottom_24_MHz
elc_plane_bottom_500_KHz = -elc_plane_bottom_500_KHz
elc_plane_top_24_MHz = -elc_plane_top_24_MHz
elc_plane_top_500_KHz = -elc_plane_top_500_KHz
mag_plane_bottom_24_MHz = -mag_plane_bottom_24_MHz
mag_plane_top_24_MHz = -mag_plane_top_24_MHz

input_plane = elc_plane_bottom_24_MHz

# ==============================================================================
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from scipy import interpolate

# ==============================================================================
fig = plt.figure(figsize=plt.figaspect(0.25))

# ==============================================================================
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_title('Interpolated')

X = np.arange(0, 13, 1)
Y = np.arange(0, 13, 1)
X, Y = np.meshgrid(X, Y)

Z = input_plane

# ------------------------------------------------------------------------------
# Interpolation
tck = interpolate.bisplrep(X, Y, Z, s=250)

ratio = 10

X_interp = np.arange(0, 13, 1/ratio)
Y_interp = np.arange(0, 13, 1/ratio)

X_interp, Y_interp = np.mgrid[0:13:ratio*13j, 0:13:ratio*13j]

Z_interp = interpolate.bisplev(X_interp[:,0], Y_interp[0,:], tck)
    
surf = ax.plot_surface(X_interp, Y_interp, Z_interp, 
                       rstride=1, 
                       cstride=1, 
                       cmap ='inferno',
                       linewidth=0, 
                       antialiased=True,
                       vmax = 0,
                       vmin = -80)

fig.colorbar(surf, shrink=0.5, aspect=10)
ax.set_zlim(-80, 0)

angle_view = 120
ax.view_init(60, angle_view)

# ==============================================================================
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.set_title('No Interpolated')

X = np.arange(0, 13, 1)
Y = np.arange(0, 13, 1)
X, Y = np.meshgrid(X, Y)
Z = input_plane

surf = ax.plot_surface(X, Y, Z, 
                       rstride=1, 
                       cstride=1, 
                       cmap ='inferno',
                       linewidth=0, 
                       antialiased=True,
                       vmax = 0,
                       vmin = -80)

fig.colorbar(surf, shrink=0.5, aspect=10)
ax.set_zlim(-80, 0)

angle_view = 120
ax.view_init(60, angle_view)

# ==============================================================================
plt.show()