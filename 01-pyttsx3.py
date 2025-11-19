import pyttsx3

enginee = pyttsx3.init()
enginee.setProperty("Voice", "brazil")
enginee.say("Olá mundo. Vamos construir um assistente virtual")
enginee.runAndWait()