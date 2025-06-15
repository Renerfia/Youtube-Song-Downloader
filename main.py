from pytubefix import YouTube
from tqdm import tqdm
import os

os.makedirs("./downloads", exist_ok=True)
print(f"Enter the all the music links here in the below continuously\nEnter the youtube link here: (Type 's' to start downloading!)")
is_running = True
contents = [] #all your content list are saved in this list

while is_running == True:

    user_input = input(">>")
    
    if user_input.lower() == "s":
        is_running = False
    else:
        contents.append(user_input)

    
try:
    for content in tqdm(contents,desc=f"Downloading",unit="song"):
        yt = YouTube(content)

        print(f"\nDownloading: {yt.title}")
        stream = yt.streams.filter(only_audio=True,file_extension="mp4").first() #you can change video filter here(for video use only_Video = True)
        stream.download(output_path="./downloads") #you can change file path here
        print(f"{yt.title} complete!")

except Exception as e:
    print(f"There is an error:{e}")
    