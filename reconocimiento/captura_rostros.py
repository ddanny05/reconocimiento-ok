import cv2
import os

# Crea un directorio para guardar imágenes
os.makedirs('rostros_capturados', exist_ok=True)

# Carga el modelo de detección facial
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Abre la cámara
cap = cv2.VideoCapture(0)

contador = 0
usuario_id = input("Introduce el ID del usuario: ")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        contador += 1
        rostro = frame[y:y+h, x:x+w]
        cv2.imwrite(f"rostros_capturados/usuario_{usuario_id}_{contador}.jpg", rostro)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Capturando rostros', frame)

    # Detiene la captura con 'q' o si tiene suficientes imágenes
    if cv2.waitKey(1) & 0xFF == ord('q') or contador >= 20:
        break

cap.release()
cv2.destroyAllWindows()
