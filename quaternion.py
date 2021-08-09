# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:02:43 2021

@author: DOLPHIN
"""

def quaternion_matrix(q):
  """Return homogeneous rotation matrix from quaternion.
  """
  qw = q[0]
  qx = q[1]
  qy = q[2]
  qz = q[3]

  return np.array([
      [1-2*qy*qy - 2*qz*qz,       2*qx*qy - 2*qz*qw,        2*qx*qz + 2*qy*qw],
      [2*qx*qy + 2*qz*qw    ,     1-2*qx*qx - 2*qz*qz,      2*qy*qz - 2*qx*qw],
      [2*qx*qz - 2*qy*qw    ,     2*qy*qz + 2*qx*qw,        1-2*qx*qx - 2*qy*qy],
      ])

def matrix_quaternion(R):  
  trace = np.trace(R)
  if trace > 0:
    s = 0.5 / np.sqrt(trace+1.0)
    qw = 0.25 / s 
    qx = (R[2,1]-R[1,2])*s
    qy = (R[0,2]-R[2,0])*s
    qz = (R[1,0]-R[0,1])*s
  else:
    if ( R[0,0] > R[1,1] and R[0,0] > R[2,2] ):
      s = 2.0 * np.sqrt( 1.0 + R[0,0] - R[1,1] - R[2,2])
      qw = (R[2,1] - R[1,2]) / s
      qx = 0.25 * s
      qy = (R[0,1] + R[1,0]) / s
      qz = (R[0,2] + R[2,0]) / s
    elif (R[1,1] > R[2,2]):
      s = 2.0 * np.sqrt( 1.0 + R[1,1] - R[0,0] - R[2,2])
      qw = (R[0,2] - R[2,0] ) / s
      qx = (R[0,1] + R[1,0] ) / s
      qy = 0.25 * s
      qz = (R[1,2] + R[2,1] ) / s
    else:
      s = 2.0 * np.sqrt( 1.0 + R[2,2] - R[0,0] - R[1,1] )
      qw = (R[1,0] - R[0,1] ) / s
      qx = (R[0,2] + R[2,0] ) / s
      qy = (R[1,2] + R[2,1] ) / s
      qz = 0.25 * s
  
  return np.array([qw,qx,qy,qz])
