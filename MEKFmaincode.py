# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:14:38 2019

@author: Sanskriti
"""

import testfunction
import scipy
from scipy.linalg import expm
import numpy as np
import qnv
from satellite import Satellite as sat
import constants_1U



def estimator(sat):
    w_m_k=sat.getW_BI_b(sat)
    w_oio=-v_w_IO_o
    delta_b=testfunction.delta_b_calc(b,b_e)
    w_bob=testfunction.w_bob_calc(w_m_k,q_kk,w_oio,b_e)
    phi=testfunction.phi_calc(w_bob)
    delta_x=testfunction.delta_x_calc(q_kk,delta_b)
    q_k1k=testfunction.propogate_quaternion(w_bob,q_kk)
    x_k1k=testfunction.propogate_state_vector(phi,delta_x)
    P_k1k=testfunction.propogate_covariance(phi,P_k)
    v_mag_b_e=testfunction.calc_v_mag_b_e(v_mag_b_m,v_mag_o,q_k1k)
    y=testfunction.calc_y(v_mag_b_m,v_mag_b_e)
    M_m=testfunction.calc_M_m(v_mag_b_e,q_k1k)
    K=testfunction.calc_K(P_k1k,M_m,R)
    q_k1k1=testfunction.update_quaternion(phi,delta_x_k1k,q_kk)
    x_k1k1=testfunction.update_state_vector(K,y,x_k1k,M_m)
    P_k1k1=testfunction.update_covariance(I6,K,M_m,P_k1k)
    
    

print(estimator(sat))



    