import speech_recognition as sr

recon = sr.recognizers()

with sr.Microphone() as source:
    print("Diga alguma coisa")
    audio = recon.listen(source)

print(recon.recognize_google(audio, language="pt"))