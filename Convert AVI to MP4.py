# Import libraries used to convert video files from 'avi' to 'mp4'
import os
import subprocess

# Define the path to the folder containing the video files
path = 'D:'

# Define the path to the folder where the converted video files will be saved
path2 = '"D:\\Media Gallery"'

# Define a list of the video files in the folder
files = os.listdir(path)

# Define the file extension of the video files
extension_avi = '.avi'
extension_wmv = '.wmv'

# Define the file extension of the converted video files
extension_mp4 = '.mp4'

# Define the command to convert the video files
command = 'ffmpeg -i'

# Run the command for each video file in the folder
for file in files:
    if file.endswith(extension_avi) or file.endswith(extension_wmv):
        file_name = os.path.splitext(file)[0]
        file_path = path + '\\' + file
        file_path2 = path2 + '\\' + file_name + extension_mp4
        subprocess.call(command + ' ' + file_path + ' ' + file_path2)

# End of script
