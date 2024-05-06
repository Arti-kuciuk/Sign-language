Для локального запуска нейронной сети откройте файл "test.py" в любой ide для Python (лучще всего открыть в PyCharm), установите библиотеки командами:
pip install opencv-python
pip install numpy
pip install ultralytics
Скачайте файл best.pt, и укажите к нему путь в строке №6.
Запустите код, у вас откроется окно с камерой, откройте файл Limbajul semnelor moldovenesc.jpg и повторите любой жест с картинки,
вокруг вашей руки программа нарисует прямоугольник с расспознанной буквой, после распознования всех нужных вам букв закройте файл нажав на английскую букву "Q"
В вашей ideffdnjvfnbxtcrb создастся файл detected_objects.txt в котором будут все ваши распознанные буквы или слова.

Для запуска streamlit приложения в том же проекте откройте файл app.py, установите библиотеку streamlit: pip install streamlit, в строке № 19 укажите путь к best.pt,
запустите код, вставьте в терминал команду которую вам выведет программа (пример команды: "streamlit run /Users/arti/Documents/PycharmProjects/sign_language/app.py")
в окне в браузере нажмите на кнопку "запустить распознование", откроется окно с камерой, а ниже будут выводиться распознанные буквы. 




Pentru a rula rețeaua neuronală la nivel local, deschideți fișierul "test.py" în orice ide pentru Python (cel mai bine este să îl deschideți în PyCharm), instalați bibliotecile cu ajutorul comenzilor:
pip install opencv-python
pip install numpy
pip install ultralytics
Descărcați fișierul best.pt și specificați calea către acesta în linia #6.
Rulați codul, se va deschide o fereastră cu o cameră, deschideți fișierul Limbajul semnelor moldovenesc.jpg și repetați orice gest din imagine,
în jurul mâinii, softul va desena un dreptunghi cu litera recunoscută, după recunoașterea tuturor literelor de care aveți nevoie, închideți fișierul făcând clic pe litera engleză "Q".
În ideffdnjvvfnbxtcrb dvs. va fi creat fișierul detected_objects.txt în care vor fi toate literele sau cuvintele recunoscute.

Pentru a rula aplicația streamlit în același proiect, deschideți fișierul app.py, instalați biblioteca streamlit: pip install streamlit, în linia #19 specificați calea către best.pt,
rulați codul, lipiți comanda pe care programul v-o va afișa în terminal (exemplu de comandă: "streamlit run /Users/arti/Documents/PycharmProjects/sign_language/app.py").
în fereastra din browser faceți clic pe butonul "run recognition", se va deschide o fereastră cu o cameră și literele recunoscute vor fi afișate mai jos. 




To run the neural network locally, open the file "test.py" in any ide for Python (best to open in PyCharm), install the libraries with the commands:
pip install opencv-python
pip install numpy
pip install ultralytics
Download the file best.pt, and specify the path to it in line #6.
Run the code, a window with a camera will open, open the file Limbajul semnelor moldovenesc.jpg and repeat any gesture from the picture,
around your hand the software will draw a rectangle with the recognised letter, after recognising all the letters you need, close the file by clicking on the English letter "Q".
In your ideffdnjvfnbxtcrb will be created file detected_objects.txt in which will be all your recognised letters or words.

To run the streamlit application in the same project, open the app.py file, install the streamlit library: pip install streamlit, in line #19 specify the path to best.pt,
run the code, paste the command that the programme will display to you in the terminal (example command: "streamlit run /Users/arti/Documents/PycharmProjects/sign_language/app.py").
in the window in your browser click on the "run recognition" button, a window with a camera will open and the recognised letters will be displayed below. 
