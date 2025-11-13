import cv2
from camera import Camera
from tabuleiro import Tabuleiro

largura = 1280
altura = 720

minha_camera = Camera(2)
meu_tabuleiro = Tabuleiro()

minha_camera.set_nova_resolucao(largura, altura)

print(minha_camera.get_resolucao())

while True:
    frame = minha_camera.get_frame()
    
    if frame is not None:
        frame = meu_tabuleiro.desenhar_tabuleiro(frame)
        
        cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break