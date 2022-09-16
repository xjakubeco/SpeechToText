import speech_recognition as sr


def voiceinput():
    print("Say something...")
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        audio = r.listen(source)

    mytext = r.recognize_google(audio)
    output = "You said: "+mytext
    return output


firstinput = voiceinput().lower()
print(firstinput)