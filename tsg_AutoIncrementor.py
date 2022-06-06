#main.py
#Author: Augusto Mendes
#E-mail: augustomendes4426[at]gmail.com
#Version 4

import tkinter as tk
import os
import datetime
path = os.getcwd()
path = path+"\\"
#print(path)
y = os.environ['COMPUTERNAME'] + " - Increment"
#print(y)
path = path+y
#print(path)


window = tk.Tk()
window.title("TSG: Auto-Incrementor")
window.geometry("450x700")
window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(1, minsize=200, weight=1)
window.resizable(False, False)

def clipboard_get(): #Paste
    r = tk.Tk()
    r.withdraw()
    return r.clipboard_get()

def clipboard_copy(): #Copy
    r = txt_show.get("1.0","end-1c")
    txt_show.clipboard_clear()
    return txt_show.clipboard_append(r)

def Execute():
    data = []
    data = txt_write.get("1.0","end-1c")
    data = [n for n in data.split()]
    #print(data)

    dataList = []

    x = datetime.datetime.now()
    x = x.strftime(" %d-%B-%Y %Hh %Mm %Ss")
    x = os.environ['COMPUTERNAME'] + (x)+".txt"
    
    #print(x)
    
    try:
        os.makedirs(path)
        
    except OSError:
        print("")
        #print ("Creation of the directory %s failed" % path)
        
    else:
        print("")
        #print ("Successfully created the directory %s" % path)

    x = "\\"+x
    finalFile = path + x
    #print(finalFile)
    f = open(finalFile, "w+")
    
    dataCount = len(data)
    #print(dataCount)


    for i in range(0, dataCount):
        convert = str(i+1)
        convert = convert+"-"
        covertedData = convert+data[i]
        f.write(covertedData+"\n")
        txt_show.insert("end", covertedData + "\n")


txt_write = tk.Text(window)
txt_show = tk.Text(window)

menu_write = tk.Menu(txt_write, tearoff = 0)
menu_write.add_command(label ="Paste")

menu_show = tk.Menu(txt_show, tearoff = 0)
menu_show.add_command(label ="Copy")

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_execute = tk.Button(fr_buttons, text="Execute", command=Execute)

btn_execute.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

yscroll_write = tk.Scrollbar(command=txt_show.yview, orient=tk.VERTICAL)
txt_write.configure(yscrollcommand=yscroll_write.set)

yscroll_show = tk.Scrollbar(command=txt_show.yview, orient=tk.VERTICAL)
txt_show.configure(yscrollcommand=yscroll_show.set)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_write.grid(row=0, column=1, sticky="nsew")
txt_show.grid(row=1, column=1, sticky="nsew")
yscroll_write.grid(row=0, column=2, sticky='nse')
yscroll_show.grid(row=1, column=2, sticky='nse')

lines_write = len(txt_write.get("1.0","end-1c"))
txt_write.yview_scroll(lines_write, 'units')

lines_show = len(txt_show.get("1.0","end-1c"))
txt_show.yview_scroll(lines_show, 'units')

def do_popup_write(event): #Paste
    try: 
        menu_write.tk_popup(event.x_root, event.y_root)
        
        txt_clip = clipboard_get()
        if txt_write.tag_ranges("sel"):
            txt_write.delete('1.0', "end")
            txt_write.insert("end", txt_clip)
            
        else:
            txt_write.insert("end", txt_clip)
        #print(txt_clip)
        
    finally: 
        menu_write.grab_release()
        
def do_popup_show(event): #Copy
    try: 
        menu_show.tk_popup(event.x_root, event.y_root)

        if txt_show.tag_ranges("sel"):
            txt_copy = clipboard_copy()  
        else:
            pass
            
            
            #print(txt_copy)
        
    finally: 
        menu_show.grab_release() 
  
txt_write.bind("<Button-3>", do_popup_write)
txt_show.bind("<Button-3>", do_popup_show)

window.mainloop()
