# Speak2Text
-
Voice Speech Translator
Overview
Voice Speech Translator is a Python-based application that captures voice input from the user, converts it to text, and then translates that text into a specified target language. The application uses the Google Speech Recognition API for speech-to-text conversion and the Google Translate API for translating the recognized text into the desired language.

Features
Speech Recognition: Converts spoken language into written text using Google's Speech Recognition API.
Text Translation: Translates the recognized text into another language using Google Translate.
Language Flexibility: Supports multiple languages for both input and output, making it versatile for users around the world.
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.6 or later
pip3 package manager
You'll also need to install the required Python libraries:


```
pip3 install SpeechRecognition pyaudio googletrans==4.0.0-rc1
```
For macOS users, if you encounter issues with pyaudio, ensure that you have the Xcode Command Line Tools installed:


```
xcode-select --install
```
Installation
Clone the Repository:
```
git clone https://github.com/yourusername/voice-speech-translator.git
cd voice-speech-translator
```
Set Up a Virtual Environment (Optional but Recommended):
```
python3 -m venv venv
source venv/bin/activate
```

Install Dependencies:

bash
```
pip3 install -r requirements.txt
```
If you don’t have a requirements.txt file, install the libraries manually:


```
pip3 install SpeechRecognition pyaudio googletrans==4.0.0-rc1
```
Usage
Run the Application:

```
python3 voice_translate.py
```
Enter the Target Language: When prompted, enter the language code for translation (e.g., en for English, es for Spanish, uz for Uzbek).

Speak into the Microphone: The application will listen to your speech, convert it to text, and then translate it into the specified language.

View Translated Text: The translated text will be displayed in the terminal.

Example

```
Enter the language code for translation (e.g., 'en' for English, 'es' for Spanish): es
Please speak clearly into the microphone...
You said: "Hello, how are you?"
Translated Text: "Hola, ¿cómo estás?"
```
Troubleshooting
ModuleNotFoundError: Ensure that all required modules are installed. You may need to update pip and setuptools if you encounter issues with distutils.
pyaudio Installation Issues on macOS: Install Xcode Command Line Tools or consider using the sounddevice library as an alternative.
Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss improvements or bugs.

License
This project is licensed under the MIT License - see the LICENSE file for details.