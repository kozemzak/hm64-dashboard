from lookups import *
from Feature import Feature

ALL = 'all'
ANIMALS_GROUP = 'animals'
GIRLS_GROUP = 'girls'
MISC_GROUP = 'misc'
NPC_GROUP = 'npc'
#PHOTOS_GROUP = 'photos'
PLAYER_GROUP = 'player'
#RECIPES_GROUP = 'recipes'
RESOURCES_GROUP = 'resources'
RIVALS_GROUP = 'rivals'
TIME_GROUP = 'time'
TOOLS_GROUP = 'tools'
WEATHER_GROUP = 'weather'

features = {

    'ann_affection': Feature(
        shark_addr = 0x801C3F93,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
    ),
    
    'ann_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x08,
    ),
    
    'ann_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x01,
    ),
    
    'axe_level': Feature(
        shark_addr = 0x80189081,
        n_bytes = 1,
        groups = [ALL, TOOLS_GROUP],
        lookup = LOOKUP_TOOL_LEVEL,
    ),
    
    'axe_uses': Feature(
        shark_addr = 0x8118906E,
        n_bytes = 2,
        groups = [ALL, TOOLS_GROUP],
    ),
    
    'baby_affection': Feature(
        shark_addr = 0x801C3F95,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'bartender_affection': Feature(
        shark_addr = 0x801C3FAC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'bartender_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x10,
    ),
    
    'bartender_gift': Feature(
        shark_addr = 0x8016F8D6,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x02,
    ),
    
    'basil_affection': Feature(
        shark_addr = 0x801C3F9E,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'basil_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x20,
    ),
    
    'basil_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'carpenter_axe_affection': Feature(
        shark_addr = 0x801C3FAF,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'carpenter_axe_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x80,
    ),
    
    'carpenter_axe_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x10,
    ),
    
    'carpenter_master_affection': Feature(
        shark_addr = 0x801C3FB0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'carpenter_master_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x02,
    ),
    
    'carpenter_master_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x40,
    ),
    
    'carpenter_saw_affection': Feature(
        shark_addr = 0x801C3FAE,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'carpenter_saw_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x01,
    ),
    
    'carpenter_saw_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x20,
    ),
    
    'cliff_affection': Feature(
        shark_addr = 0x801C3F99,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
    ),
    
    'cliff_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x01,
    ),
    
    'cliff_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x20,
    ),
    
    'dog_affection': Feature(
        shark_addr = 0x801886B0,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
    ),
    
    'dog_name_char_1': Feature(
        shark_addr = 0x801886B1,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'dog_name_char_2': Feature(
        shark_addr = 0x801886B2,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'dog_name_char_3': Feature(
        shark_addr = 0x801886B3,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'dog_name_char_4': Feature(
        shark_addr = 0x801886B4,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'dog_name_char_5': Feature(
        shark_addr = 0x801886B5,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'dog_name_char_6': Feature(
        shark_addr = 0x801886B6,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'doug_affection': Feature(
        shark_addr = 0x801C3FA0,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
    ),
    
    'doug_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x01,
    ),
    
    'doug_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x20,
    ),
    
    'ellen_affection': Feature(
        shark_addr = 0x801C3F9F,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'ellen_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x40,
    ),
    
    'ellen_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x08,
    ),
    
    'elli_affection': Feature(
        shark_addr = 0x801C3F92,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
    ),
    
    'elli_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x04,
    ),
    
    'elli_gift': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x80,
    ),
    
    'farm_name_char_1': Feature(
        shark_addr = 0x8021E6D2,
        n_bytes = 1,
        groups = [ALL, MISC_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'farm_name_char_2': Feature(
        shark_addr = 0x8021E6D3,
        n_bytes = 1,
        groups = [ALL, MISC_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'farm_name_char_3': Feature(
        shark_addr = 0x8021E6D4,
        n_bytes = 1,
        groups = [ALL, MISC_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'farm_name_char_4': Feature(
        shark_addr = 0x8021E6D5,
        n_bytes = 1,
        groups = [ALL, MISC_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'farm_name_char_5': Feature(
        shark_addr = 0x8021E6D6,
        n_bytes = 1,
        groups = [ALL, MISC_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'farm_name_char_6': Feature(
        shark_addr = 0x8021E6D7,
        n_bytes = 1,
        groups = [ALL, MISC_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'fisherman_affection': Feature(
        shark_addr = 0x801C3FAD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'fisherman_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x20,
    ),
    
    'fisherman_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'gold': Feature(
        shark_addr = 0x811FD60E,
        n_bytes = 4,
        groups = [ALL, RESOURCES_GROUP],
    ),
    
    'gold_shipping_bin': Feature(
        shark_addr = 0x8123738A,
        n_bytes = 4,
        groups = [ALL, RESOURCES_GROUP],
    ),
    
    'gotz_affection': Feature(
        shark_addr = 0x801C3FA1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'gotz_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x02,
    ),
    
    'gotz_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x40,
    ),
    
    'gotz_wife_affection': Feature(
        shark_addr = 0x801C3FA2,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'gotz_wife_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'gotz_wife_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x80,
    ),
    
    'gray_affection': Feature(
        shark_addr = 0x801C3F97,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
    ),
    
    'gray_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x40,
    ),
    
    'gray_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x08,
    ),
    
    'hammer_level': Feature(
        shark_addr = 0x80189082,
        n_bytes = 1,
        groups = [ALL, TOOLS_GROUP],
        lookup = LOOKUP_TOOL_LEVEL,
    ),
    
    'hammer_uses': Feature(
        shark_addr = 0x81189070,
        n_bytes = 2,
        groups = [ALL, TOOLS_GROUP],
    ),
    
    'harris_affection': Feature(
        shark_addr = 0x801C3F96,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
    ),
    
    'harris_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x20,
    ),
    
    'harris_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x04,
    ),
    
    'hoe_level': Feature(
        shark_addr = 0x80189080,
        n_bytes = 1,
        groups = [ALL, TOOLS_GROUP],
        lookup = LOOKUP_TOOL_LEVEL,
    ),
    
    'hoe_uses': Feature(
        shark_addr = 0x8118906C,
        n_bytes = 2,
        groups = [ALL, TOOLS_GROUP],
    ),
    
    'horse_affection': Feature(
        shark_addr = 0x8016FDD0,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
    ),
    
    'horse_name_char_1': Feature(
        shark_addr = 0x8016FDD1,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'horse_name_char_2': Feature(
        shark_addr = 0x8016FDD2,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'horse_name_char_3': Feature(
        shark_addr = 0x8016FDD3,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'horse_name_char_4': Feature(
        shark_addr = 0x8016FDD4,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'horse_name_char_5': Feature(
        shark_addr = 0x8016FDD5,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'horse_name_char_6': Feature(
        shark_addr = 0x8016FDD6,
        n_bytes = 1,
        groups = [ALL, ANIMALS_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'jeff_affection': Feature(
        shark_addr = 0x801C3F98,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
    ),
    
    'jeff_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x80,
    ),
    
    'jeff_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x10,
    ),
    
    'kai_affection': Feature(
        shark_addr = 0x801C3F9A,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
    ),
    
    'kai_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x02,
    ),
    
    'kai_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        groups = [ALL, RIVALS_GROUP],
        mask = 0x40,
    ),
    
    'karen_affection': Feature(
        shark_addr = 0x801C3F94,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
    ),
    
    'karen_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x10,
    ),
    
    'karen_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x02,
    ),
    
    'kent_affection': Feature(
        shark_addr = 0x801C3FA4,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'kent_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x08,
    ),
    
    'kent_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x01,
    ),
    
    'lillia_affection': Feature(
        shark_addr = 0x801C3F9D,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'lillia_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x10,
    ),
    
    'lillia_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x02,
    ),
    
    'maria_affection': Feature(
        shark_addr = 0x801C3F90,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
    ),
    
    'maria_conversation': Feature(
        shark_addr = 0x8016F8B3,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x02,
    ),
    
    'maria_gift': Feature(
        shark_addr = 0x8016F8B3,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x04,
    ),
    
    'may_affection': Feature(
        shark_addr = 0x801C3FA7,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'may_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x40,
    ),
    
    'may_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x08,
    ),
    
    'mayor_affection': Feature(
        shark_addr = 0x801C3F9B,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'mayor_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'mayor_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x80,
    ),
    
    'mayor_wife_affection': Feature(
        shark_addr = 0x801C3F9C,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'mayor_wife_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x08,
    ),
    
    'mayor_wife_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x01,
    ),
    
    'midwife_affection': Feature(
        shark_addr = 0x801C3FA6,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'midwife_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x20,
    ),
    
    'midwife_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'num_fish_caught': Feature(
        shark_addr = 0x8118983A,
        n_bytes = 2,
        groups = [ALL, MISC_GROUP],
    ),
    
    'num_lumber': Feature(
        shark_addr = 0x81189E50,
        n_bytes = 2,
        groups = [ALL, RESOURCES_GROUP],
    ),
    
    'old_woman_affection': Feature(
        shark_addr = 0x801C3FB4,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'old_woman_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x08,
    ),
    
    'old_woman_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x01,
    ),
    
    'old_man_affection': Feature(
        shark_addr = 0x801C3FB5,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'old_man_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x10,
    ),
    
    'old_man_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x02,
    ),
    
    'pastor_affection': Feature(
        shark_addr = 0x801C3FA9,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'pastor_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x80,
    ),
    
    'pastor_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x10,
    ),
    
    'player_alcohol_tolerance': Feature(
        shark_addr = 0x80189E52,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
    ),
    
    'player_fatigue': Feature(
        shark_addr = 0x801890D1,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
    ),
    
    'player_happiness': Feature(
        shark_addr = 0x80182FB8,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
    ),
    
    'player_name_char_1': Feature(
        shark_addr = 0x80189061,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'player_name_char_2': Feature(
        shark_addr = 0x80189062,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'player_name_char_3': Feature(
        shark_addr = 0x80189063,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'player_name_char_4': Feature(
        shark_addr = 0x80189064,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'player_name_char_5': Feature(
        shark_addr = 0x80189065,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'player_name_char_6': Feature(
        shark_addr = 0x80189066,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
        lookup = LOOKUP_NAME_CHAR,
    ),
    
    'player_stamina': Feature(
        shark_addr = 0x80189060,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
    ),
    
    'player_stamina_max': Feature(
        shark_addr = 0x8020563F,
        n_bytes = 1,
        groups = [ALL, PLAYER_GROUP],
    ),
    
    'popuri_affection': Feature(
        shark_addr = 0x801C3F91,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
    ),
    
    'popuri_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x02,
    ),
    
    'popuri_gift': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        groups = [ALL, GIRLS_GROUP],
        mask = 0x40,
    ),
    
    'potion_master_affection': Feature(
        shark_addr = 0x801C3FA3,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'potion_master_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'rick_affection': Feature(
        shark_addr = 0x801C3FA8,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'rick_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x01,
    ),
    
    'rick_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x20,
    ),
    
    'saibara_affection': Feature(
        shark_addr = 0x801C3FAB,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'saibara_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x02,
    ),
    
    'saibara_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x40,
    ),
    
    'shipper_affection': Feature(
        shark_addr = 0x801C3FAA,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'shipper_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x08,
    ),
    
    'shipper_gift': Feature(
        shark_addr = 0x8016F8D6,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x01,
    ),
    
    'sickle_level': Feature(
        shark_addr = 0x8018907F,
        n_bytes = 1,
        groups = [ALL, TOOLS_GROUP],
        lookup = LOOKUP_TOOL_LEVEL,
    ),
    
    'sickle_uses': Feature(
        shark_addr = 0x8118906A,
        n_bytes = 2,
        groups = [ALL, TOOLS_GROUP],
    ),
    
    'sprite_1_affection': Feature(
        shark_addr = 0x801C3FB1,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'sprite_1_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'sprite_1_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x80,
    ),
    
    'sprite_2_affection': Feature(
        shark_addr = 0x801C3FB2,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'sprite_2_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'sprite_2_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x80,
    ),
    
    'sprite_3_affection': Feature(
        shark_addr = 0x801C3FB3,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'sprite_3_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x04,
    ),
    
    'sprite_3_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x80,
    ),
    
    'stu_affection': Feature(
        shark_addr = 0x801C3FA5,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
    ),
    
    'stu_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x10,
    ),
    
    'stu_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        groups = [ALL, NPC_GROUP],
        mask = 0x02,
    ),
    
    'time_day_number': Feature(
        shark_addr = 0x80158260,
        n_bytes = 1,
        groups = [ALL, TIME_GROUP],
    ),
    
    'time_hours': Feature(
        shark_addr = 0x801FB5CA,
        n_bytes = 1,
        groups = [ALL, TIME_GROUP],
    ),
    
    'time_minutes': Feature(
        shark_addr = 0x8017027F,
        n_bytes = 1,
        groups = [ALL, TIME_GROUP],
    ),
    
    'time_season': Feature(
        shark_addr = 0x80182DB1,
        n_bytes = 1,
        groups = [ALL, TIME_GROUP],
        lookup = LOOKUP_SEASON,
    ),
    
    'time_weekday': Feature(
        shark_addr = 0x801FAD90,
        n_bytes = 1,
        groups = [ALL, TIME_GROUP],
        lookup = LOOKUP_WEEKDAY,
    ),
    
    'time_year': Feature(
        shark_addr = 0x801F6F30,
        n_bytes = 1,
        groups = [ALL, TIME_GROUP],
    ),
    
    'water_level': Feature(
        shark_addr = 0x80189083,
        n_bytes = 1,
        groups = [ALL, TOOLS_GROUP],
        lookup = LOOKUP_TOOL_LEVEL,
    ),
    
    'water_remaining': Feature(
        shark_addr = 0x8016FBCD,
        n_bytes = 1,
        groups = [ALL, TOOLS_GROUP],
    ),
    
    'water_uses': Feature(
        shark_addr = 0x81189072,
        n_bytes = 2,
        groups = [ALL, TOOLS_GROUP],
    ),
    
    'weather_today': Feature(
        shark_addr = 0x802373A9,
        n_bytes = 1,
        groups = [ALL, WEATHER_GROUP],
        lookup = LOOKUP_WEATHER,
    ),
    
    'weather_tomorrow': Feature(
        shark_addr = 0x80205238,
        n_bytes = 1,
        groups = [ALL, WEATHER_GROUP],
        lookup = LOOKUP_WEATHER,
    ),

}
