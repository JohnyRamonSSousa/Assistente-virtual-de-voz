from gtts import gTTS
from playsound import playsound

tts = gTTS("Olá Mundo. Vamos construir nosso assistente", lang="pt-br")
tts.save("dados/audio.mp3")
playsound("dados/audio.mp3")