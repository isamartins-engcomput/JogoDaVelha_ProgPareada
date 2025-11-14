import cv2

class Camera:
    def __init__(self, id_camera):
        self.id_camera = id_camera
        self.video_cap = cv2.VideoCapture(self.id_camera)
        # validar abertura da camera depois
        
    def get_frame(self):
        ret, frame = self.video_cap.read()
        if ret:
            return frame
        return None
    
    def get_resolucao(self):
        return self.video_cap.get(cv2.CAP_PROP_FRAME_WIDTH), self.video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    def set_nova_resolucao(self, nova_largura, nova_altura):
        self.video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, nova_altura)
        self.video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, nova_largura)
    
    def __str__(self):
        return  str(self.id_camera)
    