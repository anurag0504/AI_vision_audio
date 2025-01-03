from googletrans import Translator


class MultilingualSupport:
    def __init__(self):
        self.translator = Translator()

    def translate(self, text, target_language):
        """
        Translate the given text into the target language.
        :param text: Text to translate
        :param target_language: Target language code (e.g., 'es' for Spanish)
        :return: Translated text
        """
        try:
            translation = self.translator.translate(text, dest=target_language)
            return translation.text
        except Exception as e:
            return f"Translation failed: {str(e)}"
