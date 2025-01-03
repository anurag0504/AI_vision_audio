import cv2
import mediapipe as mp

class VisionProcessor:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_hands = mp.solutions.hands
        self.face_detection = self.mp_face_detection.FaceDetection(min_detection_confidence=0.5)
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    def process_frame(self, image):
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results_face = self.face_detection.process(image)
        results_hands = self.hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, results_face, results_hands
