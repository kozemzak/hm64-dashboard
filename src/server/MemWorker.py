from constants import ROM_ANCHOR
from ctypes.util import find_library
import ctypes
from functional import seq
import functools
import logging
import psutil

libc = ctypes.CDLL(find_library('c'))

VM_PROT_READ = 1

class VM_REGION_BASIC_INFO(ctypes.Structure):
    _fields_ = [
        ('protection', ctypes.c_uint32),
        ('max_protection', ctypes.c_uint32),
        ('inheritance', ctypes.c_uint32),
        ('shared', ctypes.c_uint32),
        ('reserved', ctypes.c_uint32),
        ('offset', ctypes.c_ulonglong),
        ('behavior', ctypes.c_uint32),
        ('user_wired_count', ctypes.c_ushort),
    ]

class MemWorker:
    """ Implements a class for interacting with another process' memory.

        Methods:
            mem_search(pattern)
            read_bytes(addr, nbytes)
    """
    def __init__(self, task):
        self.task = task

    @property
    @functools.lru_cache()
    def rom_addr(self):
        results = list(self.mem_search(ROM_ANCHOR))
        assert len(results) == 1, \
            'There was an error retrieving the memory location of the ROM'
        return results[0]

    @staticmethod
    def find_matching_pids(name, cmdline):
        """ Identifies all PIDs for processes that meet the information provided.
    
        Args:
            name (string): A substring matching the name of the process(es) of 
                interest
            cmdline (string): A substring matching the command line of the
                process(es) of interest
    
        Returns:
            (list): A list of PIDs for the process(es) of interest in order of
                least recently created to most recently created process.
        """
        return seq(psutil.process_iter()) \
            .map(lambda x: x.as_dict(attrs = ['pid', 'name', 'cmdline', 'create_time'])) \
            .filter(lambda x: x['name'] is not None) \
            .filter(lambda x: name in x['name']) \
            .filter(lambda x: cmdline in ' '.join(x['cmdline'])) \
            .sorted(lambda x: x['create_time']) \
            .map(lambda x: x['pid']) \
            .to_list()

    @classmethod
    def from_pid(cls, pid):
        """ Creates and returns a MemWorker instance given a PID.

        Args:
            pid (int): ID of target process

        Returns:
            (MemWorker obj): For the process with given PID
        """
        task = ctypes.c_uint32()
        status = libc.task_for_pid(
            libc.mach_task_self(), 
            ctypes.c_int(pid), 
            ctypes.pointer(task),
        )
        if status != 0:
            raise Exception(f'task_for_pid failed with error code: {status}.')

        return cls(task)

    @classmethod
    def from_process_info(cls, name, cmdline):
        """ Creates and returns a MemWorker instance given information about a 
            target process' name and command line.

            Args:
            name (string): A substring matching the name of the process(es) of 
                interest
            cmdline (string): A substring matching the command line of the
                process(es) of interest

            Returns:
                (MemWorker obj): For the most-recently opened process
                satisfying the name and command line criteria.
        """
        pids = cls.find_matching_pids(name, cmdline)  # sorted least to most recently created
        
        if not pids:
            raise Exception(f'No process exists with "{name}" in name and "{cmdline}" in \
                command line.')
        
        elif len(pids) > 1:
            logger.warning(f'More than one process exists with "{name}" in name and \
                "{cmdline}" in command line. The most recently opened process will be used.')

        return cls.from_pid(pids[-1])

    def mem_iter(self):
        address = ctypes.c_ulong(0)
        size = ctypes.c_ulong(0)
        flavor = 9
        info = VM_REGION_BASIC_INFO()
        info_count = ctypes.c_uint32(ctypes.sizeof(info) // 4)
        name = ctypes.c_uint32(0)

        while True:
            status = libc.mach_vm_region(
                self.task,
                ctypes.pointer(address),
                ctypes.pointer(size),
                flavor,
                ctypes.pointer(info),
                ctypes.pointer(info_count),
                ctypes.pointer(name),
            )

            if status == 1:
                break

            if status != 0: 
                raise Exception(f'mach_vm_region failed with error code: {status}')

            if info.protection & VM_PROT_READ:
                yield address.value, size.value

            address.value += size.value

    def mem_search(self, pattern):
        for offset, n_bytes in self.mem_iter():
            try:
                buf = self.read_bytes(offset, n_bytes)
            except Exception as e:
                logging.warning(e)
                continue

            index = buf.find(pattern)
            while index != -1:
                yield offset + index
                index = buf.find(pattern, index + 1)

    def read_bytes(self, address, n_bytes):
        data = ctypes.c_void_p(0)
        data_count = ctypes.c_uint32(0)

        status = libc.mach_vm_read(
            self.task, 
            ctypes.c_ulonglong(address), 
            ctypes.c_longlong(n_bytes), 
            ctypes.pointer(data), 
            ctypes.pointer(data_count),
        )



        if status != 0:
            raise Exception(f'mach_vm_read returned: {status}')
        
        buf = ctypes.string_at(data.value, data_count.value)
        libc.vm_deallocate(self.task, data, data_count)
        return buf
        
