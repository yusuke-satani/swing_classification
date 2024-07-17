from pytube import YouTube 

# where to save 
SAVE_PATH = "videos" #to_do 

# link of the video to be downloaded 
link = "https://youtu.be/0PJx1QL-0KM?si=I5BeLwbHp8BVc_Ct"

try: 
    # object creation using YouTube 
    yt = YouTube(link) 
except: 
    #to handle exception 
    print("Connection Error") 

# Get all streams and filter for mp4 files
mp4_streams = yt.streams.filter(file_extension='mp4').all()

# get the video with the highest resolution
d_video = mp4_streams[-1]

try: 
    # downloading the video 
    d_video.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except: 
    print("Some Error!")



