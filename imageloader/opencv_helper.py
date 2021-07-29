import cv2

def apply_gaussian_blur(img):
    return cv2.GaussianBlur(img,(7,7),cv2.BORDER_DEFAULT)

def apply_blur(img):
    return cv2.blur(img,(10, 10))

def apply_median_blur(img):
    return cv2.medianBlur(img,5)

def apply_edge_cascade(img):
    return cv2.Canny(img, 125, 175)

def apply_crop(img):
    return img[0:200]

def apply_bilateral_filtering(img):
    return cv2.bilateralFilter(img,9,75,75)



def read_image(path):
    return cv2.imread(path)

def write_image(path, img):
    return cv2.imwrite(path, img)
