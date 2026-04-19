import yt_dlp

def download_youtube_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example Usage
if __name__=="__main__":
    print("Enter your URL here:")    
    video_url = input()
    download_youtube_audio(video_url)
    print("URL downloaded.")