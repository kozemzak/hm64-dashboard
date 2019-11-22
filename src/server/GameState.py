from constants import PROCESS_NAME, ROM_ANCHOR, ROM_NAME
from features import features
from MemWorker import MemWorker
from functional import seq
import re

class GameState:
    def __init__(self, memworker, features):
        self.memworker = memworker
        self._features = features

    @staticmethod
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

    @classmethod
    def from_rom_constants(cls):
        memworker = MemWorker.from_process_info(PROCESS_NAME, ROM_NAME)
        return cls(memworker, features)

    def get_features(self):
        features = seq(self._features.items()) \
            .map(lambda kv: (kv[0], kv[1].get_value(self.memworker))) \
            .to_dict()
        return self.merge_name_chars_to_string(features)
