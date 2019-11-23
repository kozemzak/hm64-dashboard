from constants import PROCESS_NAME, ROM_ANCHOR, ROM_NAME
from utils import process_features
from features import features
from MemWorker import MemWorker
from functional import seq

class GameState:
    def __init__(self, memworker, features):
        self.memworker = memworker
        self._features = features

    @classmethod
    def from_rom_constants(cls):
        memworker = MemWorker.from_process_info(PROCESS_NAME, ROM_NAME)
        return cls(memworker, features)

    def get_features(self):
        features = seq(self._features.items()) \
            .map(lambda kv: (kv[0], kv[1].get_value(self.memworker))) \
            .to_dict()
        return process_features(features)
