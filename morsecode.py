import cv2
from gaze_tracking import GazeTracking
import time

MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.....': '  '
}

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

sequence = ""  
output_text = ""  
last_blink_time = time.time()
blink_duration = 0
blink_start_time = None


while True:

    _, frame = webcam.read()
    gaze.refresh(frame)
    frame = gaze.annotated_frame()

    if gaze.is_blinking():
        if blink_start_time is None: 
            blink_start_time = time.time()
        blink_duration = time.time() - blink_start_time
    else:
        if blink_start_time is not None:  
            if blink_duration < 0.5:  
                sequence += '.'
            elif blink_duration >= 0.5:  
                sequence += '-'
            blink_start_time = None 
            blink_duration = 0
            last_blink_time = time.time()

    if time.time() - last_blink_time > 2 and sequence:
        decoded_letter = MORSE_CODE_DICT.get(sequence, '')
        output_text += decoded_letter
        sequence = ""  


    cv2.putText(frame, f"Sequence: {sequence}", (20, 60), cv2.FONT_HERSHEY_DUPLEX, 0.6, (147, 58, 31), 1)
    cv2.putText(frame, f"Output: {output_text.strip()}", (20, 90), cv2.FONT_HERSHEY_DUPLEX, 0.6, (147, 58, 31), 1)


    cv2.imshow("Morse Code Typing", frame)


    if cv2.waitKey(1) == 27:  
        break

# Cleanup
webcam.release()
cv2.destroyAllWindows()
