import numpy as np
sun_vector=np.array([input()])
SS_GAIN=3.3 #gain factor as the readings from sunsensor are in voltage.
SS_QUANTIZER=pow(2,10)  #because we have 10 bit adc
MAX_ANGLE=55            #taken from pratham's simulink model,can be adjusted, it is the 1/2 of threshold value of angle which will be taken in FOV
v_S1=np.array([1,0,0])   #vectors perpendicular to sensors.
v_S2=np.array([-1,0,0])
v_S3=np.array([0,1,0])
v_S4=np.array([0,-1,0])
v_S5=np.array([0,0,1])
v_S6=np.array([0,0,-1])
ss=np.array([0,0,0,0,0,0])
def ad_convertor(sun_vector,v_S1,v_S2,v_S3,v_S4,v_S5,v_S6,SS_GAIN,SS_QUANTIZER):    #works as adc convertor, quantizes the readings of sensor
        u=1/SS_QUANTIZER                                                            #for more you can refer to documentation of this code.
        ss[0]=(np.dot(sun_vector,v_S1))
        if ss[0]<0:
            ss[0]=0    
        ss[0]=(u)*(round(ss[0]/u))*SS_GAIN
        ss[1]=(np.dot(sun_vector,v_S2))
        if ss[1]<0:
            ss[1]=0    
        ss[1]=(u)*(round(ss[1]/u))*SS_GAIN
        ss[2]=(np.dot(sun_vector,v_S3))
        if ss[2]<0:
            ss[2]=0    
        ss[2]=(u)*(round(ss[2]/u))*SS_GAIN
        ss[3]=(np.dot(sun_vector,v_S4))
        if ss[3]<0:
            ss[3]=0    
        ss[3]=(u)*(round(ss[3]/u))*SS_GAIN
        ss[4]=(np.dot(sun_vector,v_S5))
        if ss[4]<0:
            ss[4]=0    
        ss[4]=(u)*(round(ss[4]/u))*SS_GAIN
        ss[5]=(np.dot(sun_vector,v_S6))
        if ss[5]<0:
            ss[5]=0    
        ss[5]=(u)*(round(ss[5]/u))*SS_GAIN
        return ss                            #stores quantized values of all readings.
ad_convertor(sun_vector,v_S1,v_S2,v_S3,v_S4,v_S5,v_S6,SS_GAIN,SS_QUANTIZER)           
a=np.cos(MAX_ANGLE*np.pi/180)
f=np.array([0,0,0,0,0,0])
def light(ss,a):                #calucates the flag value-light
    for i in range(6):
        if ss[i]>a:
            f[i]=1
        else:
            f[i]=0
        return f    
f=light(ss,a)            
#print(f)
#print(ss)
#from here code begins to back calculate sun vector from the model.
#this code has to be added in quest. 
dark=0
light=1
def calc_sv(ss,dark,light):
      v_sun_m=np.array([0,0,0])            
      for i in range(6):
           if ss[i]==0:
               dark=dark+1
      if dark==6:
          light=0
      if light==1:     
         for n in range(3):
                  m=n*2;
                  if ss[m]>=ss[m+1]:
                        v_sun_m[n]=1.0*ss[m]
                  else:
                     v_sun_m[n]=-1.0*ss[m+1]
      mode=pow((pow(v_sun_m[0],2)+pow(v_sun_m[1],2)+pow(v_sun_m[2],2)),0.5)                       
      v_sun_m=v_sun_m/mode        #gives the unit sun vector to be used in quest.    
#print(v_sun_m)
               
        
            
   