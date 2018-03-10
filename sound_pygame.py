import pygame.mixer
import time


def main():
    pygame.mixer.init(frequency = 44100 )
    pygame.mixer.music.load("警報音声.wav")        # 音楽ファイルの読み込み
    pygame.mixer.music.play(-1)                   # 音楽の再生回数(ループ再生)
    time.sleep(10)                                # 音楽の再生時間
    pygame.mixer.music.stop()                     # 再生の終了


if __name__ == '__main__':
    main()

