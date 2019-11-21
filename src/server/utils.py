import argparse
from functional import seq
import psutil
import re

GOLD_ADDR_SHARK = 0x1FD60E
GOLD_ADDR_HACK = 0x20177C
ROM_ANCHOR = 'HARVESTMOON64       \x00\x00\x00\x00\x00\x00\x00NYWE'

def handle_args():
    """ Handles command line arguments. Only required argument is ROM name.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'rom_name', 
        type = str, 
        help = 'rom name, ending with .z64',
    )
    args = parser.parse_args()
    return args

def cmdline_contains_rom_name(pinfo, rom_name):
    """
        Returns True if the ROM filename is present in the command line
        of a process, otherwise false.

        Args:
            pinfo (TODO): TODO
            rom_name (string): TODO

        Returns:
            boolean: True if the ROM name is present in the command line of 
            a process, otherwise False
    """
    for cmd in pinfo['cmdline']:
        if rom_name in cmd:
            return True
    return False

def find_pid(rom_name):
    """ Identifies PID of OpenEmu process running a ROM with the provided name.

        Args:
            rom_name (string): File name of ROM ending with .z64

        Returns:
            integer: The PID of the OpenEmu process running specified ROM.
    """
    pinfo = seq(psutil.process_iter()) \
        .map(lambda p: p.as_dict(attrs = ['pid', 'name', 'cmdline'])) \
        .filter(lambda pinfo: pinfo['name'] == 'OpenEmuHelperApp') \
        .filter(lambda pinfo: cmdline_contains_rom_name(pinfo, rom_name)) \
        .to_list()
    assert len(pinfo) <= 1, \
        'No OpenEmu process is open for the ROM %s.' %(rom_name)
    assert len(pinfo) <= 1, \
        'More than one OpenEmu process is open for the ROM %s.' %(rom_name)
    return pinfo[0]['pid']

def get_rom_address(memworker):
    """ Finds the memory address of the anchor in the ROM.
    """
    results = list(memworker.mem_search(ROM_ANCHOR)) # from generator
    assert len(results) == 1, \
        'There was an error retrieving the memory location of the ROM'
    return results[0].value

def shark_to_rom_address(shark_code):
    feature_addr_shark = shark_code & 0x00FFFFFF
    feature_type_shark = shark_code & 0xFF000000
    diff = GOLD_ADDR_SHARK - feature_addr_shark
    feature_addr_rom = GOLD_ADDR_HACK - diff
    feature_addr_rom += -2 * ((feature_addr_hack + 2) % 4) + 5
    if feature_type_shark == 0x81000000:
        feature_addr_rom -= 1
    return feature_addr_rom

def merge_dicts(dict_list):
    merged = dict_list[0].copy()
    for i in range(1, len(dict_list)):
        merged.update(dict_list[i])
    return merged

def merge_name_chars_to_string(data):
    """ Merges characters that are part of a name into a single string.
        
        Args:
            data (dict): key is name of DataItem and value is value of DataItem

        Returns:
            A dictionary with name characters consolidated into name strings.
    """
    name_string_data = seq(data.items()) \
        .filter(lambda kv: 'name_char' in kv[0]) \
        .sorted() \
        .map(lambda kv: (re.split('_char_[0-9]', kv[0])[0], kv[1])) \
        .group_by_key() \
        .map(lambda kv: (kv[0], ''.join(kv[1]))) \
        .to_dict()
    other_data = seq(data.items()) \
        .filter(lambda kv: 'name_char' not in kv[0]) \
        .to_dict()
    return merge_dicts([name_string_data, other_data])
