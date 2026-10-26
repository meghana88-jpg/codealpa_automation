
import os
import shutil

# Define source and destination folders
source_folder = os.path.join(os.getcwd(), "Source")
destination_folder = os.path.join(os.getcwd(), "Destination")

print("Starting JPG Image Automation...")
print("Source folder:", source_folder)
print("Destination folder:", destination_folder)

# Check whether the Source folder exists
if not os.path.isdir(source_folder):
    print("Error: Source folder not found!")
else:
    # Create Destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Get all files from Source
    files = os.listdir(source_folder)

    moved = 0

    # Move JPG and JPEG images
    for filename in files:
        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(
                destination_folder, filename
            )

            # Avoid overwriting an existing file
            if os.path.exists(destination_path):
                print("Skipped (already exists):", filename)
                continue

            shutil.move(source_path, destination_path)
            print("Moved:", filename)S
            moved += 1

    print("--------------------------------")
    print("Total images moved:", moved)
    print("Automation completed successfully!")
