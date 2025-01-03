import cv2
import mediapipe as mp

class EmotionAnalyzer:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(refine_landmarks=True)
        self.emotions = {
            "happy": "😊",
            "neutral": "😐",
            "surprised": "😮",
            "sad": "😢",
            "angry": "😠"
        }

    def analyze(self, image):
        """
        Analyze the image to detect emotions based on facial landmarks.
        :param image: Input image
        :return: Detected emotion
        """
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_image)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Analyze specific landmarks (e.g., eyes, mouth, eyebrows)
                # Simplified example: wide mouth = happy, raised eyebrows = surprised
                mouth_open = self.calculate_distance(
                    face_landmarks.landmark[13], face_landmarks.landmark[14]
                )
                eyebrow_raise = self.calculate_distance(
                    face_landmarks.landmark[65], face_landmarks.landmark[55]
                )

                if mouth_open > 0.05:
                    return "happy"
                elif eyebrow_raise > 0.02:
                    return "surprised"
                else:
                    return "neutral"

        return "neutral"

    def calculate_distance(self, point1, point2):
        """
        Calculate the Euclidean distance between two points.
        :param point1: First point
        :param point2: Second point
        :return: Distance
        """
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5
