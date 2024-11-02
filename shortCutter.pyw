import tkinter as tk
import pyperclip
import os
import keyboard
import pyautogui
from screeninfo import get_monitors

# Define your links and email
email = "yourgmail@gmail.com"
webpage_link = "https://yourwebsite.com"
linkedin_link = "https://linkedin.com/in/yourprofile"
github_link = "https://github.com/yourusername"
pdf_path = r"path\to\your\pdf"  # Update with your actual PDF path

#global variables
root = None
is_run = True

# Function to copy text to clipboard
def copy_to_clipboard(text, label, root):
    pyperclip.copy(text)
    label.config(text=f"Copied to clipboard: {text}")
    root.after(0, lambda: keyboard.write(text))
    root.after(500, root.destroy)  # Close the window after 0.5 seconds
    remove_hotkeys()  # Remove hotkeys after action is taken

# Function to open a PDF file
def open_pdf(label, root):
    try:
        os.startfile(pdf_path)  
        label.config(text="PDF opened successfully!")
        root.after(500, root.destroy) 
    except Exception as e:
        label.config(text=f"Error: {str(e)}")
    remove_hotkeys() 

# Function to create and open the Tkinter GUI at the mouse position, within monitor bounds
def open_gui():
    global root
    x, y = pyautogui.position()
    monitor = get_monitor_at_mouse()

    if monitor is None:
        screen_width, screen_height = pyautogui.size()
        monitor_x, monitor_y = 0, 0
    else:
        screen_width, screen_height = monitor.width, monitor.height
        monitor_x, monitor_y = monitor.x, monitor.y

    # Define window size
    window_width = 400
    window_height = 500

    # Ensure the window opens within monitor bounds
    x = min(max(x, monitor_x), monitor_x + screen_width - window_width)
    y = min(max(y, monitor_y), monitor_y + screen_height - window_height)

    # Create the Tkinter window
    root = tk.Tk()
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.config(bg="#2b2b2b")
    root.overrideredirect(True) 
    root.attributes("-topmost", True)

    title_bar = tk.Frame(root, bg="#2b2b2b", relief="raised", bd=0)
    title_bar.pack(fill=tk.X)

    def on_enter_close(event):
        close_button.config(bg="#f70d1a", fg="white")

    def on_leave_close(event):
        close_button.config(bg="#2b2b2b", fg="white") 

    close_button = tk.Button(
        title_bar,
        text="✕", 
        command=lambda: (root.destroy(), remove_hotkeys()), 
        bg="#2b2b2b",
        fg="white",
        bd=0,
        font=("Segoe UI", 8, "bold"),  
        activebackground="#ff5f5f",
        activeforeground="white",
        padx=10, pady=5
    )
    close_button.pack(side=tk.RIGHT, padx=0, pady=0)
    close_button.bind("<Enter>", on_enter_close)  
    close_button.bind("<Leave>", on_leave_close)

    status_label = tk.Label(root, text="Select an option:", fg="white", bg="#2b2b2b")
    status_label.pack(pady=10)


    button1 = tk.Button(root, text="Copy Email", command=lambda: copy_to_clipboard(email, status_label, root), width=20, bg="#007acc", fg="white")
    button1.pack(pady=5)

    button2 = tk.Button(root, text="Copy Webpage Link", command=lambda: copy_to_clipboard(webpage_link, status_label, root), width=20, bg="#007acc", fg="white")
    button2.pack(pady=5)

    button3 = tk.Button(root, text="Copy LinkedIn Link", command=lambda: copy_to_clipboard(linkedin_link, status_label, root), width=20, bg="#007acc", fg="white")
    button3.pack(pady=5)

    button4 = tk.Button(root, text="Copy GitHub Link", command=lambda: copy_to_clipboard(github_link, status_label, root), width=20, bg="#007acc", fg="white")
    button4.pack(pady=5)

    button5 = tk.Button(root, text="Open PDF File", command=lambda: open_pdf(status_label, root), width=20, bg="#007acc", fg="white")
    button5.pack(pady=5)

    # Set up temporary hotkeys
    keyboard.add_hotkey("alt+1", lambda: button1.invoke())
    keyboard.add_hotkey("alt+2", lambda: button2.invoke())
    keyboard.add_hotkey("alt+3", lambda: button3.invoke())
    keyboard.add_hotkey("alt+4", lambda: button4.invoke())
    keyboard.add_hotkey("alt+5", lambda: button5.invoke())
    keyboard.add_hotkey("alt+esc", lambda: close_button.invoke())


    root.mainloop()

# Function to remove the temporary hotkeys
def remove_hotkeys():
    keyboard.remove_hotkey("alt+1")
    keyboard.remove_hotkey("alt+2")
    keyboard.remove_hotkey("alt+3")
    keyboard.remove_hotkey("alt+4")
    keyboard.remove_hotkey("alt+5")
    keyboard.remove_hotkey("alt+esc")

# Function to get the monitor where the mouse is currently located
def get_monitor_at_mouse():
    x, y = pyautogui.position()
    for monitor in get_monitors():
        if monitor.x <= x < monitor.x + monitor.width and monitor.y <= y < monitor.y + monitor.height:
            return monitor
    return None 


# function to stop the execution
def stop():
    global is_run, root
    keyboard.remove_all_hotkeys()
    is_run = False
    os._exit(0)

# Hotkey for stopping the all execution
keyboard.add_hotkey("alt+shift+q", stop)



# Main loop to wait for the Alt+Q hotkey to open the GUI
while is_run:
    keyboard.wait("alt+q")
    open_gui()


##ShortCutter
#Ege Sezginer
#2.11.2024
