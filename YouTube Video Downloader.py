from tkinter import *
import tkinter as tk
import yt_dlp


class downloader():
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("944x500+500+200")

        MainFrame = Frame(self.root, bg="white", bd=10, width=810, height=490, relief=RIDGE)
        MainFrame.grid(row=0, column=0, pady=40)

        TitleFrame = Frame(MainFrame)
        TitleFrame.grid(row=0, column=0, padx=40)

        WidgetFrame = Frame(MainFrame, bd=0, width=810, height=490, relief=RIDGE)
        WidgetFrame.grid(row=2, column=0, padx=20, pady=40)

        # Title
        self.lblDownloadTitle = Label(
            TitleFrame,
            font=('arial', 20, 'bold'),
            text="YouTube Downloader",
            bd=7,
            anchor='w'
        )
        self.lblDownloadTitle.grid(row=0, column=0, sticky='w', padx=10)

        # -----------------------------------------

        def download_video():
            link = url_entry.get()

            try:
                Feedback_label.config(text="Downloading...")

                ydl_opts = {
                    'outtmpl': '%(title)s.%(ext)s'
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])

                Feedback_label.config(text="Download Complete!")

            except Exception as e:
                Feedback_label.config(text="Error downloading!")

        # -----------------------------------------

        label_url = Label(
            WidgetFrame,
            text="\tEnter in this box the full URL of your Video :",
            font=('arial', 24),
            justify='center',
            pady=24
        )
        label_url.grid(row=0, column=0)

        # URL Entry
        url_entry = Entry(
            WidgetFrame,
            width=48,
            font=('Arial', 22),
            fg='blue',
            justify='center'
        )
        url_entry.grid(row=1, column=0)
        url_entry.focus()

        # Download Button
        download_button = Button(
            WidgetFrame,
            text="Download",
            font=('Arial', 16),
            command=download_video
        )
        download_button.grid(row=1, column=1)

        # Feedback Label
        Feedback_label = Label(
            self.root,
            text="Feedback widget",
            font=('Arial', 24),
            fg='blue'
        )
        Feedback_label.grid(row=2, column=0, pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    application = downloader(root)
    root.mainloop()