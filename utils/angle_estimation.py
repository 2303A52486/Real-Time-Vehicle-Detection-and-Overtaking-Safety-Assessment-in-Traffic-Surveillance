def calculate_overtaking_angle(bbox):
    obj_center = (bbox[0] + bbox[2]) / 2
    frame_center = CAMERA_CONFIG["frame_width"] / 2
    mm_per_pixel = CAMERA_CONFIG["sensor_width"] / CAMERA_CONFIG["frame_width"]
    offset_mm = (obj_center - frame_center) * mm_per_pixel
    return round(np.degrees(np.arctan(offset_mm / CAMERA_CONFIG["focal_length"])), 2)

# Angle Accuracy Calculation
def compute_angle_accuracy(predicted_angle, true_angle=0):
    error = abs(predicted_angle - true_angle)
    accuracy = max(0, 100 - (error / 90) * 100)
    return round(accuracy, 2)