import cv2
import numpy as np
from ultralytics import YOLO
import time

model = YOLO("/Users/arti/Documents/PycharmProjects/sign_language/runs/detect/train12/weights/best.pt")
cap = cv2.VideoCapture(0)

# Очистка файла перед записью
with open("detected_objects.txt", "w") as f:
    pass

prev_label = None
last_file_label = ""
label_counters = {}
start_time = time.time()

# Получение последней буквы из файла
with open("detected_objects.txt", "r") as f:
    lines = f.readlines()
    if lines:
        last_file_label = lines[-1].strip()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (1920, 1080))
    # results = model(frame)
    results = model.predict(source=frame, imgsz=640, conf=0.5)

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            label = f"{result.names[int(box.cls[0])]}"   # {box.conf[0]:.2f}
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
            print(label)

            if label != prev_label:
                if prev_label:
                    label_counters[prev_label] += 1
                prev_label = label
                label_counters[prev_label] = 1
            else:
                label_counters[prev_label] += 1

    if time.time() - start_time > 1:
        if label_counters:
            max_label = max(label_counters, key=label_counters.get)
            if label_counters[max_label] >= 7 and max_label != last_file_label:
                with open("detected_objects.txt", "a") as f:
                    f.write(max_label)
                    last_file_label = max_label
        label_counters = {}
        prev_label = None
        start_time = time.time()

    cv2.imshow("Распознавание языка жестов", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Удаление повторяющихся букв в конце работы программы
with open("detected_objects.txt", "r") as f:
    lines = f.readlines()
    if lines:
        cleaned_lines = [lines[0]]  # Сохраняем первую букву
        for i in range(1, len(lines)):
            if lines[i] != lines[i - 1]:  # Проверяем на совпадение с предыдущей буквой
                cleaned_lines.append(lines[i])
        with open("detected_objects.txt", "w") as f:
            for line in cleaned_lines:
                f.write(line)
        print("Повторяющиеся буквы удалены")
