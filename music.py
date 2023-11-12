from pygame import mixer
from tkinter import messagebox

channelspaused={}
def listen(filename, channelno=0):
    
    if not mixer.get_init():
        mixer.init()
    channel=mixer.Channel(channelno)
    playing=channel.get_busy()
    if channelno in channelspaused:
        channel.unpause()
        del channelspaused[channelno]
    elif playing==True:
        channel.pause()
        channelspaused[channelno]=True
    else:
        sound=mixer.Sound(filename)
        channel.play(sound)

listen("music\\virus.mp3")

while mixer.get_busy:
    pass