import cv2
import numpy as np
import random
import math
import time

# parameters for creating the wheel
radius= 300
center = (400,400)
number_of_sections = 6
font_size = 2
font_type= cv2.FONT_HERSHEY_PLAIN
font_thickness = 2
font_color=(0,0,0)
section_labels=["one","two","three","four","five","six"]
rotating_angle=0

# pointer parameters
pointer_length = 150
pointer_x = center[0]
pointer_start_y = 10
pointer_end_y = 125
pointer_color= (255,228,196)
pointer_thickness= 5


image = np.zeros((800, 800, 3), dtype=np.uint8)
def create_wheel(image, radius, center, number_of_sections, rotating_angle,section_labels):
    angle= 360/number_of_sections

    for i in range(number_of_sections):
        start_angle= i*angle + rotating_angle
        end_angle = (i+1) *angle + rotating_angle


        if i % 2 == 0:
            color = (255,224,32)
        else:
            color = (80,208,255)

        cv2.ellipse(image,center,(radius,radius),0,start_angle, end_angle, color,-1)

        text_position = (start_angle + end_angle) / 2

        text_position_horizontal = int(center[0] + (radius - 50) * math.cos(math.radians(text_position)))
        text_position_veritcle = int(center[1] + (radius - 50) * math.sin(math.radians(text_position)))

        label = section_labels[i]
        cv2.putText(image,label,(text_position_horizontal,text_position_veritcle),font_type,font_size,font_color,font_thickness,lineType=cv2.LINE_AA
                    )

    return image


spinning = False
start_time = 0
def on_clicking(click,x,y,flags,param):
    global start_time
    global spinning

    if click == cv2.EVENT_LBUTTONDOWN and not spinning:
        spinning = True
        start_time =time.time()


cv2.namedWindow('CSES Spin the Wheel')
cv2.setMouseCallback('CSES Spin the Wheel', on_clicking)

spin_duration = random.uniform(5, 8)
speed = 20

while True:
    if spinning:
        time_passed = time.time() - start_time
        if time_passed < spin_duration:
            rotating_angle = speed * time_passed
            new_image = create_wheel(image, radius, center, number_of_sections, rotating_angle, section_labels)

    else:
        new_image = create_wheel(image, radius, center, number_of_sections, rotating_angle, section_labels)
        cv2.line(new_image, (pointer_x, pointer_start_y), (pointer_x, pointer_end_y), pointer_color, pointer_thickness)

    cv2.imshow('CSES Spin the Wheel', new_image)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == 13:
        spinning = False

cv2.destroyAllWindows()


