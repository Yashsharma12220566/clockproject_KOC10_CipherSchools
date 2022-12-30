#Clock Angle Problem
#Clock Angle Problem: Given time in hh:mm format in 24-hour notation, calculate the
#shorter angle between the hour and minute hand in an analog clock.

def find_angle(hh, mm):
    #handle 24-hour notation
    hh = hh % 12
    
    #find the position of hour hand
    h = (hh*360)//12+(mm*360)//(12*60)
    
    #finf the position of minutes's hand
    m = (mm*360)//60
    
    #calculate the angle difference 
    angle = abs(h-m)
    
    #consider the shorter angle and return it
    if angle > 180:
        angle = 360 - angle
        
    return angle


hh = int(input())
mm = int(input())
print(find_angle(hh, mm))
