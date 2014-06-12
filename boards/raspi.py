
from generic import GenericBoard

class RaspberryPi(GenericBoard):
    def __init__(self):
        pass
        
    @classmethod
    def match(cls, e):
        return e.HARDWARE == "BCM2708"
    
