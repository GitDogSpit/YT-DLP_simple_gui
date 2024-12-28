import tkinter as tk
from tkinter import ttk

from pathlib import Path

from logic import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AppGUI:
    def __init__(self, root, logic_handler):
        self.root = root
        self.logic_handler = logic_handler
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("1280x720")
        self.root.configure(bg="#181818")
        self.root.resizable(False, False)

        canvas = tk.Canvas(self.root, bg="#181818", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        #The auto-convert toggle button
        button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
        auto_conv_button = tk.Button( image=button_image_1, borderwidth=0, highlightthickness=0, command=self.logic_handler.toggle_auto_convert, relief="flat",)
        auto_conv_button.image = button_image_1  # Prevent garbage collection
        auto_conv_button.place(x=1021.0, y=377.0, width=40.0, height=24.0)
        #The auto_convert text
        canvas.create_text(829.0, 377.0, anchor="nw", text="Automatically Convert", fill="#FFFFFF", font=("Inter", 16 * -1),)


        #CONVERT DROPDOWN THAT NEEDS TO BE FORMATTED
        image_image_10 = tk.PhotoImage(file=relative_to_assets("image_6.png"))
        image_10 = canvas.create_image(995.0, 440.0, image=image_image_10)
        convertVideo_dropdown = ttk.Combobox(self.root, width = 27,  textvariable = tk.StringVar()) 
        convertVideo_dropdown['values'] = self.logic_handler.videoFormat_dropdown_options()
        convertVideo_dropdown.place(x=820, y=460)


        #The download "down arrow" image
        image_image_2 = tk.PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(1229.0, 671.0, image=image_image_2)


        #The thumbnail image
        image_image_3 = tk.PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(1041.0, 148.0, image=image_image_3)
        #The thumbnail video title
        canvas.create_text(875.0, 277.0, anchor="nw", text="RAT ESPIONAGE ACTION GAME", fill="#FFFFFF", font=("Inter", 16 * -1),)
        #The thumbnail video channel
        canvas.create_text(875.0, 308.0, anchor="nw", text="DogSpit!", fill="#FFFFFF", font=("Inter", 16 * -1))
        #The weird little bars under the channel thumbnail
        image_image_4 = tk.PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(844.0, 301.0, image=image_image_4)


        #The audio text header
        canvas.create_text(33.0, 81.0, anchor="nw", text="AUDIO", fill="#FFFFFF", font=("Inter", 16 * -1))
        #Audio toggle button
        button_image_2 = tk.PhotoImage(file=relative_to_assets("button_2.png"))
        audio_button = tk.Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=self.logic_handler.toggle_audio, relief="flat",)
        audio_button.place(x=333.0, y=80.0, width=40.0, height=24.0)

        #AUDIO CHOICE DROPDOWN NEEDS TO BE CONVERTED
        image_image_5 = tk.PhotoImage(file=relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(203.0, 159.0, image=image_image_5)
        audioChoices_dropdown = ttk.Combobox(self.root, width = 27,  textvariable = tk.StringVar()) 
        audioChoices_dropdown['values'] = self.logic_handler.audioChoices_dropdown_options()
        audioChoices_dropdown.place(x=203, y=159)

        #Audio Left Column
        canvas.create_text(33.0, 202.0, anchor="nw", text="Extension", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(33.0, 236.0, anchor="nw", text="Channels", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(33.0, 270.0, anchor="nw", text="FileSize", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(33.0, 304.0, anchor="nw", text="BitRate", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(33.0, 338.0, anchor="nw", text="Proto", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(33.0, 372.0, anchor="nw", text="Codec", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(33.0, 406.0, anchor="nw", text="ASR", fill="#FFFFFF", font=("Inter", 16 * -1),)

        #Audio Right Column
        canvas.create_text(148.0, 202.0, anchor="nw", text="MP4", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(148.0, 236.0, anchor="nw", text="2", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(148.0, 270.0, anchor="nw", text="5.96MiB", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(148.0, 304.0, anchor="nw", text="49k", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(148.0, 338.0, anchor="nw", text="https", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(148.0, 372.0, anchor="nw", text="opus", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(148.0, 406.0, anchor="nw", text="48k", fill="#FFFFFF", font=("Inter", 16 * -1),)


        #Video Header
        canvas.create_text(437.0, 81.0, anchor="nw", text="VIDEO", fill="#FFFFFF", font=("Inter", 16 * -1))
        #Video toggle button
        button_image_3 = tk.PhotoImage(file=relative_to_assets("button_3.png"))
        video_button = tk.Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=self.logic_handler.toggle_video,relief="flat",)
        video_button.place(x=737.0, y=80.0, width=40.0, height=24.0)

        #VIDEO CHOICE DROPDOWN NEEDS TO BE CONVERTED
        image_image_6 = tk.PhotoImage(file=relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(607.0, 161.0, image=image_image_6)
        videoChoices_dropdown = ttk.Combobox(self.root, width = 27,  textvariable = tk.StringVar()) 
        videoChoices_dropdown['values'] = self.logic_handler.videoChoices_dropdown_options()
        videoChoices_dropdown.place(x=607, y=161)

        #Video Left Column
        canvas.create_text(437.0, 202.0, anchor="nw", text="Extension", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(437.0, 236.0, anchor="nw", text="Resolution", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(437.0, 270.0, anchor="nw", text="FileSize", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(437.0, 304.0, anchor="nw", text="BitRate", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(437.0, 338.0, anchor="nw", text="FPS", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(437.0, 372.0, anchor="nw", text="Codec", fill="#FFFFFF", font=("Inter", 16 * -1),)

        #Video Right Column
        canvas.create_text(559.0, 202.0, anchor="nw", text="webm", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(559.0, 236.0, anchor="nw", text="1920x1080", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(559.0, 270.0, anchor="nw", text="49.71MiB", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(559.0, 304.0, anchor="nw", text="2920k", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(559.0, 338.0, anchor="nw", text="30", fill="#FFFFFF", font=("Inter", 16 * -1),)
        canvas.create_text(559.0, 372.0, anchor="nw", text="avc1.640028", fill="#FFFFFF", font=("Inter", 16 * -1),)


        #The enter URL text box
        button_image_4 = tk.PhotoImage(file=relative_to_assets("button_4.png"))
        URL_enter = tk.Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=self.logic_handler.url_entry_box_button, relief="flat",)
        URL_enter.place(x=503.0, y=7.0, width=64.0, height=40.0)


        #Video URL entry box
        entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(349.0, 27.0, image=entry_image_1)
        entry_1 = tk.Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        entry_1.place(x=203.0, y=7.0, width=292.0, height=38.0)


        #File image
        image_image_7 = tk.PhotoImage(file=relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(599.0, 28.0, image=image_image_7)


        #The download button
        button_image_5 = tk.PhotoImage(file=relative_to_assets("button_5.png"))
        button_5 = tk.Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=self.logic_handler.download_button, relief="flat",)
        button_5.place(x=17.0, y=11.0, width=83.0, height=32.0)


        #The convert button
        button_image_6 = tk.PhotoImage(file=relative_to_assets("button_6.png"))
        button_6 = tk.Button(image=button_image_6, borderwidth=0, highlightthickness=0, command=self.logic_handler.convert_button, relief="flat",)
        button_6.place(x=112.0, y=11.0, width=83.0, height=32.0)


        #top line i think
        image_image_9 = tk.PhotoImage(file=relative_to_assets("image_9.png"))
        image_9 = canvas.create_image(414.0, 446.0, image=image_image_9)
        self.root.resizable(False, False)


        #Bottom line i think
        image_image_8 = tk.PhotoImage(file=relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(423.0, 61.0, image=image_image_8)

        self.root.mainloop()