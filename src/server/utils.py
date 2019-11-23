from functional import seq
import re

def get_heart_color(affection):
    if affection <= 0x33:
        return 'White'
    elif affection >= 0x34 and affection <= 0x67:
        return 'Blue'
    elif affection >= 0x68 and affection <= 0x9B:
        return 'Green'
    elif affection >= 0x9C and affection <= 0xCF:
        return 'Yellow'
    elif affection >= 0xD0:
        return 'Pink'

def add_heart_color_features(features):
    hearts = {}
    hearts['ann_heart_color'] = get_heart_color(features['ann_affection'])
    hearts['elli_heart_color'] = get_heart_color(features['elli_affection'])
    hearts['karen_heart_color'] = get_heart_color(features['karen_affection'])
    hearts['maria_heart_color'] = get_heart_color(features['maria_affection'])
    hearts['popuri_heart_color'] = get_heart_color(features['popuri_affection'])
    return {**features, **hearts}

def merge_name_chars_to_string(features):
    name_string_features = seq(features.items()) \
        .filter(lambda kv: 'name_char' in kv[0]) \
        .sorted() \
        .map(lambda kv: (re.split('_char_[0-9]', kv[0])[0], kv[1])) \
        .group_by_key() \
        .map(lambda kv: (kv[0], ''.join(kv[1]))) \
        .to_dict()
    other_features = seq(features.items()) \
        .filter(lambda kv: 'name_char' not in kv[0]) \
        .to_dict()
    return {**name_string_features, **other_features}

def process_features(features):
    features = merge_name_chars_to_string(features)
    features = add_heart_color_features(features)
    return features

