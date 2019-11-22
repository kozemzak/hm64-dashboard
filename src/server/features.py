from lookups import *
from Feature import Feature

features = {

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
        lookup = LOOKUP_CHICKEN_LOCATION,
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
        lookup = LOOKUP_CHICKEN_LOCATION,
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
        lookup = LOOKUP_CHICKEN_LOCATION,
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
        lookup = LOOKUP_CHICKEN_LOCATION,
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
        lookup = LOOKUP_CHICKEN_LOCATION,
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
        lookup = LOOKUP_CHICKEN_LOCATION,
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

    'num_fish_caught': Feature(
        shark_addr = 0x8118983A,
        n_bytes = 2,
    ),

    'num_lumber': Feature(
        shark_addr = 0x81189E50,
        n_bytes = 2,
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

    'potion_master_affection': Feature(
        shark_addr = 0x801C3FA3,
        n_bytes = 1,
    ),

    'potion_master_conversation': Feature(
        shark_addr = 0x8016F8CD,
        n_bytes = 1,
        mask = 0x04,
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
