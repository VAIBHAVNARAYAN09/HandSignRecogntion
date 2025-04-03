import cv2
import os

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()


folder = "C:\\Users\\Vaibhav\\Desktop\\coding\\project\\data\\5"

# Create folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)

counter = 0
while True:
    success, img = cap.read()

    if not success:
        print("Error: Failed to read frame.")
        continue

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord("s"):
        cv2.imwrite(f'{folder}/{counter}.jpg', img)
        print("Saved image:", counter)
        counter += 1
   
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
