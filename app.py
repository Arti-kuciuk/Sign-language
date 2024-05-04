import streamlit as st
import cv2
from ultralytics import YOLO
import time


# Функция для обновления видео
def update_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        yield frame
    cap.release()


# Загрузка модели нейросети
model = YOLO("/Users/arti/Documents/PycharmProjects/sign_language/runs/detect/train12/weights/best.pt")

# Настройка приложения
st.set_page_config(page_title="Sign Language Recognition", layout="wide")
st.title("Sign Language Recognition")

# Отображение видео
video_placeholder = st.empty()

# Инициализация переменных
prev_label = None
last_file_label = ""
label_counters = {}
start_time = time.time()
is_running = False
recognized_letters = ""

# Добавление кнопок внизу экрана
start_button = st.button("Запустить распознавание")
pause_button = st.button("Пауза")

# Логика для кнопок
if start_button:
    is_running = True
    st.write("Распознавание запущено!")
elif pause_button:
    is_running = False
    st.write("Распознавание на паузе.")

# Отображение распознанных букв
recognized_text = st.empty()

# Основной цикл приложения
video_generator = update_video()
while is_running:
    # Обновление видео
    frame = next(video_generator)

    # Проверка на None перед отображением изображения
    if frame is not None:
        # Обработка нейросети
        results = model.predict(source=frame, imgsz=640, conf=0.7)
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                label = f"{result.names[int(box.cls[0])]}"
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

                if label != prev_label:
                    if prev_label:
                        label_counters[prev_label] += 1
                    prev_label = label
                    label_counters[prev_label] = 1
                    recognized_letters += label
                else:
                    label_counters[prev_label] += 1

        if label_counters and time.time() - start_time > 1:
            max_label = max(label_counters, key=label_counters.get)
            if label_counters[max_label] >= 5 and max_label != last_file_label:
                last_file_label = max_label
                cleaned_letters = [recognized_letters[0]]  # Сохраняем первую букву
                for i in range(1, len(recognized_letters)):
                    if recognized_letters[i] != recognized_letters[i - 1]:  # Проверяем на совпадение с предыдущей буквой
                        cleaned_letters.append(recognized_letters[i])
                recognized_text.markdown(f"<h3>Recognized letters: {''.join(cleaned_letters)}</h3>", unsafe_allow_html=True)
            label_counters = {}
            prev_label = None
            start_time = time.time()

        # Преобразование кадра в формат, который можно отобразить в Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(frame, channels="RGB", use_column_width=True)
