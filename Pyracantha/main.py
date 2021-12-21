'''
Little monologue about Pyracantha jam
'''
import tkinter
import time

words = ["That's Pyracantha, fire thorn.",
"Don't eat the seeds, they contain cyanide.", 
"The flesh doesn't taste too good, either.", 
"I heard they taste real good as jam.", 
"...but of course it would taste good, jam is just fruit with an obscene amount of sugar.", 
"Why spend all that time straining seeds from a tiny berry when you can use domesticated fruit..."]
images = [r'Pyracantha/m.png', r'Pyracantha/m.png', r'Pyracantha/mConfused.png', r'Pyracantha/mHappy.png',
r'Pyracantha/m.png', r'Pyracantha/mConfused.png']

master = tkinter.Tk(className="Pyracantha Jam")
master.geometry("800x400")
master.columnconfigure(1, weight = 60)

#master.columnconfigure(0, weight = 1)

i = 0
def next_msg():
    global i
    global speech
#    global img_label

    if i < len(words):
        speech.config(text = words[i])

#        img = tkinter.PhotoImage(master = master, file = images[i])
#        img_label = tkinter.Label(master, image = img)
#        img_label.grid(column = 2, row = 0, sticky=tkinter.W, padx=5, pady=5)
#        img_label.image = img
        if i == 2 or i == 5:
                img_label.image = tkinter.PhotoImage(master = master, file = r'Pyracantha/mConfused.png')
        elif i == 3:
                img_label.image = tkinter.PhotoImage(master = master, file = r'Pyracantha/mHappy.png')
        else:
                img_label.image = tkinter.PhotoImage(master = master, file = r'Pyracantha/m.png')
        print(str(images[i]))
        i += 1
        print(i)

speech = tkinter.Label(master, text = "")
speech.grid(column=1, row=1, padx=5, pady=5)

pyr = tkinter.PhotoImage(master = master, file = r'Pyracantha/pyracanthaPhoto.png', height=300)
pyr_label = tkinter.Label(master, image = pyr).grid(column = 1, row = 0)

img = tkinter.PhotoImage(master = master, file = r'Pyracantha/m.png')
img_label = tkinter.Label(master, image = img)
img_label.grid(column = 2, row = 0)

next = tkinter.Button(master, text = 'Next', command = next_msg)
next.grid(column=2, row=2, sticky=tkinter.SE, padx=5, pady=5)
master.mainloop()