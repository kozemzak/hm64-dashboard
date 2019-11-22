from constants import GOLD_ADDR_ROM, GOLD_ADDR_SHARK
import struct

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
        lookup (dict): Optional. For numeric values that should be
            interpreted as a character or string. Key is a hex byte.
            Value is a string representing the human meaning.
        mask (hex): Optional. For memory locations storing 2+ indicators.
            Value of feature is true if non-zero value results from
            bit-wise and-ing the mask with the bytes in game memory.

    Note: If neither lookup nor mask is specified, the feature is
        interpreted as an integer.
    """
    def __init__(self, shark_addr, n_bytes, lookup = None, mask = None):
        self.shark_addr = shark_addr
        self.n_bytes = n_bytes
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
 
    @property
    def rom_offset(self):
        feature_addr_shark = self.shark_addr & 0x00FFFFFF
        feature_type_shark = self.shark_addr & 0xFF000000
        diff = GOLD_ADDR_SHARK - feature_addr_shark

        feature_offset_rom = GOLD_ADDR_ROM - diff
        feature_offset_rom += -2 * ((feature_offset_rom + 2) % 4) + 5
        if feature_type_shark == 0x81000000:
            feature_offset_rom -= 1
        return feature_offset_rom
       
    def get_value(self, memworker):
        feature_addr = memworker.rom_addr + self.rom_offset
        raw_mem = memworker.read_bytes(feature_addr, self.n_bytes)
        value = self._int_from_raw_mem(raw_mem)
        
        if self.lookup:
            try:
                return self.lookup[value]
            except Exception as e:
                print(e)
                print(self.lookup)
                return None

        elif self.mask is not None:
            return self._bool_from_mask(value)

        return value
