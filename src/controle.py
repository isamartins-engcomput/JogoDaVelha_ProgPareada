import mediapipe

class Controle:
    def __init__(self):
        self.pacote = mediapipe.solutions.hands
        self.mao = self.pacote.Hands()

    def detectar_maos(self, frame):
        resultado = self.mao.process(frame)
        lista_maos = resultado.multi_hand_landmarks
        
        if lista_maos is not None:
            for hand_landmarks in resultado.multi_hand_landmarks:
                for landmark in hand_landmarks.landmark:
                    return landmark.x * frame.shape[1], landmark.y * frame.shape[0]
        
        return 0, 0