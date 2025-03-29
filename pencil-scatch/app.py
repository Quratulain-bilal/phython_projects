import cv2
img = cv2.imread("parrot1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted = 255 - gray
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blurred = 255 - blurred

# Create the pencil sketch
sketch = cv2.divide(gray, inverted_blurred, scale=256.0)

# Save the sketch
cv2.imwrite("pencil_sketch.jpg", sketch)


