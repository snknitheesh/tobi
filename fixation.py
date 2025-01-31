import tobii_research as tr

def fixation_callback(fixation_data):
    print(f"Fixation at: {fixation_data['fixation_point_on_display_area']}")

trackers = tr.find_all_eyetrackers()
if trackers:
    tracker = trackers[0]
    tracker.subscribe_to(tr.EYETRACKER_FIXATION_DATA, fixation_callback, as_dictionary=True)
    input("Press Enter to stop...")
    tracker.unsubscribe_from(tr.EYETRACKER_FIXATION_DATA, fixation_callback)
