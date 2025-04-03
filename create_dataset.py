import os
import pickle

import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

data = []
labels = []

for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []

        img_full_path = os.path.join(DATA_DIR, dir_, img_path)
        print("Image path:", img_full_path)

        img = cv2.imread(img_full_path)
        if img is None:
            print("Error: Failed to load image.")
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            # We assume only one hand is detected in each image
            hand_landmarks = results.multi_hand_landmarks[0]

            for landmark in hand_landmarks.landmark:
                x = landmark.x
                y = landmark.y
                data_aux.append(x)
                data_aux.append(y)

        # Pad sequences with zeros to ensure uniform length
        while len(data_aux) < 42:  # Assuming max_landmarks is 21
            data_aux.extend([0, 0])

        data.append(data_aux)
        labels.append(dir_)

        # Debug prints
        print("Sample data:", data_aux)
        print("Length:", len(data_aux))
        print("Data type:", type(data_aux))

# Check if any data was loaded
print("Total samples:", len(data))

# Save data to pickle file
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
