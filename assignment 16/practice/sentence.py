from playsound import playsound
import gtts
s1 = input("enter first string: ")
s2 = input("enter second string: ")
s3 = input("enter third string: ")
list_str = [len(s1), len(s2), len(s3)]
list_str.sort(reverse=True)
if list_str[0] == len(s1):
    tts = gtts.gTTS(s1)
elif list_str[0] == len(s2):
    tts = gtts.gTTS(s2)
else:
    tts = gtts.gTTS(s3)
tts.save("voice.mp3")
playsound('voice.mp3')