from pytube import YouTube
import sys
import time
import requests


urls = [
	"https://www.youtube.com/watch?v=CCnKhFtuNj4"
]

	
def dl_complete(stream, file_path):
	print("\nDownload Complete\n") 

def progress(chunk, file_handle, bytes_remaining):
    global filesize
    global count 

    remaining = (100 * bytes_remaining) / filesize
    step = 100 - int(remaining)
    sys.stdout.write("\r"+str(step)+"% Downloading" + "." * count)
    sys.stdout.flush()
    count += 1
    if(count > 3): 
    	count = 1

def is_video_url_valid(url):
	return requests.get(url)



for url in urls:
	if not is_video_url_valid(url):
		print("Video unavailbale for download : "+ url)
		continue

	try:
		my_video = YouTube(url, on_progress_callback = progress, on_complete_callback = dl_complete)

	except VideoUnavailable:
		print(f'Video {url} is unavaialable, skipping.')
		continue
	else:
		if not "videoDetails" in my_video.vid_info:
				print(f'Video {url} is unavaialable, skipping.')
				continue

		file_name = my_video.title	

		stream = my_video.streams.get_highest_resolution()

		if stream is None:
			print("Video unavailbale for download : "+ file_name)
			continue

		filesize = stream.filesize
		count = 1
		print("\n"+stream.title+"\n")

		file = stream.download("dl_files")





