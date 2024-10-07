
# Keylogger and Clogger Scripts

This repository contains two Python scripts: `keylogger.py` and `clogger.py`. The `keylogger.py` script captures keystrokes and sends logs via email, while `clogger.py` initiates and runs the keylogger.

## Keylogger Overview

### `keylogger.py`
This script captures all keystrokes made on the keyboard and periodically sends the logs to a specified email address.

#### Features:
- Captures keystrokes using the `pynput` library.
- Sends the captured keystrokes via email using the `smtplib` library.
- Logs are sent at regular intervals (configurable via the timer).

#### Code Breakdown:
- **`__init__(self, timer, email, password)`**: Initializes the keylogger with a timer (in seconds) and email credentials.
- **`send_mail(self, email, password, message)`**: Sends the keystroke logs to the specified email address.
- **`process_keys(self, key)`**: Processes the keypress events and stores them in the log.
- **`report(self)`**: Sends the log via email at each interval and resets the log.
- **`start(self)`**: Starts the keylogger and listens for keystrokes.

### `clogger.py`
This script runs the keylogger from `keylogger.py` by creating an instance of the `Keylogger` class with specified parameters.

## Prerequisites

- Python 3.x
- Required Libraries: 
    - `pynput`: Install using `pip install pynput`
    - `smtplib` (default Python library)

## Usage

1. Replace the email and password in `clogger.py` with your own Gmail credentials.
2. Adjust the timer in seconds for how often logs should be sent (currently set to 5 seconds).
3. Run the `clogger.py` script:

```bash
python3 clogger.py
```

## Disclaimer

These scripts are intended for educational purposes only. Logging keystrokes without consent is illegal and unethical. Always ensure you have permission before using these scripts on any system.

# 0x1tsjusthicham