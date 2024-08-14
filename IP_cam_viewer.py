import cv2

camera_url = 'rtsp://192.168.1.201/live.sdp' 
cap = cv2.VideoCapture(camera_url)

while True:
    ret, frame = cap.read()
    cv2.imshow('IP Camera Stream', frame)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
