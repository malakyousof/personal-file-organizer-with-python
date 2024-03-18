import os
import shutil

# Define source and destination paths
source_path = r"C:\Users\dell\Downloads"
destination_path_courses = r"D:\courses"
destination_path_shows = r"D:\shows"
destination_path_college = r"D:\college"

# Check if the source path exists
if os.path.exists(source_path):
    # List all files in the source path
    files = os.listdir(source_path)
    
    # Iterate over each file
    for file in files:
        # Check if the file is a .rar file
        if os.path.isfile(os.path.join(source_path, file)) and file.lower().endswith(".rar"):
            # Construct the destination path for courses
            destination_file = os.path.join(destination_path_courses, file)
            # Move the file to the courses folder
            shutil.move(os.path.join(source_path, file), destination_file)
            print(f"Moved {file} to {destination_file}")
        
        # Check if the file is an .mp4 file
        elif os.path.isfile(os.path.join(source_path, file)) and file.lower().endswith(".mp4") :
            # Construct the destination path for shows
            destination_file = os.path.join(destination_path_shows, file)
            # Move the file to the shows folder
            shutil.move(os.path.join(source_path, file), destination_file)
            print(f"Moved {file} to {destination_file}")
        
        # Check if the file name contains the word 'lecture'
        elif "lecture" in file.lower():
            # Construct the destination path for college-related files
            destination_file = os.path.join(destination_path_college, file)
            # Move the file to the college folder
            shutil.move(os.path.join(source_path, file), destination_file)
            print(f"Moved {file} to {destination_file}")

    print("Files have been organized into respective folders.")
else:
    print("The specified source path does not exist.")
destination_path = r"D:\shows"

# Check if the source path exists
if os.path.exists(source_path):
    # List all directories in the source path
    folders = [folder for folder in os.listdir(source_path) if os.path.isdir(os.path.join(source_path, folder))]
    
    # Iterate over each folder
    for folder in folders:
        # Check if the folder name contains 'lecture', 'S0', or 'season'
        if ".S0" in folder.lower() or "season" in folder.lower():
            # Construct the destination path
            destination_folder = os.path.join(destination_path, folder)
            # Move the folder to the destination folder
            shutil.move(os.path.join(source_path, folder), destination_folder)
            print(f"Moved folder {folder} to {destination_folder}")
    print("'S0', or 'season' in their name have been moved to the shows folder.")
else:
    print("The specified source path does not exist.")
   