'''QUESTION - Find final position in 2d given initial position and velocity
Given an initial position of a point moving in a 2d cartesian plane with a constant velocity, find the the final position of the point after a given time in two dimensions.

Hint: final position = intial position + velocity * time
'''
#PLATFORM - IITM COURSE

def final_position(pos: tuple, vel: tuple, time:int) -> tuple:
   
    x1, y1 = pos
    vx, vy = vel
    
    final_x = x1 + vx * time
    final_y = y1 + vy * time
    
    return (final_x, final_y)
    

