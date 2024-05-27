import pygame as PG

class AudioEngine:

    def Global_Audio(audio):      #Modulo Mixer para la Musica
        PG.mixer.music.load(f'music/{audio}.mp3')
        PG.mixer.music.play(fade_ms=2000)

