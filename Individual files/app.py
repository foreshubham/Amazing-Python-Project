import cv2

def Convert(image):
    Gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Change COLOR_RGB2GRAY to COLOR_BGR2GRAY
    Blur_image = cv2.GaussianBlur(Gray_image, (3, 3), 0)
    detect_edge = cv2.adaptiveThreshold(Blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

    output = cv2.bitwise_and(image, image, mask=detect_edge)

    cv2.imshow("Original picture", image)  # Show the processed image, not the original
    cv2.imshow("Cartoon Effect", output)
    cv2.waitKey(0)

img = cv2.imread("new.jpeg")
Convert(img)
