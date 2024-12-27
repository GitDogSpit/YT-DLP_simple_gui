# logic.py

#ONLY HERE FOR TESTING
import yt_dlp as yt
import json

class FormatInfo:
    '''We need to store all the information for each format that we read in...'''
    def __init__(self, format_id, resolution=None, fps=None, codec=None):
        self.format_id = format_id
        self.resolution = resolution
        self.fps = fps
        self.codec = codec

    def __repr__(self):
        return (f"FormatInfo(format_id='{self.format_id}', "
                f"resolution='{self.resolution}', fps={self.fps}, codec='{self.codec}')")


class AppLogic:
    def __init__(self):
        self.auto_convert = False
        self.audio = True
        self.video = True
        self.convert_dropdown_choice = "MP4"

    def toggle_auto_convert(self):
        #to reference this in commands do: command=self.logic_handler.toggle_auto_convert
        self.auto_convert = not self.auto_convert
        print(f"Auto Convert toggled: {self.auto_convert}")

    def toggle_audio(self):
        #to reference this in commands do: command=self.logic_handler.toggle_audio
        self.audio = not self.audio
        print(f"Audio toggled: {self.audio}")

    def toggle_video(self):
        #to reference this in commands do: command=self.logic_handler.toggle_video
        self.video = not self.video
        print(f"Video toggled: {self.video}")

    def url_entry_box_button(self):
        print("URL entered: sample")

    def download_button(self):
        print("Download button clicked")

    def convert_button(self):
        print("Convert button clicked")

    def videoFormat_dropdown_options(self):
        return ["MP4", "webm", "mkv", "mov"]
    
    def audioChoices_dropdown_options(self):
        return ["mp3_bad", "mp3_alright", "mp3_good", "mp3_best"] 
    
    def videoChoices_dropdown_options(self):
        return ["240p", "720p", "1080p", "1440p", "2560p"]
    
    if __name__ == '__main__':
        #dont forget to santizie just in case
        #yt.YoutubeDL.sanitize_info
        #https://github.com/yt-dlp/yt-dlp#usage-and-options

        ydl_opts = {
            'quiet': True,
            'listformats': False,
        }

        video_url = "https://youtu.be/qbIooWQfwU0?si=XKZlqxtFGwstnaxC"

        with yt.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats', [])

        try:

            #incoming, prepping for seperation
            thumbnails = []
            audios = []
            videos = []

            for f in formats:
                output = [f"Format ID: {f['format_id']}"]

                #add attributes only if they exist
                if 'resolution' in f and f['resolution']:
                    output.append(f"Resolution: {f['resolution']}")
                    if f['resolution'] == 'audio only':
                        audios.append(f['format_id'])
                        print(f'{f['format_id']} is audio')

                if 'fps' in f and f['fps']:
                    output.append(f"FPS: {f['fps']}")
                    if f['fps'] > 0 and f['fps'] < 1:
                        thumbnails.append(f['format_id'])
                        print(f"{f['format_id']} is a thumbnail")
                    elif f['fps'] > 1:
                        videos.append(f['format_id'])
                        print(f"{f['format_id']} is a video")
                    else:
                        #actually redudant but leave as is.
                        print('This is audio')

                # if 'acodec' in f and f['acodec']:
                #     output.append(f"Audio Codec: {f['acodec']}")
                # if 'vcodec' in f and f['vcodec']:
                #     output.append(f"Video Codec: {f['vcodec']}")
                # if 'ext' in f and f['ext']:
                #     output.append(f"Extension: {f['ext']}")
                # if 'asr' in f and f['asr']:
                #     output.append(f"Audio sampling rate: {f['asr']}")
                # if 'abr' in f and f['abr']:
                #     output.append(f"Audio Bitrate: {f['abr']}")
                # if 'vbr' in f and f['vbr']:
                #     output.append(f"Video Bitrate: {f['vbr']}")
                print(", ".join(output))

            print('Printing POST information')
            print("Thumbnails:", thumbnails)
            print("Audios:", audios)
            print("Videos:", videos)

        except Exception as e:
            print(f"Error: {e}")



        '''TEST LATER --remux-video FORMAT'''