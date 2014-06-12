
import re
import os

RE_OUI = "([\da-f]{2}:){2}[\da-f]{2}$"
MANUFACTURERS = {}

for line in open(os.path.join(os.path.dirname(__file__), "manuf")):
    line = line.strip()
    if not line:
        continue
    if line.startswith("#"):
        continue

    oui, remainder = line.split("\t", 1)
    oui = oui.lower()
    if not re.match(RE_OUI, oui):
        continue
    if "#" in remainder:
        _, remainder = remainder.split("#", 1)
        remainder = remainder.strip()
    MANUFACTURERS[oui] = remainder

def get(hardware_address, fallback="Unknown"):
    return MANUFACTURERS.get(hardware_address[:8], fallback)