import cv2
import time
from gaze_tracking import GazeTracking
import numpy as np

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

blink_count = 0
row_blinks = 0
column_blinks = 0
last_blink_time = time.time()
detecting_row = True 
Sentence = ""

blink_matrix = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y'],
    ['Z', ' ', '1', '2', '3'],
]


while True:

    _, frame = webcam.read()
    gaze.refresh(frame)

    frame = gaze.annotated_frame()


    if gaze.is_blinking():
        current_time = time.time()
        if current_time - last_blink_time > 0.3:  
            last_blink_time = current_time

            if detecting_row:
                if blink_count >= 6:
                    blink_count = 1
                else:
                    blink_count += 1
                row_blinks = blink_count
            else:
                if blink_count >= 5:
                    blink_count = 1
                else:
                    blink_count += 1
                column_blinks = blink_count


    elif time.time() - last_blink_time >= 2:  
        if blink_count > 0:
            if detecting_row:
                detecting_row = False  
            else:
                Sentence += blink_matrix[row_blinks - 1][column_blinks - 1]


                row_blinks = 0
                column_blinks = 0
                detecting_row = True  


            blink_count = 0

    visual_frame = 255 * np.ones((600, 400, 3), dtype=np.uint8) 

    for i, row in enumerate(blink_matrix):
        for j, letter in enumerate(row):
            if i + 1 == row_blinks:
                color = (0, 255, 0)  
                if not detecting_row and j + 1 == column_blinks:
                    color = (255, 0, 0)  
            elif not detecting_row and j + 1 == column_blinks:
                color = (255, 0, 0)  
            else:
                color = (0, 0, 0)  

            
            cv2.putText(visual_frame, letter, (50 + j * 60, 100 + i * 60), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    
    cv2.putText(frame, f"{Sentence}", (40, 70), cv2.FONT_HERSHEY_DUPLEX, 1.0, (147, 58, 31), 2)

    cv2.imshow("Blink Matrix Encoding", frame)
    cv2.imshow("Blink Matrix Visualization", visual_frame)

    if cv2.waitKey(1) == 27:
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()
