import cv2

try:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
except AttributeError:
    recognizer = cv2.face.LBPHFaceRecognizer_create() if cv2.__version__.startswith('4') else cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX
id = 0  # Starting ID from 0

# Replace the empty string with actual names
names = ['', 'avi']

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()

    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        try:
            id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

            if accuracy < 100:
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))

            print(f"ID: {id}, Accuracy: {accuracy}")
        except cv2.error as e:
            print(f"Error predicting face: {e}")

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()
