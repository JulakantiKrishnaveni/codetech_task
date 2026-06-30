
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("sample.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)

    print("Recognized Text:")
    print(text)

    with open("output.txt","w") as file:
        file.write("Recognized Text:\n")
        file.write(text)

    print("\nOutput saved successfully!")

except Exception as e:
    print("Error:",e)
