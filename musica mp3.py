import yt_dlp

playlist_url = 'https://www.youtube.com/watch?v=e_oFiNyOgiw&list=PLvC0GZWIwKUfGWspoJ1rkyBN8xjrobTwI'

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(playlist_title)s/%(playlist_index)03d - %(title)s.%(ext)s',

    'postprocessors': [
        {   # Estrai audio in MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',    # 128/192/256/320
        },
        {   # Scrivi metadati ID3
            'key': 'FFmpegMetadata',
        },
    ],

    # Niente thumbnail
    'writethumbnail': False,

    # Assicurati di usare ffmpeg e di rimuovere i file sorgente
    'prefer_ffmpeg': True,
    'keepvideo': False,

    'quiet': False,
    'noprogress': False,
    'ignoreerrors': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
