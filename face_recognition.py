import cv2
import face_recognition
import os
import numpy as np

# Load known faces
known_faces_dir = 'known_faces'
known_face_encodings = []
known_face_names = []

for filename in os.listdir(known_faces_dir):
    image = face_recognition.load_image_file(f"{known_faces_dir}/{filename}")
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    name = os.path.splitext(filename)[0]
    known_face_names.append(name)

# Load test image
image_path = 'test_images/group_photo.jpg'
image = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

# Convert to OpenCV format
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Compare faces
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)

    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    # Draw box
    cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(image_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Show result
cv2.imshow("Face Recognition", image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
