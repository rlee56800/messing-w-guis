'''
Little monologue about Pyracantha jam
'''
import tkinter
import time

words = [["That's Pyracantha, fire thorn."],
["Don't eat the seeds, they contain cyanide."], 
["The flesh doesn't taste too good, either."], 
["I heard they taste real good as jam."], 
["...but of course it would taste good, jam is just fruit with an obscene amount of sugar."], 
["Why spend all that time straining seeds from a tiny berry when you can use domesticated fruit..."]]

master = tkinter.Tk(className="Pyracantha Jam")
master.geometry("600x400")
master.columnconfigure(1, weight = 60)

#master.columnconfigure(0, weight = 1)

i = 0
def next_msg():
    global i
    global speech
    if i < len(words):
        speech.config(text = words[i])
        i += 1
        print(i)

speech = tkinter.Label(master, text = "")
speech.grid(column=1, row=1, padx=5, pady=5)
next = tkinter.Button(master, text = 'Next', command = next_msg)
next.grid(column=2, row=2, sticky=tkinter.SE, padx=5, pady=5)
master.mainloop()