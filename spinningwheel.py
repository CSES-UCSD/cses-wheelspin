# import cv2
# import numpy as np
# # Create a blank image
# img = np.zeros((500, 500, 3), dtype=np.uint8)
# # Draw the wheel
# cv2.circle(img, (250, 250), 250, (255, 255, 255), -1)
# cv2.circle(img, (250, 250), 100, (0, 0, 0), -1)
# # Draw the segments
# angles = np.linspace(0, 2*np.pi, 8)
# points = []
# for angle in angles:
#   # Get the corresponding point on the circle
#   point = (250 + 100 * np.cos(angle), 250 + 100 * np.sin(angle))
#   # Add the point to the list
#   points.append(point)
# # Draw the segments
# points = [tuple(point) for point in points]
# cv2.fillPoly(img, [points], (255, 255, 255))
# # Rotate the image
# theta = np.pi / 180  # Angle of rotation in radians
# rotation_matrix = cv2.getRotationMatrix2D((250, 250), theta, 1)
# rotated_img = cv2.warpAffine(img, rotation_matrix, (500, 500))
# # Show the image
# cv2.imshow("Spinning Wheel", rotated_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# import numpy as np
# # Create a black image of the desired size
# image = np.zeros((500, 500, 3), dtype="uint8")
# # Draw a filled circle on the image
# cv2.circle(image, (250, 250), 100, (255, 255, 255), -1)
# # Display the image on the screen
# cv2.imshow("Circle", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
# Create a black image of the desired size
image = np.zeros((500, 500, 3), dtype="uint8")
# Draw a filled circle on the image
cv2.circle(image, (250, 250), 100, (255, 255, 255), -1)
# Create a rotation matrix
angle = 0
rotation_matrix = cv2.getRotationMatrix2D((250, 250), angle, 1)
# Rotate the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (500, 500))
# Display the image on the screen
cv2.imshow("Circle", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
