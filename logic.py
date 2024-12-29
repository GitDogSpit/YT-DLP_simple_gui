# logic.py

#ONLY HERE FOR TESTING
import yt_dlp as yt
import json

class FormatInfo:
    '''Store all the information for each format that we read in...'''
    def __init__(self, format_id):
        self.format_id = format_id
        self.TypeOfMedia = None
        self.Extension = None
        self.Channels = None
        self.FileSize = None
        self.Protocol = None
        self.AudioSampleRate = None
        self.Resolution = None
        self.FPS = None

        self.VideoBitrate = None
        self.AudioBitrate = None
        self.AudioCodec = None
        self.VideoCodec = None
        #print(f"New Instance: {self.format_id}")

    def DisplayInformationFull(self):
        try:
            print(f'My ID is: {self.format_id}')
            print(f'My Resolution is: {self.Resolution}')
            print(f'My FPS is: {self.FPS}')
            print(f'My Audio Codec is: {self.AudioCodec}')
            print(f'My Video Codec is: {self.VideoCodec}')
            print(f'My Extension is: {self.Extension}')
            print(f'My Audio Sample Rate is: {self.AudioSampleRate}')
            print(f'My Audio Bitrate is: {self.AudioBitrate}')
            print(f'My Video Bitrate is: {self.VideoBitrate}')
        except Exception as e:
            print(f"Skip")

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

            for format in formats:
                output = [f"Format ID: {format['format_id']}"]

                #instantialize the format per format in the return
                item = FormatInfo(format_id=format['format_id'])

                #add attributes to the format only if they exist
                if 'resolution' in format and format['resolution']:
                    output.append(f"Resolution: {format['resolution']}")
                    item.Resolution = format['resolution'] #append to object
                    if format['resolution'] == 'audio only':
                        audios.append(item)
                        #print(f"{format['format_id']} is audio")

                if 'fps' in format and format['fps']:
                    output.append(f"FPS: {format['fps']}")
                    item.FPS = format['fps'] #append to object
                    if format['fps'] > 0 and format['fps'] < 1:
                        thumbnails.append(item)
                        #print(f"{format['format_id']} is a thumbnail")
                    elif format['fps'] > 1:
                        videos.append(item)
                        #print(f"{format['format_id']} is a video")
                    else:
                        pass
                        #actually redudant but leave as is.
                        #print('This is audio')

                #we no longer need to check whether something is audio, video, or a thumbnail
                if 'acodec' in format and format['acodec']:
                    output.append(f"Audio Codec: {format['acodec']}")
                    item.AudioCodec = format['acodec'] #append to object
                if 'vcodec' in format and format['vcodec']:
                    output.append(f"Video Codec: {format['vcodec']}")
                    item.VideoCodec = format['vcodec'] #append to object
                if 'ext' in format and format['ext']:
                    output.append(f"Extension: {format['ext']}")
                    item.Extension = format['ext'] #append to object
                if 'asr' in format and format['asr']:
                    output.append(f"Audio sampling rate: {format['asr']}")
                    item.AudioSampleRate = format['asr'] #append to object
                if 'abr' in format and format['abr']:
                    output.append(f"Audio Bitrate: {format['abr']}")
                    item.AudioBitrate = format['abr'] #append to object
                if 'vbr' in format and format['vbr']:
                    output.append(f"Video Bitrate: {format['vbr']}")
                    item.VideoBitrate = format['vbr'] #append to object
                #print(", ".join(output))

            ''' PRINTING OUT INFORMATION'''

            # print("Printing POST information")
            # print("Thumbnails:", [t.format_id for t in thumbnails])
            # print("Audios:", [a.format_id for a in audios])
            # print("Videos:", [v.format_id for v in videos])

            # print("Object Printing: Thumbnails")
            # for thumbnail in thumbnails:
            #     thumbnail.DisplayInformationFull()
            #     print('Next')

            # print("Object Printing: Audio")
            # for audio in audios:
            #     audio.DisplayInformationFull()
            #     print('Next')

            # print("Object Printing: Video")
            # for video in videos:
            #     video.DisplayInformationFull()
            #     print('Next')

            '''FIRST JOB IS TO GRAB RESOLUTIONS AND TELL ME THEIR ID's'''
            for video in videos:
                print(video.format_id, video.Resolution)

        except Exception as e:
            print(f"Error: {e}")



        '''TEST LATER --remux-video FORMAT'''