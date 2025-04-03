# Hand Sign Recognition Model

## Overview
The Hand Sign Recognition Model is a machine learning-based system that detects and classifies hand gestures using computer vision techniques. It uses MediaPipe for hand landmark detection and a Random Forest Classifier for gesture classification. This model can be used for sign language recognition, gesture-based controls, and human-computer interaction.

## Features
- Real-time hand detection using a webcam.
- Custom dataset collection for training.
- Hand landmark extraction using MediaPipe.
- Random Forest Classifier for efficient classification.
- Live prediction visualization on the screen.

## Technologies Used
- Python (Primary programming language)
- OpenCV (Image capturing and processing)
- MediaPipe (Hand landmark detection)
- scikit-learn (Random Forest Classifier)
- NumPy & Pickle (Data handling and storage)

## Project Structure
- capture.py -> Captures hand sign images for dataset creation.
- create_dataset.py -> Processes images and extracts hand landmarks.
- train_classifier.py -> Trains a Random Forest model on extracted features.
- inference_classifier.py -> Real-time hand sign recognition using trained model.
- test.py -> Alternative test script for live prediction.
- data/ -> Directory containing captured images.
- data.pickle -> Pickle file storing extracted landmark features.
- model.p -> Trained model saved for inference.

## How It Works
1. **Capture Hand Sign Images** (capture.py)
   - Opens a webcam and saves images when 's' is pressed.
   - Press 'q' to quit capturing.

2. **Process Dataset & Extract Features** (create_dataset.py)
   - Reads saved images and extracts 21 hand landmark points using MediaPipe.
   - Saves the processed features and labels in data.pickle.

3. **Train the Model** (train_classifier.py)
   - Loads data.pickle and trains a Random Forest Classifier.
   - Saves the trained model as model.p.

4. **Real-Time Gesture Recognition** (inference_classifier.py)
   - Uses a webcam to detect hand landmarks.
   - Predicts gestures and displays them on the screen.

## Use Cases
- Sign Language Recognition
- Gesture-Controlled Applications
- Human-Computer Interaction
- Smart Home Automation


