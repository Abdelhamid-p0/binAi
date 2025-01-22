from ultralytics import YOLO
import cv2

# Charger le modèle entraîné
model = YOLO("best.pt")  # Remplacez "best.pt" par le chemin de votre fichier .pt si nécessaire

# Ouvrir la webcam (index 0 pour la webcam par défaut)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Impossible d'ouvrir la webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur lors de la capture de la vidéo.")
        break

    # Effectuer la détection sur l'image capturée
    results = model(frame)

    # Annoter l'image avec les résultats
    annotated_frame = results[0].plot()

    # Afficher l'image annotée
    cv2.imshow("Détection en temps réel", annotated_frame)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()


# Charger le modèle entraîné
model = YOLO("best.pt")  # Remplacez "best.pt" par le chemin de votre fichier .pt si nécessaire

# Ouvrir la webcam (index 0 pour la webcam par défaut)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Impossible d'ouvrir la webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur lors de la capture de la vidéo.")
        break

    # Effectuer la détection sur l'image capturée
    results = model(frame)

    # Annoter l'image avec les résultats
    annotated_frame = results[0].plot()

    # Afficher l'image annotée
    cv2.imshow("Détection en temps réel", annotated_frame)

    # Quitter avec la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
