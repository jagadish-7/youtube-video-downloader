from pytube import YouTube


print("\nYouTube Video Downloader, created by Tech Jagadish!")
print("------------------------")


while 1:
    # Taking the URL from the user as input
    youtube_url = input("Enter the URL(q to quit): ")
    print()

    # If the user presses q, then the program end.
    if(youtube_url == 'q' or youtube_url == 'Q'):
        print("Quitting...")
        print("Thank you, visit again!")
        break
    else:
        # Creating a YouTube object using the given URL
        yt = YouTube(youtube_url)

        # Taking care of the quality
        quality = yt.streams.get_highest_resolution()

        # This is the path where our video will be saved, after downloading
        video_path = "Your_Download/"
        print("Downloading the video...!")
        # Doanloading the video in the given path
        quality.download(video_path)

        # Showing a conformation message to the user, when the downloading is completed.
        print("Download completed...")
        print("Thank you, visit again to our website tech Jagadish!")
        continue
