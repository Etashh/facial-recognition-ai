import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image
import random

dataset_base_path = os.path.join(os.getcwd(), 'data')
IMG_HEIGHT = 48
IMG_WIDTH = 48

sub_dirs_to_process = ['train', 'test', 'val']

emotion_labels = {
    'angry': 0,
    'disgust': 1,
    'fear': 2,
    'happy': 3,
    'neutral': 4,
    'sad': 5,
    'surprise': 6
}
label_to_emotion = {value: key for key, value in emotion_labels.items()}
all_images = []
all_labels = []

print("Commencing first stage (Data Preprocessing)")
for sub_dir in sub_dirs_to_process:
    current_path = os.path.join(dataset_base_path, sub_dir)
    if not os.path.exists(current_path):
        print(f"Warning: Directory '{current_path}' not found. Skipping.")
        continue

    print(f"Processing images in: {current_path}")
    for emotion_folder_name in os.listdir(current_path):
        emotion_folder_path = os.path.join(current_path, emotion_folder_name)

        if os.path.isdir(emotion_folder_path):
            try:
                numerical_label = int(emotion_folder_name)

                if 0 <= numerical_label <= 6:
                    label = numerical_label
                    emotion_name_for_print = label_to_emotion.get(label, f"Unknown (ID: {label})")
                    print(f"  Processing emotion: {emotion_name_for_print} (Label: {label})")

                    for image_filename in os.listdir(emotion_folder_path):
                        if image_filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                            image_path = os.path.join(emotion_folder_path, image_filename)

                            try:
                                img = Image.open(image_path)
                                img = img.convert('L')
                                img = img.resize((IMG_WIDTH, IMG_HEIGHT))
                                img_array = np.array(img) / 255.0
                                img_flattened = img_array.flatten()
                                all_images.append(img_flattened)
                                all_labels.append(label)
                            except Exception as e:
                                print(f"Error processing image {image_path}: {e}")
                else:
                    print(
                        f"  Found folder: '{emotion_folder_name}' but its numerical value ({numerical_label}) is outside the expected emotion label range (0-6). Skipping.")
            except ValueError:
                print(f"  Found non-numeric folder: '{emotion_folder_name}'. Skipping.")

X = np.array(all_images)
y = np.array(all_labels)

print(f"\nPreprocessing complete!")
print(f"Total images processed (X shape): {X.shape}")
print(f"Total labels processed (y shape): {y.shape}")

if X.shape[0] > 0:
    print(f"Example of X (first 5 features of first image):\n{X[0, :5]}")
    print(f"Example of y (first 5 labels): {y[:5]}")
else:
    print("No valid images were loaded into X and y.")

print("\nDemonstrating random image selection:")
if len(X) > 0:
    num_images_to_display = 2

    plt.figure(figsize=(num_images_to_display * 2, 4))

    for i in range(num_images_to_display):
        if len(X) > 0:
            random_index = random.randint(0, len(X) - 1)
            random_image_flattened = X[random_index]
            random_label = y[random_index]

            random_image_2d = random_image_flattened.reshape((IMG_HEIGHT, IMG_WIDTH))

            emotion_name = label_to_emotion.get(random_label, "Unknown")

            plt.subplot(1, num_images_to_display, i + 1)
            plt.imshow(random_image_2d, cmap='gray')
            plt.title(f"{emotion_name}\n(ID: {random_label})")
            plt.axis('off')
        else:
            print("No more images to display.")
            break

    # plt.tight_layout()
    plt.show()
else:
    print("No images were processed. Check your dataset path and structure.")
