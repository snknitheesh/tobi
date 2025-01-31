import tobii_research as tr

def pupil_callback(pupil_data):
    print(f"Left Pupil Diameter: {pupil_data['left_pupil_diameter']}, Right Pupil Diameter: {pupil_data['right_pupil_diameter']}")

trackers = tr.find_all_eyetrackers()
if trackers:
    tracker = trackers[0]
    tracker.subscribe_to(tr.EYETRACKER_PUPIL_DATA, pupil_callback, as_dictionary=True)
    input("Press Enter to stop...")
    tracker.unsubscribe_from(tr.EYETRACKER_PUPIL_DATA, pupil_callback)

