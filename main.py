import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""


if __name__ == "__main__":
    speak("Hello, I'm your voice assistant! I'm here to help with information and fun stuff.")

    while True:
        query = listen().lower()

        if "hey jarvis" in query:
            speak("Hey there! How can I help today?")
        elif "goodbye" in query or "bye" in query:
            speak("Goodbye! Catch you later!")
            break
        elif "i am good " in query:
            speak("Awesome! What would you like to do?")
        elif "play music" in query:
            speak("I can't play music directly, but I can suggest fun music videos on YouTube! What kind of music do you like?")
        elif "call my boss" in query:
            speak("I'm not able to make calls yet, but I can help you find your boss's information online if you need it.")
        elif "shortest route" in query:
            speak("I can help you find the shortest route online! Just tell me where you're going.")
        elif "nearby restaurant" in query:
            speak("I can help you find yummy places to eat! What kind of food are you craving?")
        elif "tell me a joke" in query:
            speak("What do you call a lazy kangaroo? A pouch potato!")  # Add more age-appropriate jokes
        else:
            speak("Hmm, I'm still learning some things. Can you rephrase that, or try asking something else?")
