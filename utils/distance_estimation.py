def calculate_distance(bbox, label):
    width_map = {
        "car": CAMERA_CONFIG["car_width"],
        "truck": CAMERA_CONFIG["truck_width"],
        "bus": CAMERA_CONFIG["bus_width"],
        "motorcycle": 0.8
    }
    real_width = width_map.get(label.lower(), 1.8)
    pixel_width = bbox[2] - bbox[0]
    return round((real_width * CAMERA_CONFIG["focal_length"]) / pixel_width, 2)
