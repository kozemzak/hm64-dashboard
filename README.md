# HM64 Dashboard

This is an in-progress side project I have been working on to display the game state for Harvest Moon 64. It is meant to be used alongside [OpenEmu](https://openemu.org/) (v2.0.8) with a z64 ROM on MacOS.

## Getting Started

Python 3 is required for this project. You can download the dependencies using pip:

### Server dependencies:
```
python3 -m venv ./src/server/venv
source src/server/venv/bin/activate
pip install -r src/server/requirements.txt
```

### Client dependencies:
```
brew install elm
```

## Server

Right now the server locates and returns a JSON object containing some basic information like dog and horse names and affection, tool levels and number of uses, time and weather information, and stamina and fatigue.

With OpenEmu running and a x64 HM64 ROM named `hm64_rom.z64` loaded, you can view the information using the command below. Note that if there are spaces in the rom name they should be changes to hyphens '-'. For example if the ROM name is 'Harvest Moon 64 (U) [!]', then pass 'Harvest-Moon-64-(U)-[!]' as the argument.

```
sudo python src/server/server.py --rom 'hm64_rom.z64'
```

I plan on adding significantly more features, but will temporarily be transitioning my focus to the frontend.

## Client

The client is an elm application that queries the server for data, and displays it in real time.

To run:
```
cd src/client
./build.sh
open index.html
```

## Acknowledgments

A big thanks to [kirbyarm](https://gamefaqs.gamespot.com/n64/197528-harvest-moon-64/faqs/62453) and [SomeCrazyGuy](https://gamefaqs.gamespot.com/n64/197528-harvest-moon-64/faqs/47358) for their efforts in creating game shark codes for Harvest Moon 64. Having their codes has been immensely helpful for knowing where to search for values in the ROM. And [memorpy](https://github.com/n1nj4sec/memorpy).
