# HM64 Dashboard

This is an in-progress side project I have been working on to display the game state for Harvest Moon 64. It is meant to be used alongside [OpenEmu](https://openemu.org/) (v2.2.1) with a z64 ROM on MacOS.

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

With OpenEmu running and a x64 HM64 ROM named `harvest_moon_64.z64` loaded, you can start the server using the command below. If the ROM is named differently, you will need to edit constants.py in src/server. Note that if there are spaces in the rom name they should be changed to hyphens '-'. For example if the ROM name is 'Harvest Moon 64 (U) [!]', then pass 'Harvest-Moon-64-(U)-[!]' as the argument.

```
sudo python src/server/server.py
```

I plan to change this so that the constants file just becomes a series of optional command line arguments.

Right now the server locates and returns a JSON object containing information about game state. Current features include:
- NPC: affection, conversation, gifts, location bytes
- Player Data: name, stamina, max stamina, happiness, fatigue, alcohol tolerance, sick day total
- Menu Data: tools, belongings, items, bottle contents, year, season, day, weekday, time, gold
- Dog/Horse: names, age, whistled, held/brushed/ridden
- Animal Data: type, name, affection, birthday, age, condition, condition counter, fed, brushed, milked, milk type, fodder remaining
- Chicken Data: type, name, fed, holding, condition, starve counter, location, chicken feed remaining
- Tools: number of uses, level, water remaining
- Other: farm name, gold in shipping bin, lumber, number of fish caught, weather today, weather tomorrow

I will be adding more features, but welcome any requests that you might have.

## Client

The client is an elm application that queries the server for data, and displays it in real time.

To run:
```
cd src/client
./build.sh
open index.html
```

## Acknowledgments

A big thanks to [kirbyarm](https://gamefaqs.gamespot.com/n64/197528-harvest-moon-64/faqs/62453) and [SomeCrazyGuy](https://gamefaqs.gamespot.com/n64/197528-harvest-moon-64/faqs/47358) for their efforts in locating game shark codes and digging into game mechanics for Harvest Moon 64. Having their guides gave me a good starting point for analyzing ROM memory and developing this dashboard.
