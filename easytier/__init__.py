
import os
import sys
from ._easytier_cffi import ffi

class EasyTier:
    def __init__(self):
        lib_dir = os.path.join(os.path.dirname(__file__), 'lib')
        if sys.platform == 'win32':
            lib_path = os.path.join(lib_dir, 'easytier_ffi.dll')
        elif sys.platform == 'darwin':
            lib_path = os.path.join(lib_dir, 'libeasytier_ffi.dylib')
        else:
            lib_path = os.path.join(lib_dir, 'libeasytier_ffi.so')
        self.libeasytier = ffi.dlopen(lib_path)

    def parse_config(self, config: str) -> int:
        """
        Parse the configuration string into a list of key-value pairs.
        :param config: Configuration string to parse.
        :return: List of key-value pairs as dictionaries.
        """
        return self.libeasytier.parse_config(config.encode('utf-8'))

    def run_network_instance(self, config: str) -> int:
        """
        Run the network instance with the given configuration.
        This method uses the EasyTier CFFI bindings to execute a network instance
        :param config: Configuration for the network instance.
        :return: Result of running the network instance.
        """
        return self.libeasytier.run_network_instance(config.encode('utf-8'))
    
__doc__ = "easytier: A Python wrapper for EasyTier CFFI bindings" 

__version__= "0.1.0"