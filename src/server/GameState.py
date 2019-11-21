from features import features
from MemWorker import MemWorker
from functional import seq
from utils import find_pid, get_rom_address, merge_name_chars_to_string

class GameState:
    def __init__(self, memworker, rom_address, features):
        self.memworker = memworker
        self.rom_address = rom_address
        self._features = features

    @classmethod
    def from_rom_name(cls, rom_name):
        pid = find_pid(rom_name)
        memworker = MemWorker(pid)
        rom_address = get_rom_address(memworker)
        return cls(memworker, rom_address, features)

    def get_group_features(self, group):
        group_features = seq(self._features) \
            .filter(lambda kv: group in kv[1].groups) \
            .map(lambda kv: (kv[0], kv[1].get_value(self.memworker, self.rom_address))) \
            .to_dict()
        return merge_name_chars_to_string(group_features)
