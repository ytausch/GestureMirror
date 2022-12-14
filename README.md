# GestureMirror
Using an APDS9960 gesture sensor and a Raspberry Pi, this project can control an external display and a Sonos speaker.

This project might be handy if you happen to have a Raspberry Pi [smart mirror](https://magicmirror.builders/) that
is connected to an APDS9960 gesture sensor and also a Sonos speaker that you want to control.
You can realize use cases like the following:

> The display should turn on when you make a gesture and should automatically turn off when a timer expires.
Another gesture should turn on the speaker and play from a predefined URI (e. g. a radio station).

## Requirements
* Python 3.7+ (lower 3.x versions might work)
* The setup described above.

## Usage
First, clone this repository and install the dependencies (you are advised to use
[virtual environments](https://docs.python.org/3/library/venv.html)):
```bash
git clone https://github.com/ytausch/GestureMirror.git
cd GestureMirror
pip install -r requirements.txt
```

Then, make sure to personalize `main.py` for your needs.

Finally, start the application:
```bash
cd src
python -m gesturemirror.main
```
