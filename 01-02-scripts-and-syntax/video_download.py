from pytube import YouTube
# import pytube #using everything

def download_video(frog, newt): #arbitrary placeholders
    # create YouTube object from the pytube lib
    yt = YouTube(frog)
    # get highest res stream
    video_stream = yt.streams.get_highest_resolution()
    # download video
    video_stream.download(output_path= newt)

video_link = "https://youtu.be/kCBV18bdi3Y?si=XgDD8Lb12bzPl-9a" #SPRINGSTEEN: LAND OF HOPE AND DREAMS
save_path = "Videos"

download_video(video_link, save_path)