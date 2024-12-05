import cv2
import numpy as np
from django.shortcuts import render
from .models import Usuario

def reconocer_rostro(request):
    # Carga las imágenes guardadas de usuarios
    usuarios = Usuario.objects.all()
    datos_rostros = []
    nombres = []

    for usuario in usuarios:
        rostro = cv2.imread(usuario.imagen_rostro.path, cv2.IMREAD_GRAYSCALE)
        datos_rostros.append(rostro)
        nombres.append(usuario.nombre)

    # Carga el modelo de reconocimiento
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(datos_rostros, np.array(range(len(nombres))))

    # Captura desde la cámara
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        detected_faces = faces.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in detected_faces:
            rostro = gray[y:y+h, x:x+w]
            label, confidence = face_recognizer.predict(rostro)
            cv2.putText(frame, nombres[label], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Reconocimiento facial', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return render(request, 'usuarios/reconocimiento.html', {})

