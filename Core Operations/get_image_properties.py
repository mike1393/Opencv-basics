import cv2

src_img = "../src/starry_night.jpg"
img = cv2.imread(src_img)


def getPixelColor(image, row=0, col=0, color="b"):
    if color == "b":
        return image.item(row,col,0)
    elif color == "g":
        return image.item(row,col,1)
    elif color == "r":
        return image.item(row,col,2)

def setPixelColor(image, row=0, col=0, color = "b",value=0):
    if color == "b":
        return image.itemset((row,col,0),value)
    elif color == "g":
        return image.itemset((row,col,1),value)
    elif color == "r":
        return image.itemset((row,col,2),value)
row,col, color = 0,0, "b"
print(f"pixel value red in ({row},{col}) is {getPixelColor(img,row,col,color)}")
setPixelColor(img,row,col,'r',50)
print(f"pixel value red in ({row},{col}) is {getPixelColor(img,row,col,color)}")