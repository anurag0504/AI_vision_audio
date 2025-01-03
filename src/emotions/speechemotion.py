import librosa
import numpy as np

class SpeechEmotionAnalyzer:
    def analyze(self, audio_file):
        """
        Analyze the audio file to detect emotion.
        :param audio_file: Path to the audio file
        :return: Detected emotion
        """
        try:
            y, sr = librosa.load(audio_file)
            pitch = librosa.feature.rms(y=y).mean()
            if pitch > 0.05:
                return "Angry"
            elif pitch > 0.02:
                return "Happy"
            else:
                return "Calm"
        except Exception as e:
            return f"Error in audio analysis: {str(e)}"
