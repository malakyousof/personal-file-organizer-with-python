import os
import shutil

source_path_college = r"D:\college"
dc1 = r"D:\college\AI"
dc2 = r"D:\college\algorithm"  # Corrected typo here
dc3 = r"D:\college\computer network"
dc4 = r"D:\college\electronics"

if os.path.exists(source_path_college):
    # List all files in the source path
    files = [file for file in os.listdir(source_path_college) if os.path.isfile(os.path.join(source_path_college, file))]
    
    # Iterate over each file
    for file in files:
        # Check if the file name contains 'Algorithm' or 'Analysis'
        if "algorithm" in file.lower() or "analysis" in file.lower():
            # Construct the destination path
            destination_file2 = os.path.join(dc2, file)
            
            # Move the file to the destination folder
            shutil.move(os.path.join(source_path_college, file), destination_file2)
            print(f"Moved file {file} to {destination_file2}")
    print("'Algorithm' or 'Analysis' files have been moved to the specified destination folder.")
else:
    print("The specified source path does not exist.")


if os.path.exists(source_path_college):
    # List all files in the source path
    files = [file for file in os.listdir(source_path_college) if os.path.isfile(os.path.join(source_path_college, file))]
    
    # Iterate over each file
    for file in files:
        # Check if the file name contains 'AI' or 'Artificial Intelligence'
        if "AI" in file.upper() or "ARTIFICIAL INTELLIGENCE" in file.upper():
            # Construct the destination path
            destination_file1 = os.path.join(dc1, file)
            
            # Move the file to the destination folder
            shutil.move(os.path.join(source_path_college, file), destination_file1)
            print(f"Moved file {file} to {destination_file1}")
        
        # Check if the file name contains 'Computer Networks' or 'Computer Network'
        elif "COMPUTER NETWORKS" in file.upper() or "COMPUTER NETWORK" in file.upper():
            # Construct the destination path
            destination_file3 = os.path.join(dc3, file)
            
            # Move the file to the destination folder
            shutil.move(os.path.join(source_path_college, file), destination_file3)
            print(f"Moved file {file} to {destination_file3}")
    
    print("Files related to AI and Computer Networks have been moved to the specified destination folders.")
else:
    print("The specified source path does not exist.")



source_path_college = r"D:\college"
dc4 = r"D:\college\electronics"

if os.path.exists(source_path_college):
    # List all files in the source path
    files = [file for file in os.listdir(source_path_college) if os.path.isfile(os.path.join(source_path_college, file))]
    
    # Iterate over each file
    for file in files:
        # Convert the file name to lowercase
        lowercase_file = file.lower()
        
        # Check if the lowercase file name contains 'electronics'
        if "electronics" in lowercase_file:
            # Construct the destination path
            destination_file4 = os.path.join(dc4, file)
            
            # Move the file to the destination folder
            shutil.move(os.path.join(source_path_college, file), destination_file4)
            print(f"Moved file {file} to {destination_file4}")
    
    print("Files related to electronics have been moved to the specified destination folder.")
else:
    print("The specified source path does not exist.")