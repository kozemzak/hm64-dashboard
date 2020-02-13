TODO = 'missing'

LOOKUP_ANIMAL_CONDITION = {
    0x00: 'Normal',
    0x01: 'Happy',
    0x02: 'Mad',
    0x03: 'Sick',
    0x04: 'Dead',
}

LOOKUP_ANIMAL_TYPE = {
    0x00: None,
    0x01: 'Calf',
    0x02: 'Cow',
    0x03: None,
    0x04: 'Lamb',
    0x05: 'Sheep',
    0x06: 'Sheared Sheep',
}

LOOKUP_BELONGING_SLOT = {
        0x00: 'Empty',
        0x01: 'Weed',
        0x02: 'Small Rock',
        0x03: 'Lumber',
        0x04: 'Moondrop Flower',
        0x05: 'Pink-Cat-Mint Flower',
        0x07: 'Cake',
        0x08: 'Pie',
        0x09: 'Cookies',
        0x0D: 'Turnip',
        0x0E: 'Potato',
        0x0F: 'Cabbage',
        0x10: 'Tomato',
        0x11: 'Corn',
        0x12: 'Eggplant',
        0x13: 'Strawberry',
        0x14: 'Egg',
        0x15: 'Small Milk',
        0x16: 'Medium Milk',
        0x17: 'Large Milk',
        0x18: 'Gold Milk',
        0x19: 'Normal Wool',
        0x1A: 'High-Quality Wool',
        0x1B: 'Wild Grapes',
        0x1C: 'Veryberry',
        0x1D: 'Tropical Fruit',
        0x1E: 'Walnut',
        0x1F: 'Mushroom',
        0x20: 'Poisonous Mushroom',
        0x22: 'Berry of the Fullmoon Plant',
        0x23: 'Medicinal Herb',
        0x24: 'Edible Herb',
        0x25: 'Small Fish',
        0x26: 'Medium Fish',
        0x27: 'Large Fish',
        0x28: 'Dumpling',
        0x29: 'Cotton Candy',
        0x2A: 'Fried Octopus',
        0x2B: 'Roasted Corn',
        0x2C: 'Candy',
        0x2D: 'Chocolate',
        0x2E: 'Iron Ore',
        0x2F: 'Blue Rock',
        0x30: 'Rare Metal',
        0x31: 'Moonlight Stone',
        0x32: 'Pontata Root',
        0x39: 'Fodder',
}

LOOKUP_BOTTLE_CONTENTS = {
    0x00: 'Empty',
    0x01: 'Water',
    0x02: 'Wine',
    0x03: 'Cure-All Medicine',
    0x04: 'Vitamin Preparation',
    0x05: 'Vitamin Gold',
    0x06: 'Milk',
    0x07: 'Honey',
}

LOOKUP_CHICKEN_CONDITION = {
    0x00: 'Normal',
    0x01: 'Starved',
    0x02: 'Dead',
}

LOOKUP_CHICKEN_TYPE = {
    0x00: None,
    0x01: 'Chick',
    0x02: 'Adult',
}

LOOKUP_ITEM_SLOT = {
    0x00: 'Empty',
    0x01: 'Ocarina',
    0x02: 'Flower Shop Card',
    0x03: 'Bakery Card',
    0x04: 'Broken Music Box',
    0x05: 'Fixed Music Box',
    0x06: 'Door to Heaven Wine',
    0x07: 'Kazadomori',
    0x08: 'Gold Pendant',
    0x09: 'Library Book',
    0x0A: 'Treasure Map',
    0x0B: 'Marbles',
    0x0C: 'Goodluck Charm',
    0x0D: 'Medal Bag',
    0x0E: 'Horse Race Ticket',
    0x0F: 'Dog Race Ticket',
    0x10: 'Potpourri',
    0x11: 'Embroidered Handkerchief',
    0x12: 'Hand-Knit Socks',
    0x13: 'Lucky Bracelet',
    0x14: 'Flower Bath Crystals',
    0x15: 'Stamina Carrot',
}

LOOKUP_LOCATION = {
    0x00: None,
    0x52: 'Outside',
    0x58: 'Barn',
    0x59: 'Chicken Coop',
}

