import cv2
import os
import json
import numpy as np 

drawing = False
top_left_pt = (-1, -1)
bottom_right_pt = (-1, -1)
annotations = []

# Predefined labels for 12 leads
lead_labels = ["Lead I", "Lead II", "Lead III", "Lead aVR", "Lead aVL", "Lead aVF",
               "Lead V1", "Lead V2", "Lead V3", "Lead V4", "Lead V5", "Lead V6", 
               "Timeframe"]

# Initial colors for each lead
lead_colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255),
               (128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0), (0, 128, 128), (128, 0, 128),
               (0, 0, 0)]

current_color = lead_colors[0]
current_label = lead_labels[0]

# Index to keep track of the current image
current_image_index = 0
current_color_index = 0 
current_label_index = 0

def draw_rectangle(event, x, y, flags, param):
    global drawing, top_left_pt, bottom_right_pt, current_color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        top_left_pt = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        bottom_right_pt = (x, y)

        cv2.rectangle(image, top_left_pt, bottom_right_pt, current_color, 2)
        label = current_label
        new_annotation = {'x': top_left_pt[0], 'y': top_left_pt[1],
                          'width': bottom_right_pt[0] - top_left_pt[0],
                          'height': bottom_right_pt[1] - top_left_pt[1],
                          'label': label,
                          'color': current_color}
        annotations.append(new_annotation)
        cv2.putText(image, label, (top_left_pt[0], top_left_pt[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, current_color, 2)
        cv2.imshow("Annotated Image", image)

def load_image():
    global image, annotations, current_image_index
    annotations = []  # Reset annotations for the new image

    # Ensure the index stays within bounds
    current_image_index = max(0, min(current_image_index, len(image_files) - 1))

    # Load the current image
    image_path = os.path.join(image_folder, image_files[current_image_index])
    image = cv2.imread(image_path)

    # Resize the image for display
    height, width = image.shape[:2]
    max_height = 950  # Adjust as needed
    if height > max_height:
        scale = max_height / height
        new_width = int(width * scale)
        new_height = int(height * scale)
        image = cv2.resize(image, (new_width, new_height))

def load_next_image():
    global image, annotations, current_image_index
    current_image_index += 1
    load_image()

def load_previous_image():
    global image, annotations, current_image_index
    current_image_index -= 1
    load_image()

def save_annotations_to_json(image_path, annotations):
    global current_image_index
    json_folder = os.path.join(os.path.dirname(image_path), "Annotations")
    os.makedirs(json_folder, exist_ok=True)

    # Convert current_image_index to a string
    image_index_str = str(current_image_index)

    json_filename = os.path.splitext(image_index_str)[0] + '_annotations.json'
    json_path = os.path.join(json_folder, json_filename)

    with open(json_path, 'w') as json_file:
        json.dump(annotations, json_file)

    print(f"Annotations saved at: {json_path}")

# Replace this with the path to your image folder
image_folder = (r"C:\Users\alexr\OneDrive\Documents\CSC 695 - Independent Study\dataset5\Abnormal heartbeat")
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

# Ensure the index stays within bounds
current_image_index = max(0, min(current_image_index, len(image_files) - 1))

# Load an example image
image_path = os.path.join(image_folder, image_files[current_image_index])
image = cv2.imread(image_path)

# Set up the window and callback function
cv2.namedWindow("Annotated Image")
cv2.setMouseCallback("Annotated Image", draw_rectangle)

# Resize the image for display
height, width = image.shape[:2]
max_height = 950  # Adjust as needed
if height > max_height:
    scale = max_height / height
    new_width = int(width * scale)
    new_height = int(height * scale)
    image = cv2.resize(image, (new_width, new_height))

while True:
    # Display the image
    cv2.imshow("Annotated Image", image)

    # Wait for a key press
    key = cv2.waitKeyEx(0)

    # Check for key events
    if key in range(ord('1'), ord('1') + len(lead_labels)):
        current_label = lead_labels[key - ord('1')]
        current_color = lead_colors[key - ord('1')]

    elif key == ord('s'):
        annotated_image_filename = os.path.basename(image_path)
        annotated_image_path = os.path.join(os.path.dirname(image_path), "Annotated", annotated_image_filename)
        cv2.imwrite(annotated_image_path, image)
        print(f"Annotated image saved at: {annotated_image_path}")

        # Save annotations to JSON
        save_annotations_to_json(image_path, annotations)

    elif key == ord('c'):  # Change color on 'c' key
        current_color = lead_colors[current_color_index] # Change to the desired color
        current_color_index = (current_color_index + 1) % len(lead_colors)
        current_label = lead_labels[current_label_index]
        current_label_index = (current_label_index + 1) % len(lead_labels)

    elif key == 27:  # 'Esc' key to exit
        break

    elif key == ord('d'):  #  Press 'd' to load the next image
        load_next_image()

    elif key == ('a'):  #  Press 'a' to load the previous image
        load_previous_image()

cv2.namedWindow("Annotated Image")
cv2.setMouseCallback("Annotated Image", draw_rectangle)

# Save the annotations to a file or database
print("Annotations:", annotations)

# Release resources
cv2.destroyAllWindows()
