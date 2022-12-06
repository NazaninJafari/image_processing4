import cv2
import numpy as np

video_cap = cv2.VideoCapture(0)

width  = int(video_cap.get(3))  #width
height = int(video_cap.get(4))  #height

save_video = cv2.VideoWriter('video_detectColors.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20, (width,height), 0)
#cv2.VideoWriter(file path, fourcc, fps, (w,h))

while True:
    
    ret, frame = video_cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    not_blur = gray_frame[190:290, 270:370]
    
    color = (0,0,0)
    
    if not ret:
        break

    frame_size = (width,height)
    # Using cv2.blur() method 
    frame_blur = cv2.blur(gray_frame, frame_size)
    frame_blur[190:290, 270:370] = not_blur
    colour = np.average(frame_blur[190:290, 270:370])

    #detect colour
    if colour > 190:
        Text = 'WHITE'
        cv2.putText(frame_blur , Text, (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )
    elif 90 <= colour <= 190:
        Text = 'GRAY'
        cv2.putText(frame_blur , Text, (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 ) 
    elif colour < 90:
        Text = 'BLACK'
        cv2.putText(frame_blur , Text, (50,40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2 )

    key = cv2.waitKey(1)
    if key == 27:
        break

    cv2.imshow('output', frame_blur)

video_cap.release()
cv2.destroyAllWindows()  