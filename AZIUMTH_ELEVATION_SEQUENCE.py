import math

#--------------------------------------------
# Azimuth and Elevation Position Compensation 
# Forrest Schultz , 3-14-2023
#--------------------------------------------

#CONSTANT SETUP 
adjacent_length_cons = 3 # A non-zero number to act as a leg in the trig equations. Doesn't need to change

#VARIABLES TO BE READ FROM ENCODER AND UPDATED IN LOOP
current_azimuth = 0 #This is the current elevation position of the camera system at which a reading is taken
current_elevation = 45 #This is the current elevation position of the camera system at which a reading is taken
azimuth_offset = 5 #This is X error from the center of camera frame (0,0) to the center of the target positon (must be in degrees)
elevation_offset = 5 #This is the Y error from the center of camera frame (0,0) to the center of the target positon (must be in degrees)


if current_elevation == 90:
    current_elevation = 89.999999 #To avoid arccosine error at 90 degrees


#EQUATION SEQUENCE
x = math.tan(math.radians(azimuth_offset)) * adjacent_length_cons
r = adjacent_length_cons / math.cos(math.radians(azimuth_offset))
z = adjacent_length_cons * math.sin(math.radians(current_elevation))

theta = math.degrees(math.acos(z / r))
phi = math.degrees(math.acos(x / (r * math.sin(math.radians(theta)))))


# ANSWERS (DISTANCE TO CENTER TARGET)
azimuth_pos_move = 90 - phi
elevation_pos_move = 90 - current_elevation - theta + elevation_offset

# NEW ABSOLUTE POSITIONS
new_abs_azimuth = (current_azimuth + azimuth_pos_move) % 360
if new_abs_azimuth < 0:
    new_abs_azimuth += 360
new_abs_elevation = current_elevation + elevation_pos_move


print("Azimuth Position to Move:", azimuth_pos_move)
print("Elevaiton Position to Move:", elevation_pos_move)
print()
print("New Absolute Azimuth:", new_abs_azimuth)
print("New Absolution Elevation:", new_abs_elevation)




