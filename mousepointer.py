import tobii_research as tr
import pyautogui

def gaze_callback(gaze_data):
    left_eye = gaze_data['left_gaze_point_on_display_area']
    screen_width, screen_height = pyautogui.size()
    
    x = int(left_eye[0] * screen_width)
    y = int(left_eye[1] * screen_height)

    pyautogui.moveTo(x, y)

trackers = tr.find_all_eyetrackers()
if trackers:
    tracker = trackers[0]
    tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_callback, as_dictionary=True)
    input("Press Enter to stop...")
    tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_callback)
