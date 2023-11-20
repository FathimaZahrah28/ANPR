import cv2
import webbrowser

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    data, _, _ = detector.detectAndDecode(img)
    
    if data:
        if data.startswith('http') or data.startswith('https'):
            # Jika QR code berisi URL, buka di web browser
            webbrowser.open(data)
            break
        else:
            # Jika QR code berisi teks, tampilkan teksnya
            print("QR Code Text:", data)
            break

    cv2.imshow("YoWeScan", img)

    key = cv2.waitKey(1)
    if key == ord("q") or key == 27:
        break

cap.release()
cv2.destroyAllWindows()