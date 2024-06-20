import cv2
import os

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getUnconnectedOutLayersNames()

# Replace with the path to your labeled images and corresponding JSON annotations
image_folder = (r"C:\Users\alexr\OneDrive\Documents\CSC 695 - Independent Study\dataset5\Abnormal heartbeat")
json_folder = (r"C:\Users\alexr\OneDrive\Documents\CSC 695 - Independent Study\dataset5\Abnormal heartbeat\Annotations")

# Load annotated images and corresponding JSON annotations
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

for image_file in image_files:
    # Load image
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Load JSON annotations
    json_file = os.path.join(json_folder, os.path.splitext(image_file)[0] + '_annotations.json')
    with open(json_file, 'r') as f:
        annotations = json.load(f)

    # Convert annotations to YOLO format
    yolo_annotations = []
    for annotation in annotations:
        x_center = (annotation['x'] + annotation['width'] / 2) / width
        y_center = (annotation['y'] + annotation['height'] / 2) / height
        w = annotation['width'] / width
        h = annotation['height'] / height
        yolo_annotations.append([x_center, y_center, w, h])

    # Run YOLO on the image
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward(layer_names)

    # Post-process the detections
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Adjust confidence threshold as needed
                box = obj[0:4] * np.array([width, height, width, height])
                x, y, w, h = box.astype(int)
                label = lead_labels[class_id]

                # Draw bounding box on the image
                cv2.rectangle(image, (x, y), (x + w, y + h), lead_colors[class_id], 2)
                cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, lead_colors[class_id], 2)

    # Display the annotated image
    cv2.imshow("Annotated Image", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
