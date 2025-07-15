# vehicle classes 
VEHICLE_CLASSES = {3: "car", 4: "motorcycle", 6: "bus", 8: "truck"}

# Define colors for vehicle classes
CLASS_COLORS = {
    3: (0, 255, 255),       # Yellow
    8: (255, 0, 0),     # Blue
    6: (0, 0, 255),       # Red
    4: (255, 255, 0),  # Cyan
    "default":(0, 255, 0)  # Green
}

def draw_boxes(frame, boxes, labels, scores):
    for box, label, score in zip(boxes, labels, scores):
        if label.item() in VEHICLE_CLASSES and score.item() > 0.5:
            x1, y1, x2, y2 = map(int, box)
            cls_id = label.item()
            color = CLASS_COLORS.get(cls_id, CLASS_COLORS['default'])
            class_name = VEHICLE_CLASSES[cls_id]
            distance = calculate_distance((x1, y1, x2, y2), class_name)
            angle = calculate_overtaking_angle((x1, y1, x2, y2))
            angle_accuracy = compute_angle_accuracy(angle)
            label_text = f"{class_name}, D:{distance:.2f}m, A:{angle:.2f}° | Acc:{angle_accuracy:.2f}%"
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label_text, (x1, max(y1 - 10, 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return frame