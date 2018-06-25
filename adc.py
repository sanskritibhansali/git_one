import numpy as np
#x=float(input())
#y=float(input())
#z=float(input())
#sun_vector=np.array([x,y,z])
#print(sun_vector)
SS_GAIN=3.3 #gain factor as the readings from sunsensor are in voltage.
SS_QUANTIZER=pow(2,10)-1  #because we have 10 bit adc
MAX_ANGLE=55            #taken from pratham's simulink model,can be adjusted, it is the 1/2 of threshold value of angle which will be taken in FOV
v_S1=np.array([1,0,0])   #vectors perpendicular to sensors.
v_S2=np.array([-1,0,0])
v_S3=np.array([0,1,0])
v_S4=np.array([0,-1,0])
v_S5=np.array([0,0,1])
v_S6=np.array([0,0,-1])
def ad_convertor(sun_vector,v_S1,v_S2,v_S3,v_S4,v_S5,v_S6,SS_GAIN,SS_QUANTIZER):    #works as adc convertor, quantizes the readings of sensor
        u=1/(SS_QUANTIZER-1)                                                          #for more you can refer to documentation of this code.
        #print(u)
        ss1=np.dot(sun_vector,v_S1)
        if ss1<0:
            ss1=0    
        ss1=(u)*(round(ss1/u))*SS_GAIN
        #print(ss1)
        ss2=(np.dot(sun_vector,v_S2))
        if ss2<0:
            ss2=0    
        ss2=(u)*(round(ss2/u))*SS_GAIN
        ss3=(np.dot(sun_vector,v_S3))
        if ss3<0:
            ss3=0    
        ss3=(u)*(round(ss3/u))*SS_GAIN
        ss4=(np.dot(sun_vector,v_S4))
        if ss4<0:
            ss4=0    
        ss4=(u)*(round(ss4/u))*SS_GAIN
        ss5=(np.dot(sun_vector,v_S5))
        if ss5<0:
            ss5=0    
        ss5=(u)*(round(ss5/u))*SS_GAIN
        ss6=(np.dot(sun_vector,v_S6))
        if ss6<0:
            ss6=0    
        ss6=(u)*(round(ss6/u))*SS_GAIN
        return np.array([ss1,ss2,ss3,ss4,ss5,ss6])                            #stores quantized values of all readings.
print(ad_convertor(sun_vector,v_S1,v_S2,v_S3,v_S4,v_S5,v_S6,SS_GAIN,SS_QUANTIZER))
ss=ad_convertor(sun_vector,v_S1,v_S2,v_S3,v_S4,v_S5,v_S6,SS_GAIN,SS_QUANTIZER)          
a=np.cos(MAX_ANGLE*np.pi/180)*SS_GAIN
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
      return v_sun_m/mode        #gives the unit sun vector to be used in quest.    
print(calc_sv(ss,dark,light))
               
        
            
   