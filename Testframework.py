# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:46:35 2019

@author: Sanskriti
"""
import numpy as np
import satellite
import MEKFmaincode
import testfunction
control_step=1
model_step=1
Advitiy = satellite.Satellite(v_state0,t0) 
Advitiy.setMag_i(np.array([1,1,1]))
Advitiy.setMag_b_m_c(np.array([1,1,1]))
Advitiy.setPos(np.array([1,1,1]))
Advitiy.setVel(np.array([1,2,1]))
v_state0 = np.hstack((v_q0_BO,v_w0_BOB))
print("v_state0")
print(v_state0)                         

#Make satellite object
init=1
end=7
k=0
t0=0
m_sgp_output = np.genfromtxt('sgp_output.csv', delimiter=",")
m_magnetic_field_i = np.genfromtxt('mag_output_i_test.csv',delimiter=",") 
#Advitiy = satellite.Satellite(v_state0,t0) 
position=np.zeros((end,3))
velocity=np.zeros((end,3))
q=np.zeros((end,4))
p=np.zeros((end,6,6))
x=np.zeros((end,6))
for i in range(end):
    Advitiy.setMag_i(m_magnetic_field_i[i,1:4])
    Advitiy.setMag_b_m_c(m_magnetic_field_i[i,1:4])
    Advitiy.setPos(m_sgp_output[i,1:4])
    Advitiy.setVel(m_sgp_output[i,4:7])
    position[i]=Advitiy.getPos()
    velocity[i]=Advitiy.getVel()
    print(position)
    print(velocity)    
    q[i,:], p[i :], x[i :]=MEKFmaincode.estimator(Advitiy)
print("q")    
print(q) 
print("p")
print(p)
print("x")
print(x)   