LOOKUP_NAME_CHAR = {
    0x00: '',
    0xA1: 'A',
    0xA2: 'B',
    0xA3: 'C',
    0xA4: 'D',
    0xA5: 'E',
    0xA6: 'F',
    0xA7: 'G',
    0xA8: 'H',
    0xA9: 'I',
    0xAA: 'J',
    0xAB: 'K',
    0xAC: 'L',
    0xAD: 'M',
    0xAE: 'N',
    0xAF: 'O',
    0xB0: 'P',
    0xB1: 'Q',
    0xB2: 'R',
    0xB3: 'S',
    0xB4: 'T',
    0xB5: 'U',
    0xB6: 'V',
    0xB7: 'W',
    0xB8: 'X',
    0xB9: 'Y',
    0xBA: 'Z',
    0xBB: 'a',
    0xBC: 'b',
    0xBD: 'c',
    0xBE: 'd',
    0xBF: 'e',
    0xC0: 'f',
    0xC1: 'g',
    0xC2: 'h',
    0xC3: 'i',
    0xC4: 'j',
    0xC5: 'k',
    0xC6: 'l',
    0xC7: 'm',
    0xC8: 'n',
    0xC9: 'o',
    0xCA: 'p',
    0xCB: 'q',
    0xCC: 'r',
    0xCD: 's',
    0xCE: 't',
    0xCF: 'u',
    0xD0: 'v',
    0xD1: 'w',
    0xD2: 'x',
    0xD3: 'y',
    0xD4: 'z',
    0xD5: '1',
    0xD6: '2',
    0xD7: '3',
    0xD8: '4',
    0xD9: '5',
    0xDA: '6',
    0xDB: '7',
    0xDC: '8',
    0xDD: '9',
    0xDE: '0',
    0xDF: 'U+2753', # question mark
    0xE0: 'U+2757', # exclamation point
    0xE1: 'U+2312', # arc-ed hyphen
    0xE2: 'U+2053', # tilde
    0xE3: 'U+25CF', # middle dot
    0xE4: 'U+3001', # lower left comma
    0xE5: 'U+3002', # left lower open period
    0xE6: 'U+2044', # fraction slash
    0xE7: 'U+2606', # empty star
    0xE8: 'U+2605', # filled star
    0xE9: 'U+FF06', # ampersand
    0xEA: 'U+2661', # empty heart
    0xEB: 'U+2665', # filled heart
    0xEC: 'U+10D0', # fish hook
    0xED: 'U+1F43E', # paw print
    0xEE: ' ',
    0xEF: TODO, # x with 4 dots?
    0xF0: TODO, # empty circle
    0xF1: TODO, # degrees celcius
    0xF6: '-',
    0xF7: TODO, # multiplication
    0xF8: TODO,
    0xF9: TODO,
    0xFA: TODO, # three horizontal middle dots
    0xFB: TODO, # two horizontal middle dots
    0xFC: TODO, # left quotations
    0xFD: TODO, # right quotations
    0xFF: '',
}

LOOKUP_SEASON = {
    0x00: None,
    0x01: 'Spring',
    0x02: 'Summer',
    0x03: 'Fall',
    0x04: 'Winter',
}

LOOKUP_TOOL_LEVEL = {
    0x00: 'Standard',
    0x01: 'Silver',
    0x02: 'Gold',
}

LOOKUP_TOOL_SLOT = {
    0x00: 'Empty',
    0x01: 'Sickle',
    0x02: 'Hoe',
    0x03: 'Axe',
    0x04: 'Hammer',
    0x05: 'Watering Can',
    0x06: 'Cow Milker',
    0x07: 'Cow Bell',
    0x08: 'Brush',
    0x09: 'Sheep Shears',
    0x0A: 'Turnip Seed Bag',
    0x0B: 'Potato Seed Bag',
    0x0C: 'Cabbage Seed Bag',
    0x0D: 'Tomato Seed Bag',
    0x0E: 'Corn Seed Bag',
    0x0F: 'Eggplant Seed Bag',
    0x10: 'Strawberry Seed Bag',
    0x11: 'Moondrop Flower Seed Bag',
    0x12: 'Pink-Cat-Mint Flower Seed Bag',
    0x13: 'Blue-Mist Seed',
    0x14: 'Chicken Feed Bag',
    0x16: 'Baby Bottle',
    0x18: 'Fishing Rod',
    0x19: 'Miracle Potion',
    0x1A: 'Animal Medicine',
    0x1B: 'Grass Seed Bag',
    0x1C: 'Blue Feather',
    0x1D: 'Bottle',
}

LOOKUP_WEATHER = {
    0x01: 'Sunny',
    0x02: 'Rainy',
    0x03: 'Snowy',
    0x04: 'Rainy Festival Day',
    0x05: 'Typhoon'
}

LOOKUP_WEEKDAY = {
    0x00: 'Sunday',
    0x01: 'Monday',
    0x02: 'Tuesday',
    0x03: 'Wednesday',
    0x04: 'Thursday',
    0x05: 'Friday',
    0x06: 'Saturday',
}
