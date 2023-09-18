import customtkinter
from tkinter import *
import os
import cv2
from PIL import Image, ImageTk

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):

    APP_NAME = "CustomTkinter"
    WIDTH = 800
    HEIGHT = 500

    def __init__(self, video_source=1, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        # capture the video capturing class
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)

        # ============ create two CTkFrames ============
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, pady=5, padx=2, sticky="nw")

        # ============ frame_left ============
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "user1.jpg")),
                                                 dark_image=Image.open(os.path.join(image_path, "user1.jpg")), size=(125, 150))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "user2.jpg")),
                                                 dark_image=Image.open(os.path.join(image_path, "user2.jpg")), size=(125, 150))

        # Images labels created here
        self.profile_card = customtkinter.CTkButton(self.frame_left, corner_radius=0, height=100, text="", fg_color=("gray70", "gray30"),
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    anchor="w",
                                                    command=print("hello"))
        self.profile_card.columnconfigure(0, weight=0)
        self.profile_card.columnconfigure(1, weight=0)
        self.profile_card.rowconfigure(0, weight=0)

        # image side of the card
        self.image_side = customtkinter.CTkLabel(self.profile_card, corner_radius=0, text="", fg_color="transparent", image=self.home_image, anchor="w")
        self.image_side.grid(row=0, column=0)
        # information side of the card
        self.profile_info = customtkinter.CTkLabel(self.profile_card, corner_radius=0, fg_color="transparent", text="")
        self.profile_info.rowconfigure(0, weight=0)
        self.profile_info.rowconfigure(1, weight=0)
        self.profile_info.rowconfigure(2, weight=0)
        self.profile_info.rowconfigure(3, weight=0)
        self.profile_info.rowconfigure(4, weight=0)
        self.profile_info.columnconfigure(0, weight=0)

        self.match_info = customtkinter.CTkLabel(self.profile_info, text="MATCH: 98%", text_color="orange")
        self.match_info.grid(row=0, column=0, sticky="w")

        self.name_info = customtkinter.CTkLabel(self.profile_info, text="NAME: WASSWA SPEED")
        self.name_info.grid(row=1, column=0, sticky="w")

        self.name_info = customtkinter.CTkLabel(self.profile_info, text="GENDER: MALE")
        self.name_info.grid(row=2, column=0, sticky="w")

        self.id_info = customtkinter.CTkLabel(self.profile_info, text="NIN: CMZER4345333RF")
        self.id_info.grid(row=3, column=0, sticky="w")

        self.location_info = customtkinter.CTkLabel(self.profile_info, text="LOCATION: Astro Street, Macwan-4th street")
        self.location_info.grid(row=4, column=0, sticky="w")

        self.profile_info.grid(row=0, column=1, sticky="n", padx=20)
        self.profile_card.pack(fill="x", pady=5, padx=5)

        # user2
        self.profile_card = customtkinter.CTkButton(self.frame_left, corner_radius=0, height=100, text="", fg_color=("gray70", "gray30"),
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    anchor="w",
                                                    command=print("hello"))
        self.profile_card.columnconfigure(0, weight=0)
        self.profile_card.columnconfigure(1, weight=0)
        self.profile_card.rowconfigure(0, weight=0)

        # image side of the card
        self.image_side = customtkinter.CTkLabel(self.profile_card, corner_radius=0, text="", fg_color="transparent", image=self.chat_image, anchor="w")
        self.image_side.grid(row=0, column=0)
        # information side of the card
        self.profile_info = customtkinter.CTkLabel(self.profile_card, corner_radius=0, fg_color="transparent", text="")
        self.profile_info.rowconfigure(0, weight=0)
        self.profile_info.rowconfigure(1, weight=0)
        self.profile_info.rowconfigure(2, weight=0)
        self.profile_info.rowconfigure(3, weight=0)
        self.profile_info.rowconfigure(4, weight=0)
        self.profile_info.columnconfigure(0, weight=0)

        self.match_info = customtkinter.CTkLabel(self.profile_info, text="MATCH: 98%")
        self.match_info.grid(row=0, column=0, sticky="w")

        self.name_info = customtkinter.CTkLabel(self.profile_info, text="NAME: WASSWA SPEED")
        self.name_info.grid(row=1, column=0, sticky="w")

        self.name_info = customtkinter.CTkLabel(self.profile_info, text="GENDER: MALE")
        self.name_info.grid(row=2, column=0, sticky="w")

        self.id_info = customtkinter.CTkLabel(self.profile_info, text="NIN: CMZER4345333RF")
        self.id_info.grid(row=3, column=0, sticky="w")

        self.location_info = customtkinter.CTkLabel(self.profile_info, text="LOCATION: Astro Street, Macwan-4th street")
        self.location_info.grid(row=4, column=0, sticky="w")

        self.profile_info.grid(row=0, column=1, sticky="n", padx=20)
        self.profile_card.pack(fill="x", pady=5, padx=5)

        # ============ frame_right ============
        self.camera_frame = Canvas(self.frame_right, width=640, height=480)
        self.camera_frame.pack(pady=10, padx=10)

        self.buttonup = customtkinter.CTkButton(self.camera_frame, text="+", corner_radius=0, width=50, fg_color=("gray70", "gray30"))
        self.buttonup.place(x=10, y=10)

        self.buttondown = customtkinter.CTkButton(self.camera_frame, text="-", corner_radius=0, width=50, fg_color=("gray70", "gray30"))
        self.buttondown.place(x=10, y=50)

        self.update_frame()
        self.mainloop()

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

    def update_frame(self):
        # get a frame from the video source
        is_true, frame = self.vid.get_frame()
        if is_true:
            # Detect faces in the grayscale frame
            faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.camera_frame.create_image(0, 0, image=self.photo, anchor=NW)
        self.after(15, self.update_frame)

class MyVideoCapture:
    def __init__(self, video_source=2):
        self.vid = cv2.VideoCapture(video_source)
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        # Set the desired width and height for the resized frames
        if not self.vid.isOpened():
            raise ValueError("Unable to open camera \n select another video source", video_source)

    def get_frame(self):
        if self.vid.isOpened():
            is_true, frame = self.vid.read()
            if is_true:
                # if isTrue is true then current frame is converted to RGB and processed
                # Convert the frame to grayscale for face detection
                return is_true, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return is_true, None
        else:
            return None

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


if __name__ == "__main__":
    app = App()
