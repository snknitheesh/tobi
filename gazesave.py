import tobii_research as tr
import csv

# Open CSV file for writing
with open("gaze_data.csv", "w", newline="") as csvfile:
    fieldnames = ["timestamp", "left_x", "left_y", "right_x", "right_y"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    def gaze_callback(gaze_data):
        row = {
            "timestamp": gaze_data["device_time_stamp"],
            "left_x": gaze_data["left_gaze_point_on_display_area"][0],
            "left_y": gaze_data["left_gaze_point_on_display_area"][1],
            "right_x": gaze_data["right_gaze_point_on_display_area"][0],
            "right_y": gaze_data["right_gaze_point_on_display_area"][1]
        }
        writer.writerow(row)
        print(row)

    trackers = tr.find_all_eyetrackers()
    if trackers:
        tracker = trackers[0]
        tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_callback, as_dictionary=True)
        input("Press Enter to stop...")
        tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_callback)
