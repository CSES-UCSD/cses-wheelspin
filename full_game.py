import cv2
import numpy as np
import random
import math
import time
import pyautogui
from turtle import ht
import mediapipe as mp
from repo import repofn

# Parameters for creating the wheel
radius = 300
center = (400, 400)
number_of_sections = 6
font_size = 1
font_type = cv2.FONT_HERSHEY_PLAIN
font_thickness = 2
font_color = (0, 0, 0)
section_labels = ["2 Raffle", "1 Raffle", "Candy", "Nothing", "3 Raffle", "T-shirt"]
rotating_angle = 0

# Pointer parameters
pointer_length = 150
pointer_x = center[0]
pointer_start_y = 10
pointer_end_y = 125
pointer_color = (0, 75, 150)
pointer_thickness = 5

image = np.zeros((800, 800, 3), dtype=np.uint8)


def create_wheel(image, radius, center, number_of_sections, rotating_angle, section_labels):
    angle = 360 / number_of_sections

    for i in range(number_of_sections):
        start_angle = i * angle + rotating_angle
        end_angle = (i + 1) * angle + rotating_angle

        if i % 2 == 0:
            color = (165, 133, 23)
        else:
            color = (34, 180, 230)

        cv2.ellipse(image, center, (radius, radius), 0, start_angle, end_angle, color, -1)

        text_position = (start_angle + end_angle) / 2

        text_position_horizontal = int(center[0] + (radius - 100) * math.cos(math.radians(text_position)))
        text_position_vertical = int(center[1] + (radius - 100) * math.sin(math.radians(text_position)))

        label = section_labels[i]
        cv2.putText(image, label, (text_position_horizontal, text_position_vertical), font_type, font_size,
                    font_color, font_thickness, lineType=cv2.LINE_AA)

    return image


# Initialize variables for spinning the wheel
spinning = False
start_time = 0
spin_duration = random.uniform(3, 8)
speed = 175

# Initialize the hand tracking module (from the repo)
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
smoothening = 9
plocx, plocy = 0, 0
clocx, clocy = 0, 0

while True:
    if spinning:
        time_passed = time.time() - start_time
        if time_passed < spin_duration:
            rotating_angle = speed * time_passed
            new_image = create_wheel(image, radius, center, number_of_sections, rotating_angle, section_labels)
        else:
            spinning = False

    else:
        new_image = create_wheel(image, radius, center, number_of_sections, rotating_angle, section_labels)
        cv2.line(new_image, (pointer_x, pointer_start_y), (pointer_x, pointer_end_y), pointer_color, pointer_thickness)

    if repofn(cap, hand_detector, drawing_utils, screen_width, screen_height, index_y, smoothening, plocx, plocy, clocx, clocy):
        pyautogui.click()
        start_time = time.time() # Start the spin timer
        spinning = True


    cv2.imshow('CSES Spin the Wheel', new_image)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == 13:
        spinning = False
        spin_duration = random.uniform(3, 8)

cv2.destroyAllWindows()

