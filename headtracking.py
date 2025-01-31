import tobii_research as tr

def head_callback(head_data):
    print(f"Head Position: {head_data['head_position_from_eye_tracker']}")

trackers = tr.find_all_eyetrackers()
if trackers:
    tracker = trackers[0]
    tracker.subscribe_to(tr.EYETRACKER_HEAD_POSE, head_callback, as_dictionary=True)
    input("Press Enter to stop...")
    tracker.unsubscribe_from(tr.EYETRACKER_HEAD_POSE, head_callback)
