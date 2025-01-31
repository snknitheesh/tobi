import tobii_research as tr

# Find connected eye trackers
found_trackers = tr.find_all_eyetrackers()

if found_trackers:
    tracker = found_trackers[0]
    print(f"Connected to: {tracker.model} at {tracker.address}")

    # Callback function for gaze data
    def gaze_data_callback(gaze_data):
        print("Gaze Data:", gaze_data)

    # Subscribe to gaze data
    tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
else:
    print("No eye tracker found.")
