
# -*- coding: utf8-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy.linalg import expm
import numpy as np
import qnv
import satellite 
I3=np.matrix('1,0,0;0,1,0;0,0,1') #defining 3x3 identity matrix 
I4=np.matrix('1,0,0,0;0,1,0,0;0,0,1,0;0,0,0,1') #defining 4x4 identity matrix
P_k=np.matrix('[1,0,0],[0,1,0],[0,0,1]') #initial state covariance matrix
q_(k|k)=np.matrix('0,0,0,1')
delta_b=b-b_e #delta b, diffence between gyro bias and estimated bias
w_bib=w_m_k-b_e #estimated omega
w_bob=w_bib-w_oio*(qnv.quat2rotm(q_(k|k)))
delta_theta=q_(k|k)[0:3]/q_(k|k)[3] #vector part of error quaternion normalised such that scalar part is equated to 1
delta_x=np.array([delta_theta[0],delta_theta[1],delta_theta[2],delta_b[0],delta_b[1],delta_b[2]])  #error state vector 
A=I3-qnv.skew(w_bob)
B=-I3
t=1
C=np.matrix([[A[0,0],A[0,1],A[0,2],B[0,0],B[0,1],B[0,2]],[A[1,0],A[1,1],A[1,2],B[1,0],B[1,1],B[1,2]],[A[2,0],A[2,1],A[2,2],B[2,0],B[2,1],B[2,2]],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
Q_k=np.matrix([sigma_r_sq,0,0,0,0,0],[0,sigma_r_sq,0,0,0,0],[0,0,sigma_r_sq,0,0,0],[0,0,0,sigma_w_sq,0,0],[0,0,0,0,sigma_w_sq,0],[0,0,0,0,0,sigma_w_sq])
phi=np.linal.matrix_power(scipy.linalg.expm(A),t)  
                                
def propogate_quaternion(w_bob,q_(k|k),t):
    
    
    return 
def propogate_state_vector(phi,delta_x):
    return phi*delta_x
def propogate_covariance(phi,Q_k,P_k):
    return phi*P_k*(phi.T)+Q_k

v_mag_b_m=sat.getMag_b_m_c()  
v_mag_o=sat.getMag_o()
y=v_mag_b_m-v_mag_o
v_mag_b_e=v_mag_o*(qnv.quat2rotm(q_(k+1|k))
D=qnv.skew(v_mag_b_e)
R=I3
K=P_(k+1|k)*D.T*(D*P_(k+1|k)*D.T+R).I 
   
def update_quaternion(phi,delta_x,q_(k|k)):
    delta_q=(delta_x[0:3],0)
    return qnv.quatMultiplyNorm(delta_q,q_(k|k))

def update_state_vector(K,y,x_(k+1|k)):
    return x_(k+1|k)+K*(y-x_(k+1|k))

def update_covariance(I3,K,D,P_(k+1|k)):
    return (I3-K*D)*P_(k+1|k)
 
    
