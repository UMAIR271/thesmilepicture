import cv2

imagepath = "./i.jpg"
image_path = "./splitedimages"
img = cv2.imread(imagepath)
i = 0


for r in range(0, img.shape[0], 360):
    j = 0
    for c in range(0, img.shape[1], 360):

        cv2.imwrite(f"{image_path}/{i}{j}.png", img[r:r+360, c:c+360, :])
        j = j+1
    i = i+1
