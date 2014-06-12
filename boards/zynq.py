
from generic import GenericBoard

class ZynqBoard(GenericBoard):
    def __init__(self):
        pass
        
    @classmethod
    def match(cls, e):
        return e.HARDWARE == "Xilinx Zynq Platform"
    
