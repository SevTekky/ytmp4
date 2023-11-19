from pytube import YouTube
import os
import sys

def show_progress_bar(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    sys.stdout.write("\rDownloading: %d%%" % percentage_of_completion)
    sys.stdout.flush()

def download(link, path):
    try:
        youtube_object = YouTube(link)
        youtube_object.register_on_progress_callback(show_progress_bar)
        video_stream = youtube_object.streams.get_highest_resolution()
        video_stream.download(output_path=path)
        print("\nDownload completed successfully!")
    except Exception as e:
        print(f"An error has occurred: {e}")

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

link = input("Enter the YouTube video URL: ")
download_path = get_download_path()
download(link, download_path)





#You use the from pytube import YouTube function to import the Python Pytube library before continuing with the other aspects. Then you define the function download link.
#
#The youtubeObject = youtubeObject.streams.get_highest_resolution() command will automatically download the highest resolution available.
#Then I implemented the Try and Except to return an error message if the download fails – else it will print out that the download is completed successfully.
#
#The Link function will ask for the preferred YouTube video link to download, then immediately after you hit the enter button, the video downloading will commence.

#Progress Bar: pytube allows you to hook into the download process with a callback function. You can use this to update a progress bar.

#Download Directory: You can specify the download directory in the download() method.

#The show_progress_bar function is a callback that updates the progress of the download. It calculates the percentage of the download and prints it.
#The download function now takes an additional parameter path which is the directory where the video will be downloaded.
#The YouTube object is created with an on_progress_callback set to show_progress_bar.
#The download method of the video stream is called with output_path set to the desired download directory.
#Make sure your terminal supports carriage return (\r) for overwriting the progress line.
#If you run into any issues with the progress display, you might need to adjust the output method depending on your terminal or console.
#Use `os.path` and `os.environ`: These modules can help you construct the path to the user's Downloads folder in a platform-independent way.
#Platform Detection: You can detect the operating system and construct the path accordingly.
#The get_download_path function determines the path to the Downloads folder. It handles both Windows and Unix-like systems (like Linux and macOS).
#For Windows, it uses the winreg module to get the path from the Windows registry.
#For Unix-like systems, it assumes a default downloads folder in the user's home directory. Note that the folder name is case-sensitive and may vary (e.g., 'Downloads' vs 'downloads').
#This script should now work on different machines, automatically saving the downloaded files to the user's Downloads folder.