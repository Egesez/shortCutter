# Shortcut Helper GUI

A user-friendly GUI app that provides quick access to essential links and email information. With a simple hotkey, you can open the interface, copy items to the clipboard, and even paste them directly into the active application. The app also includes an option to open a PDF file directly from the interface and a built-in hotkey to stop all app processes instantly.

## Features

- **Copy and Paste on Command**: Quickly copy your email, webpage link, LinkedIn, or GitHub profile to the clipboard. The app also supports an auto-paste feature, sending the copied text to the active application.
- **PDF Opener**: Easily open a designated PDF file (such as your CV) with one click.
- **Customizable Hotkeys**: 
  - `Alt+Q` to open the main GUI.
  - `Alt+Shift+Q` to close the program immediately.
  - Additional hotkeys (`Alt+1`, `Alt+2`, etc.) to access buttons without using the GUI.

## How It Works

Once started, the app runs in the background, waiting for the `Alt+Q` hotkey to open the GUI near your mouse location. This GUI contains buttons to copy or paste various predefined items and to open a PDF file. When an item is copied, the app sends a `Ctrl+V` command to paste it directly into the currently active field in any application, saving you the hassle of manual pasting.

### Hotkeys
- `Alt+1`: Copy and paste email.
- `Alt+2`: Copy and paste webpage link.
- `Alt+3`: Copy and paste LinkedIn profile link.
- `Alt+4`: Copy and paste GitHub profile link.
- `Alt+5`: Open the PDF file.
- `Alt+Esc`: Close the GUI.
- `Alt+Shift+Q`: Stop all program processes.

## Setup and Installation

1. **Dependencies**: Install the required packages before running the app:
    ```bash
    pip install pyperclip keyboard pyautogui screeninfo
    ```
2. **Run the Application**: Start the application by running:
    ```bash
    python shortcut_helper.py
    ```

3. **Configuration**: Update the `email`, `webpage_link`, `linkedin_link`, `github_link`, and `pdf_path` variables in the code to personalize the links and PDF file.

## Usage

- **Opening the GUI**: Press `Alt+Q` to open the GUI at your mouse location. You’ll see options to copy various information or open your PDF file.
- **Hotkeys for Quick Access**: Use `Alt+1` through `Alt+5` for direct access to each button’s functionality without opening the GUI.
- **Exiting the App**: Press `Alt+Shift+Q` to stop all app processes instantly.

## Notes

- **Clipboard and Paste**: This application copies data to the clipboard using `pyperclip` and then pastes it into the active application using the `keyboard` library. Ensure your cursor is positioned correctly in the target application before activating the paste functionality.
- **OS Compatibility**: The app is currently tailored for Windows, as `os.startfile()` is used to open the PDF file. 
- **Contributions Appreciated**: While this app works smoothly, it’s still a work in progress. All suggestions, improvements, and bug fixes are welcome!

## Future Updates

- **Config file**: I plan to add a configuration file that will allow users to easily set up and customize links, buttons, and other settings.
- **Settings page**: I am working on a settings page that will allow users to add new buttons, modify default buttons, and set custom hotkeys, offering a more personalized experience.
- **Cooler UI?** : Why not? Although it's on the roadmap, it’s not a top priority at the moment.

## Troubleshooting

- **Tcl_AsyncDelete Error**: This error can occur if a function attempts to access Tkinter GUI elements from a non-main thread. This app manages such calls carefully to ensure they’re in the main thread.
- **Hotkey Issues**: If hotkeys persist after exiting, check the task manager to ensure the process has ended or restart the application to clear lingering hooks.
