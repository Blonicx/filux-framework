"""This class is for Face Reconition in Images and Videos"""
import face_recognition

class Face:
    def __init__(self, known_face_path):
        self._known_face_path = known_face_path

    def search_image(self, unknown_image_path, tolerance=0.6):
        known_image = face_recognition.load_image_file(self._known_face_path)
        unknown_image = face_recognition.load_image_file(unknown_image_path)

        known_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        return face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance)

    def search_video(self):
        pass
