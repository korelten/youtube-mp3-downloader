import yt_dlp
import os
import sys

def download_audio(url):
    output_folder = "music"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"📁 Created folder: {output_folder}")

    # Check for FFmpeg
    if not os.path.exists("ffmpeg.exe"):
        print("\n" + "="*50)
        print("❌ ERROR: ffmpeg.exe NOT FOUND!")
        print("="*50)
        print("1. Download FFmpeg (full_build).")
        print("2. Go to the 'bin' folder inside the archive.")
        print("3. Copy 'ffmpeg.exe' to THIS folder (next to the script).")
        print("="*50)
        input("\nPress Enter to exit...")
        sys.exit()

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(playlist_index)s - %(title)s.%(ext)s',
        'ffmpeg_location': 'ffmpeg.exe',
        
        # Bypass restrictions by pretending to be Android
        'extractor_args': {'youtube': {'player_client': ['android']}},
        
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
    }

    print(f"\n🚀 Starting download...\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n" + "="*50)
        print("✅ DONE! Files are in the 'music' folder")
        print("="*50)
    except Exception as e:
        print("\n❌ An error occurred:")
        print(e)
        print("\nTry updating the library: pip install --upgrade yt-dlp")

if __name__ == '__main__':
    print("--- YouTube Music Downloader (Universal) ---")
    link = input("Paste the URL (video or playlist): ")
    
    if link:
        download_audio(link)
    else:
        print("No URL provided.")
    
    input("\nPress Enter to exit...")