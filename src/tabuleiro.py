import cv2

class Tabuleiro:
    def __init__(self):
        pass
        
    def desenhar_tabuleiro(self, frame):
        largura_casinha = int(frame.shape[1] / 3)
        altura_casinha = int(frame.shape[0] / 3)
        cv2.line(frame, (0,altura_casinha), (frame.shape[1], altura_casinha), (255, 0, 255), thickness=5)
        cv2.line(frame, (0,(2 * altura_casinha)), (frame.shape[1], (2 * altura_casinha)), (255, 0, 255), thickness=5)
        cv2.line(frame, (largura_casinha,0), (largura_casinha, frame.shape[0]), (255, 0, 255), thickness=5)
        cv2.line(frame, ((2 * largura_casinha),0), ((2 * largura_casinha), frame.shape[0]), (255, 0, 255), thickness=5)
        return frame