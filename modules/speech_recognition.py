import speech_recognition as sr

def listen(callback=None, stop_event=None):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if callback: callback("Listening...")
        audio = recognizer.listen(source)

    # Check if the listening should be stopped
    if stop_event and stop_event.is_set():
        return ""

    try:
        # Recognize speech using Google's speech recognition
        text = recognizer.recognize_google(audio)
        if callback: callback(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        if callback: callback("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        if callback: callback(f"Could not request results; {e}")
        return ""
