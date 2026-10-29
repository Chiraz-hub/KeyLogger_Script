# Python Keylogger Project

A lightweight, efficient, and educational keyboard event listener implemented in Python using the `pynput` library. This project captures keystrokes asynchronously, batches them in memory to protect system performance, and saves them to a local log file.

## Features

- **Asynchronous Listening**: Runs efficiently in the background using `pynput.keyboard.Listener`.
- **Memory Buffering**: Saves system disk I/O performance by caching keystrokes in RAM and writing them in batches of 10 characters.
- **Clean Logs**: Filters out standard modifier keys (like Shift, Ctrl, and Alt) and translates formatting keys (`Space`, `Enter`, `Tab`) into readable spacing.
- **Graceful Shutdown**: Includes an escape sequence (`Esc` key) that flushes remaining memory buffers to disk before cleanly exiting the process.

##  Installation & Setup

### Prerequisites
- Python 3.8 or higher installed on your system.
- Ensure you have configured your Windows virtual environment (`.venv`) inside the project workspace directory.

### 1. Activate the Virtual Environment
Open your terminal in VS Code and run the appropriate activation script based on your active shell:

- **PowerShell (pwsh):**
  ```powershell
  .venv\Scripts\activate.ps1
  ```
- **Command Prompt (CMD):**
  ```cmd
  .venv\Scripts\activate.bat
  ```

### 2. Install Dependencies
Install the required keyboard handling package within your active virtual environment:
```bash
pip install pynput
```

##  Usage

1. Launch the script using your Python interpreter:
   ```bash
   python keylogger.py
   ```
2. The terminal cursor will blink, indicating the listener is actively running.
3. Open any other application (e.g., text editor, web browser) and begin typing.
4. Keystrokes will write to a newly generated file named `logs.txt` inside your folder after every 10 characters typed.
5. To stop monitoring and cleanly exit the script, return to your terminal or focus on any window and press the **`Esc`** key.

##  Security & Educational Disclaimer

This project was developed strictly for **educational purposes and security analysis**. Understanding how system hooks work is an essential part of malware analysis and ethical hacking. 

- **Authorization Requirement**: Never run monitoring tools, keyloggers, or credential-harvesting software on any device or network for which you do not have explicit, written authorization.
- **Evasion Deficiencies**: This implementation runs as a visible console process and uses standard hooks that are highly visible to modern Antivirus (AV) solutions and Endpoint Detection and Response (EDR) software.
