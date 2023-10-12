import serial
import time
import sys
import pygame
 
# COM_PORT = '/dev/cu.usbmodem142101'  # 請自行修改序列埠名稱
COM_PORT = 'COM3'  # 請自行修改序列埠名稱
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)
if ser.is_open is True:
    print("Serial port is open!")
music_state = 0

try:
    file=r'/Users/naonao/Desktop/Avicii-WithoutYou-Instrumental.mp3' # 播放音樂的路徑
    file = r"Avicii-WithoutYou-Instrumental.mp3"
    file = r"never_gonna_give_you_up.mp3"
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    pygame.mixer.music.pause()
    
    while True:
        while ser.in_waiting:
            res = ser.read_until().decode()
            print(res, music_state)
            # if res == "b\n":
            #     music_state = not music_state
            #     if music_state:
            #         pygame.mixer.music.unpause()
            #         print("unpause")
            #     else:
            #         pygame.mixer.music.pause()
            #         print("pause")
            if res == "v\n":
                v = int(ser.read_until().decode()) / 1024
                pygame.mixer.music.set_volume(v)
                print(f"{v=}")
            if res == "1\n":
                music_state = 1
                pygame.mixer.music.unpause()
                print("unpause")
            if res == "0\n":
                music_state = 0
                pygame.mixer.music.pause()
                print("pause")
 
except KeyboardInterrupt:
    ser.close()
    print('exit')

'''

button: always toggle
v:
    playing and v < 0.3: off
    not playing and v > 7: on

'''