import speech_recognition as sr
from googletrans import Translator

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Please speak clearly into the microphone...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        speech_text = recognizer.recognize_google(audio)
        print(f"You said: {speech_text}")
        return speech_text
    except sr.UnknownValueError:
        print("Sorry, I did not understand the speech.")
        return None
    except sr.RequestError:
        print("Sorry, I couldn't request results from the speech recognition service.")
        return None

def translate_text(text, target_language='en'):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    print(f"Translated Text: {translated.text}")
    return translated.text

def main():
    target_language = input("Enter the language code for translation (e.g., 'en' for English, 'es' for Spanish): ")
    speech_text = recognize_speech_from_mic()

    if speech_text:
        translated_text = translate_text(speech_text, target_language)
        print(f"Final Translated Text: {translated_text}")
    else:
        print("No speech recognized to translate.")

if __name__ == "__main__":
    main()
