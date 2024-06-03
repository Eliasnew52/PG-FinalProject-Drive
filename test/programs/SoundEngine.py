import pygame as PG

class AudioEngine:
    
    
    def SoundsEffect(effect,duration):   #Mixer Sound para los Efectos
        PG.mixer.Sound.play(f"effects/{effect}.mp3",loops= duration)
        if duration == -1:
            print(f'[NOW PLAYING: {effect} ON INFINITE LOOP] ')
        else:
            print(f'[NOW PLAYING: {effect} ONCE] ')
            
    

    def Global_Audio(song):      #Modulo Mixer para la Musica
        PG.mixer.music.load(f'music/{song}.mp3')
        PG.mixer.music.play(fade_ms=2000)
    


    def Pause_GA():
        PG.mixer.music.pause()
        print("[MUSIC IS STOPPED]")

    def Resume_GA():
        PG.mixer.music.unpause()
        print("[MUSIC IS NOW PLAYING]")

