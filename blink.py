import tobii_research as tr
import time

last_blink_time = 0
double_blink_threshold = 0.3  # Max time between blinks for a "double blink"

def blink_callback(pupil_data):
    global last_blink_time
    left_pupil = pupil_data['left_pupil_diameter']
    right_pupil = pupil_data['right_pupil_diameter']
    
    if left_pupil < 2.0 and right_pupil < 2.0:  # Blink detected
        current_time = time.time()
        if current_time - last_blink_time < double_blink_threshold:
            print("🛑 Double Blink Detected! Stopping Robot.")
            # Send stop command to robot
        else:
            print("➡️ Single Blink Detected! Moving Forward.")
            # Send move forward command
        last_blink_time = current_time

trackers = tr.find_all_eyetrackers()
if trackers:
    tracker = trackers[0]
    tracker.subscribe_to(tr.EYETRACKER_PUPIL_DATA, blink_callback, as_dictionary=True)
