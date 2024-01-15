import cv2
from PIL import Image
from utils import get_limits

def face_detection_image(image_path=None):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    if image_path is None:
        image_path = input("Enter the path of the image: ")

    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to read the image at path {image_path}")
        return

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print(f"Error: Unable to read the image at path {image_path}")
        return

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()
    
def face_detection_video():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # To capture video from webcam. 
    cap = cv2.VideoCapture(0)
    # To use a video file as input 
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display
        cv2.imshow('img', img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
    # Release the VideoCapture object
    cap.release()

def cartoonify_image(image_path):
    img = cv2.imread(image_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    detect_edge = cv2.adaptiveThreshold(blur_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)
    output = cv2.bitwise_and(img, img, mask=detect_edge)

    cv2.imshow("Original picture", img)
    cv2.imshow("Cartoon Effect", output)
    cv2.waitKey(0)  # Wait for user input before returning to the menu

    

def color_detection():
    yellow = [0, 255, 255]  # Yellow in RGB color
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_limit, upper_limit = get_limits(color=yellow)

        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)  
        mask = Image.fromarray(mask)

        bbox = mask.getbbox()

        if bbox is not None: 
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

        print(bbox)
      
        cv2.imshow('frame', frame)
           
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Face Detection (Image)")
        print("2. Face Detection (Video)")
        print("3. Cartoonify Image")
        print("4. Color Detection")
        print("5. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
    
            face_detection_image()

        elif choice == "2":
            face_detection_video()

        elif choice == "3":
            image_path = input("Enter the path of the image: ")
            cartoonify_image(image_path)

        elif choice == "4":
            color_detection()
            
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
