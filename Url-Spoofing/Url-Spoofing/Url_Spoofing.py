import gdshortener
import os
import tkinter
import sys

class url_spoofing:
    def __init__(self):
        self.request_gdshortener = gdshortener.ISGDShortener()

    def get_path(self, filename):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, filename) 
        else:
            return filename

    def window(self):
        def take_url():
            try:
                url = tkinter.Entry.get(original_url)
                second_custom = tkinter.Entry.get(second)
                custom = 'https://' + tkinter.Entry.get(custom_part) + '@'
                shortened_url = self.request_gdshortener.shorten(url, custom_url = second_custom)
                shorten_url = shortened_url[0]
                final_url = shorten_url.replace('https://', custom)
                new_url.insert(0, final_url)
                error.place(x = 5, y = 50)
                loaded.place(x = 130, y = 235)
            except:
                loaded.place(x = 5, y = 50)
                error.place(x = 130, y = 235)

        def reset():
            second.delete(0, 1000)
            original_url.delete(0, 1000)
            custom_part.delete(0, 1000)
            new_url.delete(0, 1000)

        root = tkinter.Tk()
        root.title('Url-Spoofing - by Bl4ckV v1.1.0')
        root.iconbitmap(self.get_path('eye.ico'))
        root.geometry('340x340')
        root.configure(bg='#0E0E0E')
        root.resizable(False, False)

        loaded = tkinter.Label(root, text = 'Loaded url!', bg = '#0E0E0E', fg = 'green', font = ('Arial', 10, 'bold'))
        error = tkinter.Label(root, text = 'Enter a valid url!', bg = '#0E0E0E', fg = 'red', font = ('Arial', 10, 'bold'))
        text1 = tkinter.Label(root, text = 'Url:', font = ('Arial', 10, 'bold'), fg = 'white', bg = '#0E0E0E')
        text1.place(x = 28, y = 120)
        text2 = tkinter.Label(root, text = 'Custom part:', font = ('Arial', 10, 'bold'), fg = 'white', bg = '#0E0E0E')
        text2.place(x = 28, y = 170)
        text3 = tkinter.Label(root, text = 'New url:', font = ('Arial', 10, 'bold'), fg = 'white', bg = '#0E0E0E')
        text3.place(x = 28, y = 270)

        title = tkinter.Label(root, text = 'URL', bg = '#0E0E0E', font = ('Arial', 30, 'bold'), fg = 'white')
        title.place(x = 200, y = 30)
        title2 = tkinter.Label(root, text = 'Spoofing', bg = '#0E0E0E', font = ('Arial', 20, 'bold'), fg = 'white')
        title2.place(x = 200, y = 80)
        eye = tkinter.PhotoImage(file = self.get_path('eye.jpg'))
        eye_pack = tkinter.Label(root, image = eye, borderwidth = 0)
        eye_pack.place(x = 5, y = 18)
        second_text = tkinter.Label(root, text = 'Second custom:', font = ('Arial', 10, 'bold'), fg = 'white', bg = '#0E0E0E').place(x = 180, y = 170)
        second = tkinter.Entry(root, font = ('Arial', 10, 'bold'), width = 18)
        second.place(x = 183, y = 190)
        original_url = tkinter.Entry(root, bg = 'white', font = ('Arial', 10, 'bold'), width = 40)
        original_url.place(x = 30, y = 140)
        custom_part = tkinter.Entry(root, bg = 'white', font = ('Arial', 10, 'bold'), width = 18)
        custom_part.place(x = 30, y = 190)
        buttom = tkinter.Button(root, text = 'Load', width = 10, font = ('Arial', 10, 'bold'), command = take_url)
        buttom.place(x = 30, y = 230)
        new_url = tkinter.Entry(root, bg = 'white', font = ('Arial', 10, 'bold'), width = 40, fg = 'green')
        new_url.place(x = 30, y = 290)
        reset_button = tkinter.Button(root, text = 'Reset', command = reset).place(x = 273, y = 230)
        root.mainloop()

    def start(self):
        self.window()

url_spoofing = url_spoofing()
url_spoofing.start()
