import cv2
import numpy as np
import os
import glob
import face_recognition

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

        images_path = [
            f for f in glob.glob(os.path.join(images_path, "*.*"))
            if f.lower().endswith(supported_extensions)
        ]
        print(f"{len(images_path)} encoding images found.")

        for img_path in images_path:
            try:
                # Read the image directly with OpenCV
                img = cv2.imread(img_path)
                if img is None:
                    print(f"Could not read {img_path}. Skipping...")
                    continue
                
                # Convert to RGB (face_recognition expects RGB)
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
                # Force color conversion for compatibility
                rgb_img = cv2.cvtColor(cv2.cvtColor(rgb_img, cv2.COLOR_RGB2GRAY), cv2.COLOR_GRAY2RGB)
                
                # Use OpenCV to detect faces first
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 4)
                
                if len(faces) == 0:
                    print(f"No face found in {img_path} using OpenCV. Skipping...")
                    continue
                
                # Get the first face detected by OpenCV
                x, y, w, h = faces[0]
                face_img = rgb_img[y:y+h, x:x+w]
                
                # Now try face_recognition on the detected face area
                try:
                    face_encoding = face_recognition.face_encodings(face_img)[0]
                except Exception as e:
                    print(f"Error encoding face from {img_path}: {str(e)}")
                    continue

                # Get the name from the filename
                basename = os.path.basename(img_path)
                filename = os.path.splitext(basename)[0]

                # Add face encoding and name
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(filename)

                print(f"Successfully loaded: {filename}")

            except Exception as e:
                print(f"Error processing {img_path}: {str(e)}")
                continue

        print(f"{len(self.known_face_names)} encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        # Force color conversion for compatibility
        rgb_small_frame = cv2.cvtColor(cv2.cvtColor(rgb_small_frame, cv2.COLOR_RGB2GRAY), cv2.COLOR_GRAY2RGB)
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]

            face_names.append(name)

        face_locations = np.array(face_locations) if face_locations else np.array([])
        if len(face_locations) > 0:
            face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names