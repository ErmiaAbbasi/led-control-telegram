# LED Control Telegram Bot

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview

This project is a Telegram bot that controls an LED connected to an Arduino with serial communication.  
Use Telegram commands `/on` and `/off` to turn the LED on or off remotely.


![LED Control Gif](https://s33.picofile.com/file/8485428276/20250629_063903.mp4.html)
---

## Requirements

- Python
- `python-telegram-bot` library  
- `pyserial` library  
- Arduino board with LED connected  

---

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/ErmiaAbbasi/led-control-telegram.git
   cd led-control-telegram

2. Install Python dependencies:

    pip install -r requirements.txt

3. Upload the Arduino sketch arduino.ino to your Arduino board.

---

## Usage

Start the bot by sending /start in your Telegram chat.

Use /on to turn the LED ON.

Use /off to turn the LED OFF.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

ErmiaAbbasi2006@gmail.com
