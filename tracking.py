import os
import numpy as np
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from ultralytics import YOLO
import cv2

# YOLOv8 modelini yükle
model = YOLO('yolov8n.pt')

# Video kaynağını aç
video_source = 'test.mp4'  # Video dosyasının yolu
cap = cv2.VideoCapture(video_source)

# Video çıktısı için hazırlık
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, 
                      (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

# Video üzerinde kare kare işlem yap
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Video bittiğinde çıkış yap

    # Model ile tespit yap
    results = model(frame)

    # Her tespitin bounding box koordinatlarını, confidence ve sınıf isimlerini al
    for box, conf, cls_id in zip(results[0].boxes.xyxy, results[0].boxes.conf, results[0].boxes.cls):
        x1, y1, x2, y2 = map(int, box)  # Koordinatları int formatına çevir
        score = float(conf)  # Confidence score'u float olarak al
        cls_name = model.names[int(cls_id)]  # Sınıf ismini al (örneğin 'car')

        # Etiket: sınıf ismi ve güven skoru
        label = f'{cls_name} {score:.2f}'
        label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)

        # Beyaz arka plan kutusu
        cv2.rectangle(frame, (x1, y1 - label_size[1] - 10), (x1 + label_size[0], y1), (255, 255, 255), -1)

        # Çerçeve çiz
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

        # Nesne adı ve doğruluk skoru yaz
        cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)  # Beyaz kutunun üzerine siyah yazı

    # İşlenmiş kareyi video çıktısına ekle
    out.write(frame)

    # Her kareyi ekranda göster (isteğe bağlı)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video işlemi tamamlandığında kaynakları serbest bırak
cap.release()
out.release()
cv2.destroyAllWindows()
