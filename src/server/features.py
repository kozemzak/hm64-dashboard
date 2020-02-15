from lookups import *
from Feature import Feature

features = {

    'animal_1_affection': Feature(
        shark_addr = 0x80170280,
        n_bytes = 1,
    ),

    'animal_1_age': Feature(
        shark_addr = 0x801702A1,
        n_bytes = 1,
    ),

    'animal_1_birth_day_number': Feature(
        shark_addr = 0x801702AA,
        n_bytes = 1,
    ),

    'animal_1_birth_season': Feature(
        shark_addr = 0x801702A9,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'animal_1_brushed': Feature(
        shark_addr = 0x801702AD,
        n_bytes = 1,
        mask = 0x20,
    ),

    'animal_1_condition': Feature(
        shark_addr = 0x801702A0,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_CONDITION,
    ),

    'animal_1_condition_counter': Feature(
        shark_addr = 0x801702A2,
        n_bytes = 1,
    ),

    'animal_1_fed': Feature(
        shark_addr = 0x801702AD,
        n_bytes = 1,
        mask = 0x08,
    ),

    'animal_1_gold_milk': Feature(
        shark_addr = 0x801702AB,
        n_bytes = 1,
        mask = 0x00,
    ),

    'animal_1_location': Feature(
        shark_addr = 0x8017029A,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'animal_1_milked': Feature(
        shark_addr = 0x801702AD,
        n_bytes = 1,
        mask = 0x40,
    ),

    'animal_1_name_char_1': Feature(
        shark_addr = 0x80170281,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_1_name_char_2': Feature(
        shark_addr = 0x80170282,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_1_name_char_3': Feature(
        shark_addr = 0x80170283,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_1_name_char_4': Feature(
        shark_addr = 0x80170284,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_1_name_char_5': Feature(
        shark_addr = 0x80170285,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_1_name_char_6': Feature(
        shark_addr = 0x80170286,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_1_talked_to': Feature(
        shark_addr = 0x801702AC,
        n_bytes = 1,
        mask = 0x10,
    ),

    'animal_1_type': Feature(
        shark_addr = 0x8017029F,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_TYPE,
    ),

    'animal_2_affection': Feature(
        shark_addr = 0x801702B0,
        n_bytes = 1,
    ),

    'animal_2_age': Feature(
        shark_addr = 0x801702D1,
        n_bytes = 1,
    ),

    'animal_2_birth_day_number': Feature(
        shark_addr = 0x801702DA,
        n_bytes = 1,
    ),

    'animal_2_birth_season': Feature(
        shark_addr = 0x801702D9,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'animal_2_brushed': Feature(
        shark_addr = 0x801702DD,
        n_bytes = 1,
        mask = 0x20,
    ),

    'animal_2_condition': Feature(
        shark_addr = 0x801702D0,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_CONDITION,
    ),

    'animal_2_condition_counter': Feature(
        shark_addr = 0x801702D2,
        n_bytes = 1,
    ),

    'animal_2_fed': Feature(
        shark_addr = 0x801702DD,
        n_bytes = 1,
        mask = 0x08,
    ),

    'animal_2_gold_milk': Feature(
        shark_addr = 0x801702DB,
        n_bytes = 1,
        mask = 0x00,
    ),

    'animal_2_location': Feature(
        shark_addr = 0x801702CA,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'animal_2_milked': Feature(
        shark_addr = 0x801702DD,
        n_bytes = 1,
        mask = 0x40,
    ),

    'animal_2_name_char_1': Feature(
        shark_addr = 0x801702B1,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_2_name_char_2': Feature(
        shark_addr = 0x801702B2,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_2_name_char_3': Feature(
        shark_addr = 0x801702B3,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_2_name_char_4': Feature(
        shark_addr = 0x801702B4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_2_name_char_5': Feature(
        shark_addr = 0x801702B5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_2_name_char_6': Feature(
        shark_addr = 0x801702B6,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_2_talked_to': Feature(
        shark_addr = 0x801702DC,
        n_bytes = 1,
        mask = 0x10,
    ),

    'animal_2_type': Feature(
        shark_addr = 0x801702CF,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_TYPE,
    ),

    'animal_3_affection': Feature(
        shark_addr = 0x801702E0,
        n_bytes = 1,
    ),

    'animal_3_age': Feature(
        shark_addr = 0x80170301,
        n_bytes = 1,
    ),

    'animal_3_birth_day_number': Feature(
        shark_addr = 0x8017030A,
        n_bytes = 1,
    ),

    'animal_3_birth_season': Feature(
        shark_addr = 0x80170309,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'animal_3_brushed': Feature(
        shark_addr = 0x8017030D,
        n_bytes = 1,
        mask = 0x20,
    ),

    'animal_3_condition': Feature(
        shark_addr = 0x80170300,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_CONDITION,
    ),

    'animal_3_condition_counter': Feature(
        shark_addr = 0x80170302,
        n_bytes = 1,
    ),

    'animal_3_fed': Feature(
        shark_addr = 0x8017030D,
        n_bytes = 1,
        mask = 0x08,
    ),

    'animal_3_gold_milk': Feature(
        shark_addr = 0x8017030B,
        n_bytes = 1,
        mask = 0x00,
    ),

    'animal_3_location': Feature(
        shark_addr = 0x801702FA,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'animal_3_milked': Feature(
        shark_addr = 0x8017030D,
        n_bytes = 1,
        mask = 0x40,
    ),

    'animal_3_name_char_1': Feature(
        shark_addr = 0x801702E1,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_3_name_char_2': Feature(
        shark_addr = 0x801702E2,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_3_name_char_3': Feature(
        shark_addr = 0x801702E3,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_3_name_char_4': Feature(
        shark_addr = 0x801702E4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_3_name_char_5': Feature(
        shark_addr = 0x801702E5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_3_name_char_6': Feature(
        shark_addr = 0x801702E6,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_3_talked_to': Feature(
        shark_addr = 0x8017030C,
        n_bytes = 1,
        mask = 0x10,
    ),

    'animal_3_type': Feature(
        shark_addr = 0x801702FF,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_TYPE,
    ),

    'animal_4_affection': Feature(
        shark_addr = 0x80170310,
        n_bytes = 1,
    ),

    'animal_4_age': Feature(
        shark_addr = 0x80170331,
        n_bytes = 1,
    ),

    'animal_4_birth_day_number': Feature(
        shark_addr = 0x8017033A,
        n_bytes = 1,
    ),

    'animal_4_birth_season': Feature(
        shark_addr = 0x80170339,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'animal_4_brushed': Feature(
        shark_addr = 0x8017033D,
        n_bytes = 1,
        mask = 0x20,
    ),

    'animal_4_condition': Feature(
        shark_addr = 0x80170330,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_CONDITION,
    ),

    'animal_4_condition_counter': Feature(
        shark_addr = 0x80170332,
        n_bytes = 1,
    ),

    'animal_4_fed': Feature(
        shark_addr = 0x8017033D,
        n_bytes = 1,
        mask = 0x08,
    ),

    'animal_4_gold_milk': Feature(
        shark_addr = 0x8017033B,
        n_bytes = 1,
        mask = 0x00,
    ),

    'animal_4_location': Feature(
        shark_addr = 0x8017032A,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'animal_4_milked': Feature(
        shark_addr = 0x8017033D,
        n_bytes = 1,
        mask = 0x40,
    ),

    'animal_4_name_char_1': Feature(
        shark_addr = 0x80170311,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_4_name_char_2': Feature(
        shark_addr = 0x80170312,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_4_name_char_3': Feature(
        shark_addr = 0x80170313,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_4_name_char_4': Feature(
        shark_addr = 0x80170314,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_4_name_char_5': Feature(
        shark_addr = 0x80170315,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_4_name_char_6': Feature(
        shark_addr = 0x80170316,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_4_talked_to': Feature(
        shark_addr = 0x8017033C,
        n_bytes = 1,
        mask = 0x10,
    ),

    'animal_4_type': Feature(
        shark_addr = 0x8017032F,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_TYPE,
    ),

    'animal_5_affection': Feature(
        shark_addr = 0x80170340,
        n_bytes = 1,
    ),

    'animal_5_age': Feature(
        shark_addr = 0x80170361,
        n_bytes = 1,
    ),

    'animal_5_birth_day_number': Feature(
        shark_addr = 0x8017036A,
        n_bytes = 1,
    ),

    'animal_5_birth_season': Feature(
        shark_addr = 0x80170369,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'animal_5_brushed': Feature(
        shark_addr = 0x8017036D,
        n_bytes = 1,
        mask = 0x20,
    ),

    'animal_5_condition': Feature(
        shark_addr = 0x80170360,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_CONDITION,
    ),

    'animal_5_condition_counter': Feature(
        shark_addr = 0x80170362,
        n_bytes = 1,
    ),

    'animal_5_fed': Feature(
        shark_addr = 0x8017036D,
        n_bytes = 1,
        mask = 0x08,
    ),

    'animal_5_gold_milk': Feature(
        shark_addr = 0x8017036B,
        n_bytes = 1,
        mask = 0x00,
    ),

    'animal_5_location': Feature(
        shark_addr = 0x8017035A,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'animal_5_milked': Feature(
        shark_addr = 0x8017036D,
        n_bytes = 1,
        mask = 0x40,
    ),

    'animal_5_name_char_1': Feature(
        shark_addr = 0x80170341,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_5_name_char_2': Feature(
        shark_addr = 0x80170342,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_5_name_char_3': Feature(
        shark_addr = 0x80170343,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_5_name_char_4': Feature(
        shark_addr = 0x80170344,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_5_name_char_5': Feature(
        shark_addr = 0x80170345,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_5_name_char_6': Feature(
        shark_addr = 0x80170346,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_5_talked_to': Feature(
        shark_addr = 0x8017036C,
        n_bytes = 1,
        mask = 0x10,
    ),

    'animal_5_type': Feature(
        shark_addr = 0x8017035F,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_TYPE,
    ),

    'animal_6_affection': Feature(
        shark_addr = 0x80170370,
        n_bytes = 1,
    ),

    'animal_6_age': Feature(
        shark_addr = 0x80170391,
        n_bytes = 1,
    ),

    'animal_6_birth_day_number': Feature(
        shark_addr = 0x8017039A,
        n_bytes = 1,
    ),

    'animal_6_birth_season': Feature(
        shark_addr = 0x80170399,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'animal_6_brushed': Feature(
        shark_addr = 0x8017039D,
        n_bytes = 1,
        mask = 0x20,
    ),

    'animal_6_condition': Feature(
        shark_addr = 0x80170390,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_CONDITION,
    ),

    'animal_6_condition_counter': Feature(
        shark_addr = 0x80170392,
        n_bytes = 1,
    ),

    'animal_6_fed': Feature(
        shark_addr = 0x8017039D,
        n_bytes = 1,
        mask = 0x08,
    ),

    'animal_6_gold_milk': Feature(
        shark_addr = 0x8017039B,
        n_bytes = 1,
        mask = 0x00,
    ),

    'animal_6_location': Feature(
        shark_addr = 0x8017038A,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'animal_6_milked': Feature(
        shark_addr = 0x8017039D,
        n_bytes = 1,
        mask = 0x40,
    ),

    'animal_6_name_char_1': Feature(
        shark_addr = 0x80170371,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_6_name_char_2': Feature(
        shark_addr = 0x80170372,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_6_name_char_3': Feature(
        shark_addr = 0x80170373,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_6_name_char_4': Feature(
        shark_addr = 0x80170374,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_6_name_char_5': Feature(
        shark_addr = 0x80170375,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_6_name_char_6': Feature(
        shark_addr = 0x80170376,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_6_talked_to': Feature(
        shark_addr = 0x8017039C,
        n_bytes = 1,
        mask = 0x10,
    ),

    'animal_6_type': Feature(
        shark_addr = 0x8017038F,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_TYPE,
    ),

    'animal_7_affection': Feature(
        shark_addr = 0x801703A0,
        n_bytes = 1,
    ),

    'animal_7_age': Feature(
        shark_addr = 0x801703C1,
        n_bytes = 1,
    ),

    'animal_7_birth_day_number': Feature(
        shark_addr = 0x801703CA,
        n_bytes = 1,
    ),

    'animal_7_birth_season': Feature(
        shark_addr = 0x801703C9,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'animal_7_brushed': Feature(
        shark_addr = 0x801703CD,
        n_bytes = 1,
        mask = 0x20,
    ),

    'animal_7_condition': Feature(
        shark_addr = 0x801703C0,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_CONDITION,
    ),

    'animal_7_condition_counter': Feature(
        shark_addr = 0x801703C2,
        n_bytes = 1,
    ),

    'animal_7_fed': Feature(
        shark_addr = 0x801703CD,
        n_bytes = 1,
        mask = 0x08,
    ),

    'animal_7_gold_milk': Feature(
        shark_addr = 0x801703CB,
        n_bytes = 1,
        mask = 0x00,
    ),

    'animal_7_location': Feature(
        shark_addr = 0x801703BA,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'animal_7_milked': Feature(
        shark_addr = 0x801703CD,
        n_bytes = 1,
        mask = 0x40,
    ),

    'animal_7_name_char_1': Feature(
        shark_addr = 0x801703A1,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_7_name_char_2': Feature(
        shark_addr = 0x801703A2,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_7_name_char_3': Feature(
        shark_addr = 0x801703A3,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_7_name_char_4': Feature(
        shark_addr = 0x801703A4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_7_name_char_5': Feature(
        shark_addr = 0x801703A5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_7_name_char_6': Feature(
        shark_addr = 0x801703A6,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_7_talked_to': Feature(
        shark_addr = 0x801703CC,
        n_bytes = 1,
        mask = 0x10,
    ),

    'animal_7_type': Feature(
        shark_addr = 0x801703BF,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_TYPE,
    ),

    'animal_8_affection': Feature(
        shark_addr = 0x801703D0,
        n_bytes = 1,
    ),

    'animal_8_age': Feature(
        shark_addr = 0x801703F1,
        n_bytes = 1,
    ),

    'animal_8_birth_day_number': Feature(
        shark_addr = 0x801703FA,
        n_bytes = 1,
    ),

    'animal_8_birth_season': Feature(
        shark_addr = 0x801703F9,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'animal_8_brushed': Feature(
        shark_addr = 0x801703FD,
        n_bytes = 1,
        mask = 0x20,
    ),

    'animal_8_condition': Feature(
        shark_addr = 0x801703F0,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_CONDITION,
    ),

    'animal_8_condition_counter': Feature(
        shark_addr = 0x801703F2,
        n_bytes = 1,
    ),

    'animal_8_fed': Feature(
        shark_addr = 0x801703FD,
        n_bytes = 1,
        mask = 0x08,
    ),

    'animal_8_gold_milk': Feature(
        shark_addr = 0x801703FB,
        n_bytes = 1,
        mask = 0x00,
    ),

    'animal_8_location': Feature(
        shark_addr = 0x801703EA,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'animal_8_milked': Feature(
        shark_addr = 0x801703FD,
        n_bytes = 1,
        mask = 0x40,
    ),

    'animal_8_name_char_1': Feature(
        shark_addr = 0x801703D1,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_8_name_char_2': Feature(
        shark_addr = 0x801703D2,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_8_name_char_3': Feature(
        shark_addr = 0x801703D3,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_8_name_char_4': Feature(
        shark_addr = 0x801703D4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_8_name_char_5': Feature(
        shark_addr = 0x801703D5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_8_name_char_6': Feature(
        shark_addr = 0x801703D6,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'animal_8_talked_to': Feature(
        shark_addr = 0x801703FC,
        n_bytes = 1,
        mask = 0x10,
    ),

    'animal_8_type': Feature(
        shark_addr = 0x801703EF,
        n_bytes = 1,
        lookup = LOOKUP_ANIMAL_TYPE,
    ),

    'ann_affection': Feature(
        shark_addr = 0x801C3F93,
        n_bytes = 1,
    ),

    'ann_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        mask = 0x08,
    ),

    'ann_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        mask = 0x01,
    ),

    'ann_location_byte': Feature(
        shark_addr = 0x801FBA6B,
        n_bytes = 1,
    ),

    'axe_level': Feature(
        shark_addr = 0x80189081,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_LEVEL,
    ),

    'axe_uses': Feature(
        shark_addr = 0x8118906E,
        n_bytes = 2,
    ),

    'baby_affection': Feature(
        shark_addr = 0x801C3F95,
        n_bytes = 1,
    ),

    'baby_location_byte': Feature(
        shark_addr = 0x801FBABB,
        n_bytes = 1,
    ),

    'bartender_affection': Feature(
        shark_addr = 0x801C3FAC,
        n_bytes = 1,
    ),

    'bartender_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        mask = 0x10,
    ),

    'bartender_gift': Feature(
        shark_addr = 0x8016F8D6,
        n_bytes = 1,
        mask = 0x02,
    ),

    'bartender_location_byte': Feature(
        shark_addr = 0x801FBE53,
        n_bytes = 1,
    ),

    'basil_affection': Feature(
        shark_addr = 0x801C3F9E,
        n_bytes = 1,
    ),

    'basil_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        mask = 0x20,
    ),

    'basil_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        mask = 0x04,
    ),

    'basil_location_byte': Feature(
        shark_addr = 0x801FBC23,
        n_bytes = 1,
    ),

    'belonging_slot_1': Feature(
        shark_addr = 0x80189084,
        n_bytes = 1,
        lookup = LOOKUP_BELONGING_SLOT,
    ),

    'belonging_slot_2': Feature(
        shark_addr = 0x80189085,
        n_bytes = 1,
        lookup = LOOKUP_BELONGING_SLOT,
    ),

    'belonging_slot_3': Feature(
        shark_addr = 0x80189086,
        n_bytes = 1,
        lookup = LOOKUP_BELONGING_SLOT,
    ),

    'belonging_slot_4': Feature(
        shark_addr = 0x80189087,
        n_bytes = 1,
        lookup = LOOKUP_BELONGING_SLOT,
    ),

    'belonging_slot_5': Feature(
        shark_addr = 0x80189088,
        n_bytes = 1,
        lookup = LOOKUP_BELONGING_SLOT,
    ),

    'belonging_slot_6': Feature(
        shark_addr = 0x80189089,
        n_bytes = 1,
        lookup = LOOKUP_BELONGING_SLOT,
    ),

    'belonging_slot_7': Feature(
        shark_addr = 0x8018908A,
        n_bytes = 1,
        lookup = LOOKUP_BELONGING_SLOT,
    ),

    'belonging_slot_8': Feature(
        shark_addr = 0x8018908B,
        n_bytes = 1,
        lookup = LOOKUP_BELONGING_SLOT,
    ),

    'bottle_contents': Feature(
        shark_addr = 0x8018907E,
        n_bytes = 1,
        lookup = LOOKUP_BOTTLE_CONTENTS,
    ),

    'carpenter_axe_affection': Feature(
        shark_addr = 0x801C3FAF,
        n_bytes = 1,
    ),

    'carpenter_axe_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x80,
    ),

    'carpenter_axe_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x10,
    ),

    'carpenter_axe_location_byte': Feature(
        shark_addr = 0x801FBECB,
        n_bytes = 1,
    ),

    'carpenter_master_affection': Feature(
        shark_addr = 0x801C3FB0,
        n_bytes = 1,
    ),

    'carpenter_master_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        mask = 0x02,
    ),

    'carpenter_master_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x40,
    ),

    'carpenter_master_location_byte': Feature(
        shark_addr = 0x801FBEF3,
        n_bytes = 1,
    ),

    'carpenter_saw_affection': Feature(
        shark_addr = 0x801C3FAE,
        n_bytes = 1,
    ),

    'carpenter_saw_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        mask = 0x01,
    ),

    'carpenter_saw_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x20,
    ),

    'carpenter_saw_location_byte': Feature(
        shark_addr = 0x801FBEA3,
        n_bytes = 1,
    ),

    'chicken_1_condition': Feature(
        shark_addr = 0x801C3C0D,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_CONDITION,
    ),

    'chicken_1_fed': Feature(
        shark_addr = 0x801C3C11,
        n_bytes = 1,
        mask = 0x10,
    ),

    'chicken_1_holding': Feature(
        shark_addr = 0x801C3C11,
        n_bytes = 1,
        mask = 0x08,
    ),

    'chicken_1_location': Feature(
        shark_addr = 0x801C3C06,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'chicken_1_name_char_1': Feature(
        shark_addr = 0x801C3BF0,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_1_name_char_2': Feature(
        shark_addr = 0x801C3BF1,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_1_name_char_3': Feature(
        shark_addr = 0x801C3BF2,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_1_name_char_4': Feature(
        shark_addr = 0x801C3BF3,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_1_name_char_5': Feature(
        shark_addr = 0x801C3BF4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_1_name_char_6': Feature(
        shark_addr = 0x801C3BF5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_1_starve_counter': Feature(
        shark_addr = 0x801C3C0F,
        n_bytes = 1,
    ),

    'chicken_1_type': Feature(
        shark_addr = 0x801C3C0C,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_TYPE,
    ),

    'chicken_2_condition': Feature(
        shark_addr = 0x801C3C31,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_CONDITION,
    ),

    'chicken_2_fed': Feature(
        shark_addr = 0x801C3C35,
        n_bytes = 1,
        mask = 0x10,
    ),

    'chicken_2_holding': Feature(
        shark_addr = 0x801C3C35,
        n_bytes = 1,
        mask = 0x08,
    ),

    'chicken_2_location': Feature(
        shark_addr = 0x801C3C2A,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'chicken_2_name_char_1': Feature(
        shark_addr = 0x801C3C14,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_2_name_char_2': Feature(
        shark_addr = 0x801C3C15,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_2_name_char_3': Feature(
        shark_addr = 0x801C3C16,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_2_name_char_4': Feature(
        shark_addr = 0x801C3C17,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_2_name_char_5': Feature(
        shark_addr = 0x801C3C18,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_2_name_char_6': Feature(
        shark_addr = 0x801C3C19,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_2_starve_counter': Feature(
        shark_addr = 0x801C3C33,
        n_bytes = 1,
    ),

    'chicken_2_type': Feature(
        shark_addr = 0x801C3C30,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_TYPE,
    ),

    'chicken_3_condition': Feature(
        shark_addr = 0x801C3C55,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_CONDITION,
    ),

    'chicken_3_fed': Feature(
        shark_addr = 0x801C3C59,
        n_bytes = 1,
        mask = 0x10,
    ),

    'chicken_3_holding': Feature(
        shark_addr = 0x801C3C59,
        n_bytes = 1,
        mask = 0x08,
    ),

    'chicken_3_location': Feature(
        shark_addr = 0x801C3C4E,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'chicken_3_name_char_1': Feature(
        shark_addr = 0x801C3C38,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_3_name_char_2': Feature(
        shark_addr = 0x801C3C39,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_3_name_char_3': Feature(
        shark_addr = 0x801C3C3A,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_3_name_char_4': Feature(
        shark_addr = 0x801C3C3B,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_3_name_char_5': Feature(
        shark_addr = 0x801C3C3C,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_3_name_char_6': Feature(
        shark_addr = 0x801C3C3D,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_3_starve_counter': Feature(
        shark_addr = 0x801C3C57,
        n_bytes = 1,
    ),

    'chicken_3_type': Feature(
        shark_addr = 0x801C3C54,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_TYPE,
    ),

    'chicken_4_condition': Feature(
        shark_addr = 0x801C3C79,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_CONDITION,
    ),

    'chicken_4_fed': Feature(
        shark_addr = 0x801C3C7D,
        n_bytes = 1,
        mask = 0x10,
    ),

    'chicken_4_holding': Feature(
        shark_addr = 0x801C3C7D,
        n_bytes = 1,
        mask = 0x08,
    ),

    'chicken_4_location': Feature(
        shark_addr = 0x801C3C72,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'chicken_4_name_char_1': Feature(
        shark_addr = 0x801C3C5C,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_4_name_char_2': Feature(
        shark_addr = 0x801C3C5D,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_4_name_char_3': Feature(
        shark_addr = 0x801C3C5E,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_4_name_char_4': Feature(
        shark_addr = 0x801C3C5F,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_4_name_char_5': Feature(
        shark_addr = 0x801C3C60,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_4_name_char_6': Feature(
        shark_addr = 0x801C3C61,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_4_starve_counter': Feature(
        shark_addr = 0x801C3C7B,
        n_bytes = 1,
    ),

    'chicken_4_type': Feature(
        shark_addr = 0x801C3C78,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_TYPE,
    ),

    'chicken_5_condition': Feature(
        shark_addr = 0x801C3C9D,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_CONDITION,
    ),

    'chicken_5_fed': Feature(
        shark_addr = 0x801C3CA1,
        n_bytes = 1,
        mask = 0x10,
    ),

    'chicken_5_holding': Feature(
        shark_addr = 0x801C3CA1,
        n_bytes = 1,
        mask = 0x08,
    ),

    'chicken_5_location': Feature(
        shark_addr = 0x801C3C96,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'chicken_5_name_char_1': Feature(
        shark_addr = 0x801C3C80,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_5_name_char_2': Feature(
        shark_addr = 0x801C3C81,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_5_name_char_3': Feature(
        shark_addr = 0x801C3C82,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_5_name_char_4': Feature(
        shark_addr = 0x801C3C83,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_5_name_char_5': Feature(
        shark_addr = 0x801C3C84,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_5_name_char_6': Feature(
        shark_addr = 0x801C3C85,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_5_starve_counter': Feature(
        shark_addr = 0x801C3C9F,
        n_bytes = 1,
    ),

    'chicken_5_type': Feature(
        shark_addr = 0x801C3C9C,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_TYPE,
    ),

    'chicken_6_condition': Feature(
        shark_addr = 0x801C3CC1,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_CONDITION,
    ),

    'chicken_6_fed': Feature(
        shark_addr = 0x801C3CC5,
        n_bytes = 1,
        mask = 0x10,
    ),

    'chicken_6_holding': Feature(
        shark_addr = 0x801C3CC5,
        n_bytes = 1,
        mask = 0x08,
    ),

    'chicken_6_location': Feature(
        shark_addr = 0x801C3CBA,
        n_bytes = 1,
        lookup = LOOKUP_LOCATION,
    ),

    'chicken_6_name_char_1': Feature(
        shark_addr = 0x801C3CA4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_6_name_char_2': Feature(
        shark_addr = 0x801C3CA5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_6_name_char_3': Feature(
        shark_addr = 0x801C3CA6,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_6_name_char_4': Feature(
        shark_addr = 0x801C3CA7,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_6_name_char_5': Feature(
        shark_addr = 0x801C3CA8,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_6_name_char_6': Feature(
        shark_addr = 0x801C3CA9,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'chicken_6_starve_counter': Feature(
        shark_addr = 0x801C3CC3,
        n_bytes = 1,
    ),

    'chicken_6_type': Feature(
        shark_addr = 0x801C3CC0,
        n_bytes = 1,
        lookup = LOOKUP_CHICKEN_TYPE,
    ),

    'cliff_affection': Feature(
        shark_addr = 0x801C3F99,
        n_bytes = 1,
    ),

    'cliff_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        mask = 0x01,
    ),

    'cliff_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        mask = 0x20,
    ),

    'cliff_location_byte': Feature(
        shark_addr = 0x801FBB5B,
        n_bytes = 1,
    ),

    'dog_affection': Feature(
        shark_addr = 0x801886B0,
        n_bytes = 1,
    ),

    'dog_name_char_1': Feature(
        shark_addr = 0x801886B1,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'dog_name_char_2': Feature(
        shark_addr = 0x801886B2,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'dog_name_char_3': Feature(
        shark_addr = 0x801886B3,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'dog_name_char_4': Feature(
        shark_addr = 0x801886B4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'dog_name_char_5': Feature(
        shark_addr = 0x801886B5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'dog_name_char_6': Feature(
        shark_addr = 0x801886B6,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'doug_affection': Feature(
        shark_addr = 0x801C3FA0,
        n_bytes = 1,
    ),

    'doug_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        mask = 0x01,
    ),

    'doug_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        mask = 0x20,
    ),

    'doug_location_byte': Feature(
        shark_addr = 0x801FBC73,
        n_bytes = 1,
    ),

    'ellen_affection': Feature(
        shark_addr = 0x801C3F9F,
        n_bytes = 1,
    ),

    'ellen_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        mask = 0x40,
    ),

    'ellen_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        mask = 0x08,
    ),

    'ellen_location_byte': Feature(
        shark_addr = 0x801FBC4B,
        n_bytes = 1,
    ),

    'elli_affection': Feature(
        shark_addr = 0x801C3F92,
        n_bytes = 1,
    ),

    'elli_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        mask = 0x04,
    ),

    'elli_gift': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        mask = 0x80,
    ),

    'elli_location_byte': Feature(
        shark_addr = 0x801FBA43,
        n_bytes = 1,
    ),

    'farm_name_char_1': Feature(
        shark_addr = 0x8021E6D2,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'farm_name_char_2': Feature(
        shark_addr = 0x8021E6D3,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'farm_name_char_3': Feature(
        shark_addr = 0x8021E6D4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'farm_name_char_4': Feature(
        shark_addr = 0x8021E6D5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'farm_name_char_5': Feature(
        shark_addr = 0x8021E6D6,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'farm_name_char_6': Feature(
        shark_addr = 0x8021E6D7,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'fisherman_affection': Feature(
        shark_addr = 0x801C3FAD,
        n_bytes = 1,
    ),

    'fisherman_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        mask = 0x20,
    ),

    'fisherman_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        mask = 0x04,
    ),

    'fisherman_location_byte': Feature(
        shark_addr = 0x801FBE7B,
        n_bytes = 1,
    ),

    'gold': Feature(
        shark_addr = 0x811FD60E,
        n_bytes = 4,
    ),

    'gold_shipping_bin': Feature(
        shark_addr = 0x8123738A,
        n_bytes = 4,
    ),

    'gotz_affection': Feature(
        shark_addr = 0x801C3FA1,
        n_bytes = 1,
    ),

    'gotz_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        mask = 0x02,
    ),

    'gotz_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        mask = 0x40,
    ),

    'gotz_location_byte': Feature(
        shark_addr = 0x801FBC9B,
        n_bytes = 1,
    ),

    'gotz_wife_affection': Feature(
        shark_addr = 0x801C3FA2,
        n_bytes = 1,
    ),

    'gotz_wife_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        mask = 0x04,
    ),

    'gotz_wife_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        mask = 0x80,
    ),

    'gotz_wife_location_byte': Feature(
        shark_addr = 0x801FBCC3,
        n_bytes = 1,
    ),

    'gourmet_location_byte': Feature(
        shark_addr = 0x801FC033,
        n_bytes = 1,
    ),

    'gray_affection': Feature(
        shark_addr = 0x801C3F97,
        n_bytes = 1,
    ),

    'gray_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        mask = 0x40,
    ),

    'gray_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        mask = 0x08,
    ),

    'gray_location_byte': Feature(
        shark_addr = 0x801FBB0B,
        n_bytes = 1,
    ),

    'hammer_level': Feature(
        shark_addr = 0x80189082,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_LEVEL,
    ),

    'hammer_uses': Feature(
        shark_addr = 0x81189070,
        n_bytes = 2,
    ),

    'harris_affection': Feature(
        shark_addr = 0x801C3F96,
        n_bytes = 1,
    ),

    'harris_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        mask = 0x20,
    ),

    'harris_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        mask = 0x04,
    ),

    'harris_location_byte': Feature(
        shark_addr = 0x801FBAE3,
        n_bytes = 1,
    ),

    'hoe_level': Feature(
        shark_addr = 0x80189080,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_LEVEL,
    ),

    'hoe_uses': Feature(
        shark_addr = 0x8118906C,
        n_bytes = 2,
    ),

    'horse_affection': Feature(
        shark_addr = 0x8016FDD0,
        n_bytes = 1,
    ),

    'horse_age': Feature(
        shark_addr = 0x8016FDED,
        n_bytes = 1,
    ),

    'horse_name_char_1': Feature(
        shark_addr = 0x8016FDD1,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'horse_name_char_2': Feature(
        shark_addr = 0x8016FDD2,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'horse_name_char_3': Feature(
        shark_addr = 0x8016FDD3,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'horse_name_char_4': Feature(
        shark_addr = 0x8016FDD4,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'horse_name_char_5': Feature(
        shark_addr = 0x8016FDD5,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'horse_name_char_6': Feature(
        shark_addr = 0x8016FDD6,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'item_slot_1': Feature(
        shark_addr = 0x8018908E,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_2': Feature(
        shark_addr = 0x8018908F,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_3': Feature(
        shark_addr = 0x80189090,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_4': Feature(
        shark_addr = 0x80189091,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_5': Feature(
        shark_addr = 0x80189092,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_6': Feature(
        shark_addr = 0x80189093,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_7': Feature(
        shark_addr = 0x80189094,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_8': Feature(
        shark_addr = 0x80189095,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_9': Feature(
        shark_addr = 0x80189096,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_10': Feature(
        shark_addr = 0x80189097,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_11': Feature(
        shark_addr = 0x80189098,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_12': Feature(
        shark_addr = 0x80189099,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_13': Feature(
        shark_addr = 0x8018909A,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_14': Feature(
        shark_addr = 0x8018909B,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_15': Feature(
        shark_addr = 0x8018909C,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_16': Feature(
        shark_addr = 0x8018909D,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_17': Feature(
        shark_addr = 0x8018909E,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_18': Feature(
        shark_addr = 0x8018909F,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_19': Feature(
        shark_addr = 0x801890A0,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_20': Feature(
        shark_addr = 0x801890A1,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_21': Feature(
        shark_addr = 0x801890A2,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_22': Feature(
        shark_addr = 0x801890A3,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_23': Feature(
        shark_addr = 0x801890A4,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'item_slot_24': Feature(
        shark_addr = 0x801890A5,
        n_bytes = 1,
        lookup = LOOKUP_ITEM_SLOT,
    ),

    'jeff_affection': Feature(
        shark_addr = 0x801C3F98,
        n_bytes = 1,
    ),

    'jeff_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        mask = 0x80,
    ),

    'jeff_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        mask = 0x10,
    ),

    'jeff_location_byte': Feature(
        shark_addr = 0x801FBB33,
        n_bytes = 1,
    ),

    'kai_affection': Feature(
        shark_addr = 0x801C3F9A,
        n_bytes = 1,
    ),

    'kai_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        mask = 0x02,
    ),

    'kai_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        mask = 0x40,
    ),

    'kai_location_byte': Feature(
        shark_addr = 0x801FBB83,
        n_bytes = 1,
    ),

    'kappa_location_byte': Feature(
        shark_addr = 0x80189147,
        n_bytes = 1,
    ),

    'karen_affection': Feature(
        shark_addr = 0x801C3F94,
        n_bytes = 1,
    ),

    'karen_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        mask = 0x10,
    ),

    'karen_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        mask = 0x02,
    ),

    'karen_location_byte': Feature(
        shark_addr = 0x801FBA93,
        n_bytes = 1,
    ),

    'kent_affection': Feature(
        shark_addr = 0x801C3FA4,
        n_bytes = 1,
    ),

    'kent_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x08,
    ),

    'kent_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x01,
    ),

    'kent_location_byte': Feature(
        shark_addr = 0x801FBD13,
        n_bytes = 1,
    ),

    'lillia_affection': Feature(
        shark_addr = 0x801C3F9D,
        n_bytes = 1,
    ),

    'lillia_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        mask = 0x10,
    ),

    'lillia_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        mask = 0x02,
    ),

    'lillia_location_byte': Feature(
        shark_addr = 0x801FBBFB,
        n_bytes = 1,
    ),

    'maria_affection': Feature(
        shark_addr = 0x801C3F90,
        n_bytes = 1,
    ),

    'maria_conversation': Feature(
        shark_addr = 0x8016F8B3,
        n_bytes = 1,
        mask = 0x02,
    ),

    'maria_gift': Feature(
        shark_addr = 0x8016F8B3,
        n_bytes = 1,
        mask = 0x04,
    ),

    'maria_location_byte': Feature(
        shark_addr = 0x801FB9F3,
        n_bytes = 1,
    ),

    'may_affection': Feature(
        shark_addr = 0x801C3FA7,
        n_bytes = 1,
    ),

    'may_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x40,
    ),

    'may_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x08,
    ),

    'may_location_byte': Feature(
        shark_addr = 0x801FBD8B,
        n_bytes = 1,
    ),

    'mayor_affection': Feature(
        shark_addr = 0x801C3F9B,
        n_bytes = 1,
    ),

    'mayor_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        mask = 0x04,
    ),

    'mayor_gift': Feature(
        shark_addr = 0x8016F8D2,
        n_bytes = 1,
        mask = 0x80,
    ),

    'mayor_location_byte': Feature(
        shark_addr = 0x801FBBAB,
        n_bytes = 1,
    ),

    'mayor_wife_affection': Feature(
        shark_addr = 0x801C3F9C,
        n_bytes = 1,
    ),

    'mayor_wife_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        mask = 0x08,
    ),

    'mayor_wife_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        mask = 0x01,
    ),

    'mayor_wife_location_byte': Feature(
        shark_addr = 0x801FBBD3,
        n_bytes = 1,
    ),

    'midwife_affection': Feature(
        shark_addr = 0x801C3FA6,
        n_bytes = 1,
    ),

    'midwife_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x20,
    ),

    'midwife_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x04,
    ),

    'midwife_location_byte': Feature(
        shark_addr = 0x801FBD63,
        n_bytes = 1,
    ),

    'num_chicken_feed': Feature(
        shark_addr = 0x81237410,
        n_bytes = 2,
    ),

    'num_fish_caught': Feature(
        shark_addr = 0x8118983A,
        n_bytes = 2,
    ),

    'num_fodder': Feature(
        shark_addr = 0x81180714,
        n_bytes = 2,
    ),

    'num_lumber': Feature(
        shark_addr = 0x81189E50,
        n_bytes = 2,
    ),

    'old_man_affection': Feature(
        shark_addr = 0x801C3FB5,
        n_bytes = 1,
    ),

    'old_man_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        mask = 0x10,
    ),

    'old_man_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        mask = 0x02,
    ),

    'old_man_location_byte': Feature(
        shark_addr = 0x801FBF93,
        n_bytes = 1,
    ),

    'old_woman_affection': Feature(
        shark_addr = 0x801C3FB4,
        n_bytes = 1,
    ),

    'old_woman_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        mask = 0x08,
    ),

    'old_woman_gift': Feature(
        shark_addr = 0x8016F8D7,
        n_bytes = 1,
        mask = 0x01,
    ),

    'old_woman_location_byte': Feature(
        shark_addr = 0x801FBFBB,
        n_bytes = 1,
    ),

    'pastor_affection': Feature(
        shark_addr = 0x801C3FA9,
        n_bytes = 1,
    ),

    'pastor_conversation': Feature(
        shark_addr = 0x8016F8CE,
        n_bytes = 1,
        mask = 0x80,
    ),

    'pastor_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        mask = 0x10,
    ),

    'pastor_location_byte': Feature(
        shark_addr = 0x801FBDDB,
        n_bytes = 1,
    ),

    'player_alcohol_tolerance': Feature(
        shark_addr = 0x80189E52,
        n_bytes = 1,
    ),

    'player_fatigue': Feature(
        shark_addr = 0x801890D1,
        n_bytes = 1,
    ),

    'player_happiness': Feature(
        shark_addr = 0x80182FB8,
        n_bytes = 1,
    ),

    'player_name_char_1': Feature(
        shark_addr = 0x80189061,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'player_name_char_2': Feature(
        shark_addr = 0x80189062,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'player_name_char_3': Feature(
        shark_addr = 0x80189063,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'player_name_char_4': Feature(
        shark_addr = 0x80189064,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'player_name_char_5': Feature(
        shark_addr = 0x80189065,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'player_name_char_6': Feature(
        shark_addr = 0x80189066,
        n_bytes = 1,
        lookup = LOOKUP_NAME_CHAR,
    ),

    'player_sick_days': Feature(
        shark_addr = 0x8016F8F5,
        n_bytes = 1
    ),

    'player_stamina': Feature(
        shark_addr = 0x80189060,
        n_bytes = 1,
    ),

    'player_stamina_max': Feature(
        shark_addr = 0x8020563F,
        n_bytes = 1,
    ),

    'popuri_affection': Feature(
        shark_addr = 0x801C3F91,
        n_bytes = 1,
    ),

    'popuri_conversation': Feature(
        shark_addr = 0x8016F8CF,
        n_bytes = 1,
        mask = 0x02,
    ),

    'popuri_gift': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        mask = 0x40,
    ),

    'popuri_location_byte': Feature(
        shark_addr = 0x801FBA1B,
        n_bytes = 1,
    ),

    'potion_master_affection': Feature(
        shark_addr = 0x801C3FA3,
        n_bytes = 1,
    ),

    'potion_master_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x04,
    ),

    'potion_master_location_byte': Feature(
        shark_addr = 0x801FBCEB,
        n_bytes = 1,
    ),

    'rick_affection': Feature(
        shark_addr = 0x801C3FA8,
        n_bytes = 1,
    ),

    'rick_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x01,
    ),

    'rick_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        mask = 0x20,
    ),

    'rick_location_byte': Feature(
        shark_addr = 0x801FBDB3,
        n_bytes = 1,
    ),

    'saibara_affection': Feature(
        shark_addr = 0x801C3FAB,
        n_bytes = 1,
    ),

    'saibara_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x02,
    ),

    'saibara_gift': Feature(
        shark_addr = 0x8016F8D1,
        n_bytes = 1,
        mask = 0x40,
    ),

    'saibara_location_byte': Feature(
        shark_addr = 0x801FBE2B,
        n_bytes = 1,
    ),

    'shipper_affection': Feature(
        shark_addr = 0x801C3FAA,
        n_bytes = 1,
    ),

    'shipper_conversation': Feature(
        shark_addr = 0x8016F8D3,
        n_bytes = 1,
        mask = 0x08,
    ),

    'shipper_gift': Feature(
        shark_addr = 0x8016F8D6,
        n_bytes = 1,
        mask = 0x01,
    ),

    'shipper_location_byte': Feature(
        shark_addr = 0x801FBE03,
        n_bytes = 1,
    ),

    'sickle_level': Feature(
        shark_addr = 0x8018907F,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_LEVEL,
    ),

    'sickle_uses': Feature(
        shark_addr = 0x8118906A,
        n_bytes = 2,
    ),

    'sprite_1_affection': Feature(
        shark_addr = 0x801C3FB1,
        n_bytes = 1,
    ),

    'sprite_1_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        mask = 0x04,
    ),

    'sprite_1_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x80,
    ),

    'sprite_1_location_byte': Feature(
        shark_addr = 0x801FBF1B,
        n_bytes = 1,
    ),

    'sprite_2_affection': Feature(
        shark_addr = 0x801C3FB2,
        n_bytes = 1,
    ),

    'sprite_2_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        mask = 0x04,
    ),

    'sprite_2_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x80,
    ),

    'sprite_2_location_byte': Feature(
        shark_addr = 0x801FBF43,
        n_bytes = 1,
    ),

    'sprite_3_affection': Feature(
        shark_addr = 0x801C3FB3,
        n_bytes = 1,
    ),

    'sprite_3_conversation': Feature(
        shark_addr = 0x8016F8CC,
        n_bytes = 1,
        mask = 0x04,
    ),

    'sprite_3_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x80,
    ),

    'sprite_3_location_byte': Feature(
        shark_addr = 0x801FBF6B,
        n_bytes = 1,
    ),

    'stu_affection': Feature(
        shark_addr = 0x801C3FA5,
        n_bytes = 1,
    ),

    'stu_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x10,
    ),

    'stu_gift': Feature(
        shark_addr = 0x8016F8D0,
        n_bytes = 1,
        mask = 0x02,
    ),

    'stu_location_byte': Feature(
        shark_addr = 0x801FBD3B,
        n_bytes = 1,
    ),

    'time_day_number': Feature(
        shark_addr = 0x80158260,
        n_bytes = 1,
    ),

    'time_hours': Feature(
        shark_addr = 0x801FB5CA,
        n_bytes = 1,
    ),

    'time_minutes': Feature(
        shark_addr = 0x8017027F,
        n_bytes = 1,
    ),

    'time_season': Feature(
        shark_addr = 0x80182DB1,
        n_bytes = 1,
        lookup = LOOKUP_SEASON,
    ),

    'time_weekday': Feature(
        shark_addr = 0x801FAD90,
        n_bytes = 1,
        lookup = LOOKUP_WEEKDAY,
    ),

    'time_year': Feature(
        shark_addr = 0x801F6F30,
        n_bytes = 1,
    ),

    'tool_slot_1': Feature (
        shark_addr = 0x80189075,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_SLOT,
    ),

    'tool_slot_2': Feature (
        shark_addr = 0x80189076,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_SLOT,
    ),

    'tool_slot_3': Feature (
        shark_addr = 0x80189077,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_SLOT,
    ),

    'tool_slot_4': Feature (
        shark_addr = 0x80189078,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_SLOT,
    ),

    'tool_slot_5': Feature (
        shark_addr = 0x80189079,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_SLOT,
    ),

    'tool_slot_6': Feature (
        shark_addr = 0x8018907A,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_SLOT,
    ),

    'tool_slot_7': Feature (
        shark_addr = 0x8018907B,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_SLOT,
    ),

    'tool_slot_8': Feature (
        shark_addr = 0x8018907C,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_SLOT,
    ),

    'water_level': Feature(
        shark_addr = 0x80189083,
        n_bytes = 1,
        lookup = LOOKUP_TOOL_LEVEL,
    ),

    'water_remaining': Feature(
        shark_addr = 0x8016FBCD,
        n_bytes = 1,
    ),

    'water_uses': Feature(
        shark_addr = 0x81189072,
        n_bytes = 2,
    ),

    'weather_today': Feature(
        shark_addr = 0x802373A9,
        n_bytes = 1,
        lookup = LOOKUP_WEATHER,
    ),

    'weather_tomorrow': Feature(
        shark_addr = 0x80205238,
        n_bytes = 1,
        lookup = LOOKUP_WEATHER,
    ),

}
