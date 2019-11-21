import struct
from utils import shark_to_rom_address

MEM_FORMATS = {
    1: '<B',
    2: '<H',
    4: '<I',
}

class Feature:
    """ Class for storing each feature from the ROM.

    Attributes:
        shark_addr (hex): Address of feature in game memory using GameShark.
        n_bytes (int): Number of bytes the feature occupies in game memory.
        groups (list): List of strings - groups the feature belongs to.
        lookup (dict): Optional. For numeric values that should be
            interpreted as a character or string. Key is a hex byte.
            Value is a string representing the human meaning.
        mask (hex): Optional. For memory locations storing 2+ indicators.
            Value of feature is true if non-zero value results from
            bit-wise and-ing the mask with the bytes in game memory.

    Note: If neither lookup nor mask is specified, the feature is
        interpreted as an integer.
    """
    def __init__(self, shark_addr, n_bytes, 
        groups = [], lookup = None, mask = None):

        self.shark_addr = shark_addr
        self.n_bytes = n_bytes
        groups = groups
        self.lookup = lookup
        self.mask = mask

    def _int_from_raw_mem(self, raw_mem):
        return struct.unpack(MEM_FORMATS[self.n_bytes], raw_mem)[0]

    def _bool_from_mask(self, value):
        if value == 0 and self.mask == 0:
            return True
        if value & self.mask:
            return True
        return False
        
    def get_value(self, memworker, rom_address):
        value_address = rom_address + shark_to_rom_address(self.shark_code)
        raw_mem = memworker.process.read_bytes(value_address, self.n_bytes)
        value = self._int_from_raw_mem(raw_mem)
        
        if self.lookup:
            return self.lookup[value]

        elif self.mask:
            return self._bool_from_mask(value)

        return value
