from datetime import datetime # for know time 
import pygame # access music files

pygame.mixer.init() #initialise pygame

#load all music files
pygame.mixer.music.load('antidote.mp3')
pygame.mixer.music.load('morning.mp3')
pygame.mixer.music.load('raat.mp3')
   

#print current time
local_time = datetime.now().strftime('%H : %M : %S')
print(local_time)

#check current time and play music according time
if local_time >= '00 : 00 : 01' and local_time <= '11 :59 :58':
    print(f"Good Morning {local_time}")
    pygame.mixer.music.load('morning.mp3')
    pygame.mixer.music.play()

elif local_time >='12 :00 :01' and local_time <= '17 : 00 : 00':
    print(f"Good Afternoon {local_time}")
    pygame.mixer.music.load('antidote.mp3')
    pygame.mixer.music.play()

elif local_time >= '17 : 00 :01':
    print(f"Good Night Soo bhi jao ab ")
    pygame.mixer.music.load('raat.mp3')
    pygame.mixer.music.play()

pygame.time.wait(100000) # music play 1 min

pygame.mixer.music.stop() # pygame stop (music stop) execution of program is complete