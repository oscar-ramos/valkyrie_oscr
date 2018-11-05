# -*- coding: utf-8 -*-

#
# Plots for Valkyrie
#

from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt


folder = '../../data/'
prefix = 'motion_acrob_'

# Read the files
path = folder + prefix
q = np.loadtxt(path+'q.txt')
xl     = np.loadtxt(path+"LHand.txt")
xldes  = np.loadtxt(path+"LHand_des.txt")
xr     = np.loadtxt(path+"RHand.txt")
xrdes  = np.loadtxt(path+"RHand_des.txt")
xb     = np.loadtxt(path+"Base.txt")
xbdes  = np.loadtxt(path+"Base_des.txt")
xlf     = np.loadtxt(path+"LFoot.txt")
xlfdes  = np.loadtxt(path+"LFoot_des.txt")
xlfdes2  = np.loadtxt(path+"LFootPosition_des.txt")
stime = np.loadtxt(path+"time.txt")

# Set the plotting times
tf = 6000
q = q[:tf,:];
time = stime[:tf]
xl = xl[:tf,:]; xldes = xldes[:tf,:]; xr = xr[:tf,:]; xrdes = xrdes[:tf,:]; 
xb = xb[:tf,:]; xbdes = xbdes[:tf,:]; xlf = xlf[:tf,:];

# Plot the temporal joint configuration
plt.plot(q[:,0], q[:,8:])
plt.xlabel('tiempo [s]')
plt.ylabel('Valor articular [rad]')
plt.title('Evolución articular en el tiempo')
# plt.legend((r'$q_1$', r'$q_2$', r'$q_3$', r'$q_4$', r'$q_5$', r'$q_6$', r'$q_7$'), loc='best')
plt.grid()
plt.show()

# ---------------------
# Right Hand
# ---------------------
plt.subplot(121)
plt.plot(xr[:,0], xr[:,1], linewidth=2)
plt.plot(xr[:,0], xr[:,2], linewidth=2)
plt.plot(xr[:,0], xr[:,3], linewidth=2)
plt.plot(xrdes[0:3580,0], xrdes[0:3580,1:4],'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('posición [m]')
plt.title("Posición de la mano derecha")
plt.legend(('x', 'y', 'z'), loc='best')
plt.xlim(right=60)
plt.grid()
#plt.show()
# ---------------------
# Left Hand
# ---------------------
plt.subplot(122)
plt.plot(xl[:,0], xl[:,1], linewidth=2)
plt.plot(xl[:,0], xl[:,2], linewidth=2)
plt.plot(xl[:,0], xl[:,3], linewidth=2)
plt.plot(xldes[0:3580,0], xldes[0:3580,1:4],'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('posición [m]')
plt.title("Posición de la mano izquierda")
plt.legend(('x', 'y', 'z'), loc='best')
plt.xlim(right=60)
#plt.axis('equal')
plt.grid()
plt.show()


# ---------------------
# Base
# ---------------------
plt.subplot(121)
plt.plot(xb[:,0], xb[:,1], linewidth=2)
plt.plot(xb[:,0], xb[:,2], linewidth=2)
# plt.plot(xb[:,0], xb[:,3], linewidth=2)
plt.plot(xbdes[0:3580,0], xbdes[0:3580,1:3],'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('posición [m]')
plt.title("Posición de la pelvis")
plt.legend(('x', 'y'), loc='best')
plt.xlim(right=60)
plt.grid()
#plt.show()
# ---------------------
# Left Foot
# ---------------------
plt.subplot(122)
plt.plot(xlf[:,0], xlf[:,1], linewidth=2)
plt.plot(xlf[:,0], xlf[:,2], linewidth=2)
plt.plot(xlf[:,0], xlf[:,3], linewidth=2)
plt.plot(xlfdes[0:498,0], xlfdes[0:498,1:4],'k--')
plt.plot(xlfdes[4079:,0], xlfdes[4079:,1:4],'k--')
plt.plot(xlfdes2[:3580,0], xlfdes2[:3580,1:4],'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('posición [m]')
plt.title("Posición del pie izquierdo")
plt.legend(('x', 'y', 'z'), loc='best')
plt.xlim(right=60)
#plt.axis('equal')
plt.grid()
plt.show()


# Plot computation time
if (False):
    plt.plot(time)
    plt.xlabel('iteración')
    plt.ylabel('tiempo [ms]')
    plt.title('Tiempo de cálculo')
    plt.grid()
    plt.show()
