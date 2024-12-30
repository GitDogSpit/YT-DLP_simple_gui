# logic.py

#ONLY HERE FOR TESTING
import yt_dlp as yt
import json

class VideoInfo:
    '''Store all information of formats for A GIVEN VIDEO'''
    def __init__(self):
        #seperation of formats
        self.thumbnails = []
        self.audios = []
        self.videos = []

    def TotalFormats(self):
        return (len(self.thumbnails) + len(self.audios) + len(self.videos))
    
    def ListVideos(self):
        for video in self.videos:
            print(video.format_id, video.Resolution)

    def ListAudios(self):
        for audio in self.audios:
            print(audio.format_id, audio.AudioBitrate)

    def ListThumbnails(self):
        for thumbnail in self.thumbnails:
            print(thumbnail.format_id, thumbnail.Resolution)

    def ListBestVideos(self):
        #first we grab the resolution from a given format
        #if the resolution is the same but the format is different, compare the bitrate
        #remember the best format_id for each resolution

        bestList = [] #should be: 269, 230, 311, 312
        currentBestPerRes = self.videos[0].format_id #assumes there is a list
        currentBestVBR = float(self.videos[0].VideoBitrate) #assumes there is a list
        tempResolution = self.videos[0].Resolution #assumes there is a list

        for video in self.videos:
            if video.Resolution != tempResolution:
                bestList.append(currentBestPerRes)  #add the best that we found to the list of best
                currentBestVBR = 0.0
                currentBestPerRes = video.format_id #reset to current video
                tempResolution = video.Resolution #reset to the new resolution

            if tempResolution == video.Resolution:
                if video.VideoBitrate > currentBestVBR:
                    currentBestPerRes = video.format_id
                    currentBestVBR = video.VideoBitrate
        bestList.append(currentBestPerRes)
        return bestList
    
    def GiveIndex(self, ID):
        for index, video in enumerate(self.videos):
            if video.format_id == ID:
                return index
        for index, audio in enumerate(self.audios):
            if audio.format_id == ID:
                return index
        for index, thumbnail in enumerate(self.thumbnails):
            if thumbnail.format_id == ID:
                return index
        return None  

class FormatInfo:
    '''Store all the information for EACH FORMAT that we read in...'''
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
        '''Display all the information that a format has'''
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
    '''The information for a given session'''
    def __init__(self):
        self.url_entry = None
        self.auto_convert = False
        self.audio = True
        self.video = True
        self.convert_dropdown_choice = "MP4"

        #startup
        print("Starting new App instance")
        self.VideoTemp = VideoInfo()

    def url_entry_box_button(self):
        if self.url_entry:
            entered_url = self.url_entry.get()  #get value via GET
            self.url_entry = entered_url #to make sure that we saved it
            print(f"THIS IS MY URL ENTRY SAVED: {self.url_entry}")
            print(f"Looking up stats for: {entered_url}")
            self.YouTubeBasicLookup()
            print("Lookup successful")
            print("Move choices to our dropdown")
            self.videoChoices_dropdown_options()
        else:
            print("Error: URL entry box not set.")

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

    def download_button(self):
        print("Download button clicked")

    def convert_button(self):
        print("Convert button clicked")

    def videoFormat_dropdown_options(self):
        return ["MP4", "webm", "mkv", "mov"]
    
    def audioChoices_dropdown_options(self):
        return ["mp3_bad", "mp3_alright", "mp3_good", "mp3_best"] 
    
    def videoChoices_dropdown_options(self):
        if self.VideoTemp.videos == None or len(self.VideoTemp.videos) == 0:
            return "None"
        else:
            print("This is what I have in my videos")
            self.VideoTemp.ListVideos()
            print("Dropdown - Videos")
            print(f'This: {self.VideoTemp.videos}')
            '''WHY WONT IT DISPLAY THE NEW LIST OF VIDEOS TO THE DROP DOWN?'''
            return self.VideoTemp.videos
        
    def YouTubeBasicLookup(self):
        '''The main-stay operation'''

        #CLI commands
        ydl_opts = {
            'quiet': True,
            'listformats': False,
        }

        #URL entry
        if self.url_entry == None:
            video_url = "https://youtu.be/qbIooWQfwU0?si=XKZlqxtFGwstnaxC"
        else:
            video_url = self.url_entry

        #go and grab the logic
        with yt.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats', [])

        try:
            for format in formats:
                '''Go through each format received one by one'''

                output = [f"Format ID: {format['format_id']}"] #cosmetic output
                item = FormatInfo(format_id=format['format_id']) #instantialize per format as "item"

                '''Add attributes to the format only if they exist
                    with the exception of resolution and fps being used
                    for "type of media" seperation '''
                
                if 'resolution' in format and format['resolution']:
                    output.append(f"Resolution: {format['resolution']}")
                    item.Resolution = format['resolution'] #append
                    if format['resolution'] == 'audio only':
                        self.VideoTemp.audios.append(item)
                        #print(f"{format['format_id']} is audio")

                if 'fps' in format and format['fps']:
                    output.append(f"FPS: {format['fps']}")
                    item.FPS = format['fps'] #append
                    if format['fps'] > 0 and format['fps'] < 1:
                        self.VideoTemp.thumbnails.append(item)
                        #print(f"{format['format_id']} is a thumbnail")
                    elif format['fps'] > 1:
                        self.VideoTemp.videos.append(item)
                        #print(f"{format['format_id']} is a video")
                    else:
                        pass
                        #actually redudant but leave as is.
                        #print('This is audio')

                #we no longer need to check whether something is audio, video, or a thumbnail
                if 'acodec' in format and format['acodec']:
                    output.append(f"Audio Codec: {format['acodec']}")
                    item.AudioCodec = format['acodec'] #append
                if 'vcodec' in format and format['vcodec']:
                    output.append(f"Video Codec: {format['vcodec']}")
                    item.VideoCodec = format['vcodec'] #append
                if 'ext' in format and format['ext']:
                    output.append(f"Extension: {format['ext']}")
                    item.Extension = format['ext'] #append
                if 'asr' in format and format['asr']:
                    output.append(f"Audio sampling rate: {format['asr']}")
                    item.AudioSampleRate = format['asr'] #append
                if 'abr' in format and format['abr']:
                    output.append(f"Audio Bitrate: {format['abr']}")
                    item.AudioBitrate = format['abr'] #append
                if 'vbr' in format and format['vbr']:
                    output.append(f"Video Bitrate: {format['vbr']}")
                    item.VideoBitrate = format['vbr'] #append
                print(", ".join(output))

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

            '''Test: Does the VideoInfo class successfuly store info? Prove by saying how many'''
            #print(VideoTemp.TotalFormats())

            '''Task 1: (Videos) Tell me their ID's and Resolution'''
            #VideoTemp.ListVideos()

            '''Task 2: (Audios) Tell me their ID's and Bitrate'''
            #VideoTemp.ListAudios()

            '''Task 3: (Thumbnail) Tell me their ID's and Resolution'''
            #VideoTemp.ListThumbnails()

            '''Task 4: List the only the best videos per resolution, based off bitrate'''
            #print(VideoTemp.ListBestVideos())

            '''Task 5: Look up method'''
            # print(VideoTemp.GiveIndex('311'))
            # print(VideoTemp.videos[5].format_id)

            '''Task 6: Apply the information to our GUI endpoint'''
        except Exception as e:
            print(f"Error: {e}")

    if __name__ == '__main__':
        #dont forget to santizie just in case
        #yt.YoutubeDL.sanitize_info
        #https://github.com/yt-dlp/yt-dlp#usage-and-options

        '''TEST LATER --remux-video FORMAT'''