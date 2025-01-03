import cv2
import tkinter as tk
from vision import VisionProcessor
from audio import VoiceProcessor
from gui import AppGUI
import threading
from multilingual import MultilingualSupport
from emotions.emotion import EmotionAnalyzer
from emotions.speechemotion import SpeechEmotionAnalyzer
from emotions.multimodalemotion import MultimodalEmotionAnalyzer

class AdvancedAI:
    def __init__(self, api_key):
        self.vision_processor = VisionProcessor()
        self.voice_processor = VoiceProcessor(api_key)
        self.facial_emotion_analyzer = EmotionAnalyzer()
        self.speech_emotion_analyzer = SpeechEmotionAnalyzer()
        self.multimodal_emotion_analyzer = MultimodalEmotionAnalyzer()
        self.multilingual_support = MultilingualSupport()
        self.gesture_commands = {
            "wave": "Hello there!",
            "thumbs_up": "Thank you!",
        }
        self.detected_emotion = "Neutral"

    def process_vision(self, frame):
        processed_frame, results_face, results_hands = self.vision_processor.process_frame(frame)
        gesture = self.detect_gesture(results_hands)
        facial_emotion = self.detect_facial_emotion(results_face, frame)
        return processed_frame, gesture, facial_emotion


    def detect_gesture(self, results_hands):
        if results_hands and results_hands.multi_hand_landmarks:
            for hand_landmarks in results_hands.multi_hand_landmarks:
                if hand_landmarks.landmark[4].y < hand_landmarks.landmark[8].y:
                    return "thumbs_up"
        return None
    def detect_facial_emotion(self, results_face, frame):
        """
        Detect facial emotion from Mediapipe results and the frame.
        :param results_face: Mediapipe face detection results.
        :param frame: The original image frame.
        :return: Detected emotion.
        """
        if results_face and results_face.detections:
            for detection in results_face.detections:
                # Get the bounding box coordinates
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x, y, w, h = (
                    int(bboxC.xmin * w),
                    int(bboxC.ymin * h),
                    int(bboxC.width * w),
                    int(bboxC.height * h),
                )
                # Ensure ROI is within frame bounds
                x, y, w, h = max(0, x), max(0, y), max(0, w), max(0, h)
                face_roi = frame[y : y + h, x : x + w]

                # Pass the cropped face to the emotion analyzer
                emotion = self.facial_emotion_analyzer.analyze(face_roi)
                self.detected_emotion = emotion
                return emotion
        return self.detected_emotion


    def process_audio(self, audio_file):
        speech_emotion = self.speech_emotion_analyzer.analyze(audio_file)
        return speech_emotion

    def multimodal_response(self, gesture, facial_emotion, speech_emotion=None):
        if gesture in self.gesture_commands:
            return self.gesture_commands[gesture]
        if speech_emotion and facial_emotion:
            return f"Speech Emotion: {speech_emotion}, Facial Emotion: {facial_emotion}."
        if facial_emotion:
            return f"I see you're feeling {facial_emotion}."
        return "I'm here to help!"

def vision_loop(ai, app_gui):
    cap = cv2.VideoCapture(0)  # Open webcam
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        processed_frame, gesture, facial_emotion = ai.process_vision(frame)
        speech_emotion = None  # Placeholder: Add audio processing pipeline here if required
        response = ai.multimodal_response(gesture, facial_emotion, speech_emotion)
        app_gui.update_text(f"Gesture: {gesture}, Facial Emotion: {facial_emotion}\nResponse: {response}")
        app_gui.update_image(processed_frame)

    cap.release()

def voice_loop(ai):
    ai.voice_processor.run()

def main():
    api_key = "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"

    # Initialize the advanced AI
    ai = AdvancedAI(api_key)

    # Create the GUI
    root = tk.Tk()
    app_gui = AppGUI(root)

    # Start vision loop in a thread
    vision_thread = threading.Thread(target=vision_loop, args=(ai, app_gui))
    vision_thread.daemon = True
    vision_thread.start()

    # Start voice processing loop in a thread
    voice_thread = threading.Thread(target=voice_loop, args=(ai,))
    voice_thread.daemon = True
    voice_thread.start()

    # Run the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
