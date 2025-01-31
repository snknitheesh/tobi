import tobii_research as tr
import time

gaze_start_time = None
stare_threshold = 1.0  # Time in seconds to trigger an action

def gaze_callback(gaze_data):
    global gaze_start_time
    gaze_x, gaze_y = gaze_data['left_gaze_point_on_display_area']

    if 0.4 < gaze_x < 0.6 and 0.4 < gaze_y < 0.6:  # Center of the screen
        if gaze_start_time is None:
            gaze_start_time = time.time()
        elif time.time() - gaze_start_time > stare_threshold:
            print("🚀 Staring at a point!")
            # Send command to robot
            gaze_start_time = None  # Reset timer
    else:
        gaze_start_time = None  # Reset if gaze moves away

trackers = tr.find_all_eyetrackers()
if trackers:
    tracker = trackers[0]
    tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_callback, as_dictionary=True)
    input("Press Enter to stop...")
    tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_callback)
