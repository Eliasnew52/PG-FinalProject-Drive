import pygame as PG
import time
class AudioEngine:
        


    
    def SoundsEffect(effect,duration):   #Mixer Sound para los Efectos
        PG.mixer.Sound.play(f"effects/{effect}.mp3",loops= duration)
        if duration == -1:
            print(f'[NOW PLAYING: {effect} ON INFINITE LOOP] ')
        else:
            print(f'[NOW PLAYING: {effect} ONCE] ')
    
    def EngineStartup():
        
        # Initialize Pygame mixer
        PG.mixer.init()
        
        # Load sound files
        EngineStartup = PG.mixer.Sound("music/EngineStartup.wav")
        EngineIdle = PG.mixer.Sound("music/EngineIdle.wav")
        
        # Play EngineStartup sound
        startup_channel = EngineStartup.play(loops=0)
                
        # Play EngineIdle sound in a loop
        idle_channel = EngineIdle.play(loops=-1)
        
        return idle_channel

    def StopEngineIdle(idle_channel):
        # Stop the EngineIdle sound
        PG.mixer.stop()
 


    def Global_Audio(song):      #Modulo Mixer para la Musica
        
        PG.mixer.music.load(f'music/{song}.mp3')
        PG.mixer.music.play(fade_ms=2000)
    

    def Resume_GA():
        PG.mixer.music.unpause()
        print("[MUSIC IS NOW PLAYING]")
    
    def Pause_GA():
        PG.mixer.music.pause()

