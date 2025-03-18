import cv2

img = cv2.imread("image.jpg")  # Image ko load kar raha hai

cartoon = cv2.stylization(img, sigma_s=150, sigma_r=0.25)  # Cartoon effect apply kar raha hai

cv2.imwrite("cartoon.jpg", cartoon)  # Output image ko save kar raha hai
