import cv2

# Load the image
image = cv2.imread('business-girl.jpg')

# Define the new width and height
new_width = 800
new_height = 900

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image as a new file in PNG format
cv2.imwrite('new-image.png', resized_image)

# Save the resized image as a new file in JPEG format
# cv2.imwrite('path_to_new_image.jpg', resized_image)