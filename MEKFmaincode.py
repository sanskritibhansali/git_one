# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:14:38 2019

@author: Sanskriti
"""

from constants_1U import *
import testfunction
import scipy
from scipy.linalg import expm
import numpy as np
import qnv
import satellite


v_state0 = np.hstack((v_q0_BO,v_w0_BOB))
print("v_state0")
print(v_state0)                         
t0 = 0
#Make satellite object
Advitiy = satellite.Satellite(v_state0,t0) 
Advitiy.setMag_i(np.array([1,1,1]))
Advitiy.setMag_b_m_c(np.array([1,1,1]))
#Advitiy.setMag_o(np.array([1,2,1]))
  #t0 from line 42 of main_code

b=np.array([1,1,1]) #bias
b_e=np.array([0,0,0]) #estimated bias
#I3=np.matrix('1,0,0;0,1,0;0,0,1') #defining 3x3 identity matrix 
#I4=np.matrix('1,0,0,0;0,1,0,0;0,0,1,0;0,0,0,1') #defining 4x4 identity matrix
#I6=np.matrix('1,0,0,0,0,0;0,1,0,0,0,0;0,0,1,0,0,0;0,0,0,1,0,0;0,0,0,0,1,0;0,0,0,0,0,1')
#P_k=np.matrix('1,0,0,0,0,0;0,1,0,0,0,0;0,0,1,0,0,0;0,0,0,1,0,0;0,0,0,0,1,0;0,0,0,0,0,1') #initial state covariance matrix
q_kk=np.array([0,0,0,1])
#R=I3
#v_mag_o=Advitiy.getMag_o()
#v_mag_o=sat.getMag_o()
#v_mag_b_m=Advitiy.getMag_b_m_c()

def estimator(sat):
    v_mag_o=Advitiy.getMag_o()
    v_mag_b_m=Advitiy.getMag_b_m_c()
    w_m_k=sat.getW_BI_b()
    w_oio=-v_w_IO_o
    delta_b=testfunction.delta_b_calc(b,b_e)
    w_bob=testfunction.w_bob_calc(w_m_k,q_kk,w_oio,b_e)
    #print(w_bob)
    phi=testfunction.phi_calc(w_bob)
    #print(phi)
    delta_x=testfunction.delta_x_calc(q_kk,delta_b)
    #print(delta_x)
    q_k1k=testfunction.propogate_quaternion(w_bob,q_kk)
    #print(q_k1k)
    x_k1k=testfunction.propogate_state_vector(phi,delta_x)
    #print(x_k1k)
    P_k1k=testfunction.propogate_covariance(phi,P_k)
    #print(P_k1k)
    v_mag_b_e=testfunction.calc_v_mag_b_e(v_mag_b_m,v_mag_o,q_k1k)
    #print(v_mag_b_e)
    y=testfunction.calc_y(v_mag_b_m,v_mag_b_e)
    #print(y)
    M_m=testfunction.calc_M_m(v_mag_b_e,q_k1k)
    #print(M_m)
    K=testfunction.calc_K(P_k1k,M_m,R)
    #print("K=")
    #print(K)   
    x_k1k1=testfunction.update_state_vector(K,y,x_k1k,M_m)
    #print("x=" )
    #print(x_k1k1)
    P_k1k1=testfunction.update_covariance(I6,K,M_m,P_k1k)
    #print("p=")
    #print(P_k1k1)
    q_k1k1=testfunction.update_quaternion(phi,x_k1k,q_kk)
    #print("qk1k1")
    print(q_k1k1)
    return q_k1k1
    
print("result")
print(estimator(Advitiy))



    