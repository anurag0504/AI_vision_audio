from emotions.emotion import EmotionAnalyzer
from emotions.speechemotion import SpeechEmotionAnalyzer

class MultimodalEmotionAnalyzer:
    def __init__(self):
        self.face_analyzer = EmotionAnalyzer()
        self.speech_analyzer = SpeechEmotionAnalyzer()

    def analyze(self, image, audio_file):
        """
        Combine facial and speech analysis for multimodal emotion recognition.
        :param image: Input image
        :param audio_file: Path to the audio file
        :return: Final detected emotion
        """
        face_emotion = self.face_analyzer.analyze(image)
        speech_emotion = self.speech_analyzer.analyze(audio_file)

        # Prioritize speech emotion if it's highly significant
        if speech_emotion == "Angry" and face_emotion in ["Neutral", "Sad"]:
            return "Frustrated"
        elif speech_emotion and face_emotion:
            return f"Face: {face_emotion}, Voice: {speech_emotion}"
        return face_emotion or speech_emotion
