import cv2
from camera import Camera
from tabuleiro import Tabuleiro
from controle import Controle
from threading import Thread
import time

def cronometro_segundos():
    for i in range(10):
        time.sleep(1)
        print(i) 

def controle_cenario():
    largura = 1280
    altura = 720

    minha_camera = Camera(0)
    meu_tabuleiro = Tabuleiro()

    minha_camera.set_nova_resolucao(largura, altura)

    print(minha_camera.get_resolucao())

    minha_mao = Controle()

    while True:
        frame = minha_camera.get_frame()
        
        if frame is not None:
            x, y = minha_mao.detectar_maos(frame)
            frame = meu_tabuleiro.desenhar_tabuleiro(frame)
            cv2.circle(frame, (int(x), int(y)), 50, (0, 255, 0), -1)
            
            cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    return
   

if __name__ == "__main__":
    tarefa1 = Thread(target=controle_cenario,)
    tarefa2 = Thread(target=cronometro_segundos)
    
    tarefa1.start()
    tarefa2.start()
    
    tarefa1.join()
    tarefa2.join()
    
    
    