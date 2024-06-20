import os
import shutil
import random

# Path to the folder containing normal ECG images
# The use of a backslash \ is treated as an escape character, so I could use double backslashes \\
# or use a raw string by adding an 'r' prefix before the string.
normal_folder = r"C:\Users\alexr\OneDrive\Documents\CSC 695 - Independent Study\dataset5\Abnormal heartbeat"

# Output folders
train_folder = r"C:\Users\alexr\OneDrive\Documents\CSC 695 - Independent Study\dataset5\Training"
validation_folder = r"C:\Users\alexr\OneDrive\Documents\CSC 695 - Independent Study\dataset5\Validation"
test_folder = r"C:\Users\alexr\OneDrive\Documents\CSC 695 - Independent Study\dataset5\Testing"

# List all image filenames
normal_images = os.listdir(normal_folder)

# Set a random seed for reproducibility
random.seed(42)

# Shuffle the list of images
random.shuffle(normal_images)

# Split ratios
train_ratio = 0.7
validation_ratio = 0.15
test_ratio = 0.15

# Split images into train, validation, and test sets
train_count = int(len(normal_images) * train_ratio)
validation_count = int(len(normal_images) * validation_ratio)

train_images = normal_images[:train_count]
validation_images = normal_images[train_count:(train_count + validation_count)]
test_images = normal_images[(train_count + validation_count):]

# Move images to the respective folders
for image in train_images:
    shutil.move(os.path.join(normal_folder, image), os.path.join(train_folder, image))

for image in validation_images:
    shutil.move(os.path.join(normal_folder, image), os.path.join(validation_folder, image))

for image in test_images:
    shutil.move(os.path.join(normal_folder, image), os.path.join(test_folder, image))
