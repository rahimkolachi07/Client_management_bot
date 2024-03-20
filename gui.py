import tkinter as tk
from tkinter import ttk, font as tkfont
import pywhatkit as kit
import datetime
from gemini import *

def org(text, bot):
    text2 = model(f"write a tasks based on conversation, do brainstorming. focuse on algoritham or model suggested by clint, dataset links or reference suggested by clints or any related information which clint is demenading.make it in bulit points for clints conversation only, ignore freelancer coversation also add title of project with clint name. it must look like professional text.  this is the text. text= [{text}]")
    if bot == 1:
        # Get current time
        now = datetime.datetime.now()

        # Send a WhatsApp message to a group
        kit.sendwhatmsg_to_group("FssBhoVjvG3CkiYE15eB88", text2, now.hour, now.minute + 2)
        return "Auto done"
    else:
        return text2 if text2 else "No text entered"
    

def prog(text, bot):
    text2 = model(f"analyze the conversation and then brainstorm and wrtie python code based on conversation. commet all the code. this is the text. text= [{text}]")
    if bot == 1:
        # Get current time
        now = datetime.datetime.now()

        # Send a WhatsApp message to a group
        kit.sendwhatmsg_to_group("FRErhhwvD17DMXrqU2wixb", text2, now.hour, now.minute + 2)
        return "Auto done"
    else:
        return text2 if text2 else "No text entered"



def display_text():
    entered_text = text_entry.get()
    bot_mode = bot_var.get()
    result = org(entered_text, bot_mode)
    
    # Clear the existing text in the text box
    text_box.delete('1.0', tk.END)
    
    # Insert the new text into the text box
    text_box.insert(tk.END, result)

def display_code():
    entered_text = code_entry.get()
    bot_mode = bot_var.get()
    result = prog(entered_text, bot_mode)
    
    # Clear the existing text in the text box
    code_box.delete('1.0', tk.END)
    
    # Insert the new text into the text box
    code_box.insert(tk.END, result)

root = tk.Tk()
root.title("Hecktobyte - Professional Text Display GUI")
root.geometry("1000x800")  # Set the size of the GUI
root.configure(bg='lightblue')  # Set the background color

# Create a custom font
custom_font = tkfont.Font(family="Helvetica", size=18)
title_font = tkfont.Font(family="Helvetica", size=20, weight="bold")

# Add a title label for your company
title_label = tk.Label(root, text="Hecktobyte", font=title_font, bg='lightblue', fg='darkblue')
title_label.pack(pady=10)

# Increase the size of the tabs
style = ttk.Style()
style.configure('TNotebook.Tab', font=('Helvetica', '18', 'bold'), padding=[12, 12])

notebook = ttk.Notebook(root)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text='Text')
notebook.add(frame2, text='Code')
notebook.pack(padx=10, pady=10)

# Text tab
text_entry = tk.Entry(frame1, font=custom_font, width=50)  # Enlarge the text box
text_entry.pack(pady=10)  # Add some padding

bot_var = tk.IntVar()
bot_button = tk.Checkbutton(frame1, text="Bot", variable=bot_var, font=custom_font, bg='lightblue')
bot_button.pack(pady=5)  # Add some padding

submit_button = tk.Button(frame1, text="Submit", command=display_text, font=custom_font, bg='white')
submit_button.pack(pady=10)  # Add some padding

text_box = tk.Text(frame1, bg='lightgreen', font=custom_font)  # Change the color of the text box
text_box.pack(pady=10)  # Add some padding

# Code tab
code_entry = tk.Entry(frame2, font=custom_font, width=50)  # Enlarge the text box
code_entry.pack(pady=10)  # Add some padding

code_button = tk.Button(frame2, text="Submit", command=display_code, font=custom_font, bg='white')
code_button.pack(pady=10)  # Add some padding

code_box = tk.Text(frame2, bg='lightgreen', font=custom_font)  # Change the color of the text box
code_box.pack(pady=10)  # Add some padding

root.mainloop()