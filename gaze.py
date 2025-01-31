import tobii_research as tr

def gaze_callback(gaze_data):
    left_eye = gaze_data['left_gaze_point_on_display_area']
    right_eye = gaze_data['right_gaze_point_on_display_area']
    print(f"Left Eye Gaze: {left_eye}, Right Eye Gaze: {right_eye}")

trackers = tr.find_all_eyetrackers()
if trackers:
    tracker = trackers[0]
    tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_callback, as_dictionary=True)
    input("Press Enter to stop...")
    tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_callback)

