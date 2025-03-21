from PIL import Image  

img = Image.open("777.jpg").convert("L")  
img.save("bw_777.jpg")  
