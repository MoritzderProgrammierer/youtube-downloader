from pytube import YouTube

url = "https://www.youtube.com/watch?v=uQRIvXymJZI"
yt = YouTube(url)

#Title of video
print(f"Title: {yt.title}")
#Number of views of video
print(f"Number of views: {yt.views}")
#Length of the video
print(f"Length of video: {yt.length} seconds")
#Description of video
print(f"Description: {yt.description}")
#Rating
print(f"Ratings: {yt.rating}")